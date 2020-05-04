from django.shortcuts import render
from django.http import JsonResponse
from hallpass.models import EncryptedData
import time

def doctor(request):
	return render(request, "doctor.html")

def fetch_data(request):
	pk = request.POST.get("pk")
	d = EncryptedData.objects.get(public_key=pk)
	return JsonResponse({'data': d.data})



