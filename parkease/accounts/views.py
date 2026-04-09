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
                return redirect('admin_dashboard')
            elif role=='attendant':
                return redirect('attendant_dashboard')

            
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request,'accounts/login.html')


# parking attendant dashboard 
def attendant_dashboard(request):
    return render(request,'accounts/attendant-dashboard.html')

# manager dashboard 
def admin_dashboard(request):
    return render(request,'accounts/admin_dashboard.html')

# view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
