from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Cycle
from .serializers import UserSerializer, CycleSerializer
from rest_framework.views import APIView, View
from django.http import JsonResponse, JsonResponse
import paho.mqtt.client as mqttc
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

def on_connect(client, userdata, flag, rc):
    print("Connecte with rc = "+str(rc))

client = mqttc.Client()
client.on_connect = on_connect 
client.connect("localhost", 1883)
client.loop_start()

class CycleLockView(APIView):
    def lock(self, val):
        client.publish("lock", val)
    
    def post(self, request):
        user = request.user
        try:
            cycle = Cycle.objects.get(user_id=user.username)
        except Cycle.DoesNotExist:
            return JsonResponse({'error':True, 'message':'Cycle not issued to current user'}, status=403)
        
        if(int(request.POST.get("lock")) == 1):
            self.lock(1)
            cycle.lock = 1
        else:
            self.lock(0)
            cycle.lock = 0
        cycle.save()
        return JsonResponse({'error':False, 'message':'success'})

class CycleBookingView(APIView):

    def post(self, request):
        qrcode = request.POST.get("qrcode")
        try:
            cycle = Cycle.objects.get(qrcode__exact = qrcode)
        except Cycle.DoesNotExist:
            return JsonResponse({'error':True, 'message':'Cycle with the qr code does not exist'}, status=404)
        if(cycle.user!=None):
            return JsonResponse({'error':True, 'message':'Cycle already registered with other user'}, status=400)

        user = request.user
        cycle.user = user
        cycle.save()
        return JsonResponse({'error':False, 'message':'Registered Successfully'}, status=200)

class CycleReturnView(APIView):
    
    def post(self, request):
        user = request.user
        try:
            cycle = Cycle.objects.get(user_id = user.username)
        except Cycle.DoesNotExist:
            return JsonResponse({'error':True, 'message':'No Cycle issued to the current user'}, status=400)
        try: 
            cycle_id = int(request.POST.get('cycle_id'))
        except Exception:
            return JsonResponse({'error':True, 'message': 'Invalid cycle_id'})
        if(cycle_id != cycle.id):
            return JsonResponse({'error':True, 'message': 'Error. The cycle was not issued to the current user'}, status=409)
    
        cycle.user = None
        cycle.save()

        return JsonResponse({'error':False, 'message': 'returned successfully'}, status=200)
