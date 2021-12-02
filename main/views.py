from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api import main

@csrf_exempt
def IndexView(request):

	message = {
		"message": "Ray Welcomes You!"
	}
	

	return JsonResponse(message)



@csrf_exempt
def ChartOne(request):

	results = main()

	return JsonResponse(results)
	
