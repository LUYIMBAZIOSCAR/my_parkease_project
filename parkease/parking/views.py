from django.shortcuts import render

# Create your views here.
def register_vehicle(request):
    return render(request,'parking/register_vehicle.html')

