from django.shortcuts import render,redirect
from .forms import BatteyServiceForm

# Create your views here.

# view for battery service
def battery_service(request):
    if request.method=='POST':
        form=BatteyServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager2_dashboard')
    else:
        form=BatteyServiceForm()
    return render(request,'battery/battery.html',{'form':form})

