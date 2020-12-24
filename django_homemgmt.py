from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import RPi.GPIO as GPIO
import time
import sys
import asyncio
#GPIO.setwarnings(False)
MAIN_GATE=23
GARAGE_GATE=24
loop = asyncio.get_event_loop()

def bgstuff(output,delay):
   GPIO.output(output, 0)
   time.sleep(delay)
   GPIO.output(output, 1)
#   GPIO.cleanup()

def trigger_main_gate(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,bgstuff(MAIN_GATE,1))
      return HttpResponse('Main Gate has been triggered')
   else:
      return HttpResponse('Not permited.')

def trigger_garage_gate(request):
   if request.user.is_authenticated:
      loop.run_in_executor(None,bgstuff(GARAGE_GATE,0.8))
      return HttpResponse('Garage Gate has been triggered')
   else:
      return HttpResponse('Not permited.')

def home(request):
   if request.user.is_authenticated:
      return render(request, 'home.html')
   else:
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return render(request, 'home.html')
      else:
         return render(request, 'login.html')
