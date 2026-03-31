from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method=="POST":
        body=request.POST
        username=body.get('username')
        password=body.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            role=user.profile.role
            if role=='admin':
                return redirect('admin-dashboard')
            elif role=='attendant':
                return redirect('dashboard')

            
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request,'login.html')


# parking attendant dashboard 
def dashboard(request):
    return render(request,'attendant-dashboard.html')

# manager dashboard 
def manager_dashboard(request):
    return render(request,'manager-dashboard.html')

# view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
