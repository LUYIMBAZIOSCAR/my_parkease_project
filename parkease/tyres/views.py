from django.shortcuts import render,redirect,get_object_or_404
from .forms import TyreServiceForm
from .models import TyreService
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# view for tyre service
@login_required
def tyre_service(request):
    if request.user.profile.role != 'manager1':
        return redirect('login')
    if request.method=='POST':
        form=TyreServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager1_dashboard')
    else:
        form=TyreServiceForm()

    return render(request,'tyres/tyre.html',{'form':form})

# view function for deleting a tyre service
def delete_tyre_service(request,service_id):
    if request.user.profile.role != 'admin':
        return redirect('login')
    tyre_service=get_object_or_404(TyreService,id=service_id)
    if request.method=='POST':
        tyre_service.delete()
        messages.success(request,'Service deleted successfully')
        return redirect('records')
    return redirect('records')
        



