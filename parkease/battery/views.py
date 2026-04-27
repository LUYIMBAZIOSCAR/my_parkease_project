from django.shortcuts import render,redirect,get_object_or_404
from .forms import BatteyServiceForm
from .models import BatteryService
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# view for battery service
@login_required
def battery_service(request):
    if request.user.profile.role !='manager2':
        return redirect('login')
    if request.method=='POST':
        form=BatteyServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager2_dashboard')
    else:
        form=BatteyServiceForm()
    return render(request,'battery/battery.html',{'form':form})

# view function to delete battery service
@login_required
def delete_battery_service(request,service_id):
    if request.user.profile.role !='admin':
        return redirect('login')
    battery_service=get_object_or_404(BatteryService,id=service_id)
    if request.method=='POST':
        battery_service.delete()
        messages.success(request,'Service successfully deleted')
        return redirect('records')
    return redirect('records')



