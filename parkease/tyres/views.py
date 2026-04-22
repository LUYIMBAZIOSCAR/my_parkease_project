from django.shortcuts import render,redirect
from .forms import TyreServiceForm

# Create your views here.

# view for tyre service
def tyre_service(request):
    if request.method=='POST':
        form=TyreServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager1_dashboard')
    else:
        form=TyreServiceForm()

    return render(request,'tyres/tyre.html',{'form':form})
