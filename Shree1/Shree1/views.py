from django.shortcuts import render

# --- HOME & SELECTION VIEWS ---

def landing_page(request):
    """The main entry point for the SHREE system."""
    return render(request, 'Shree1/home.html')

def welcome_role(request):
    """The role selection page specifically for LOGIN."""
    return render(request, 'Shree1/login_role.html')

def role_selection(request):
    """The role selection page specifically for SIGNUP."""
    return render(request, 'Shree1/signup_role.html')


# --- LOGIN VIEWS ---

def admin_login(request):
    return render(request, 'Shree1/loginAdmin.html') # Based on your screenshot naming

def warden_login(request):
    return render(request, 'Shree1/loginWarden.html')

def worker_login(request):
    return render(request, 'Shree1/loginWorker.html')

def supplier_login(request):
    return render(request, 'Shree1/loginSupplier.html')


# --- SIGNUP VIEWS ---

def worker_signup_view(request):
    return render(request, 'Shree1/signupWorker.html') # Make sure the filename is exact

def warden_signup_view(request):
    return render(request, 'Shree1/signupWarden.html')

def supplier_signup_view(request):
    return render(request, 'Shree1/signupSupplier.html')