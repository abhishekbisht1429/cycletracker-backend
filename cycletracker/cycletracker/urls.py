"""cycletracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cycleissuer import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('cycles', views.CycleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cycleissuer/', include(router.urls)),
    path('cycleissuer/cycle/lock', csrf_exempt(views.CycleLockView.as_view())),
    path('cycleissuer/cycle/book', csrf_exempt(views.CycleBookingView.as_view())),
    path('cycleissuer/cycle/return', csrf_exempt(views.CycleReturnView.as_view())),
    path('cycleissuer/cycle/booked', csrf_exempt(views.CycleIdView.as_view())),
    path('cycleissuer/auth/', include('djoser.urls')),
    path('cycleissuer/auth/', include('djoser.urls.authtoken'))
]
