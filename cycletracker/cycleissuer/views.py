from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Cycle
from .serializers import UserSerializer, CycleSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
import paho.mqtt.client as mqttc
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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

class LockView(APIView):
    def lock(self, val):
        client.publish("lock", val)
    
    def post(self, request):
        if(int(request.POST.get("lock")) == 1):
            self.lock(1)
        else:
            self.lock(0)
        return HttpResponse('success')
