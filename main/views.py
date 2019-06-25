from django.shortcuts import render
import time
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.

def update_field2(request):
    test_model = TestModel.objects.get(pk=2)
    initial_value = test_model.field2
    current_version = test_model.version
    print("suspend")
    
    
    time.sleep(5)


    test_model.field2 = initial_value + 1
    test_model.field3 = False
    print(current_version)
    test_model.save(current_version)

    return HttpResponse(initial_value + 1)
    
    