from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # 1. MAIN LANDING PAGE
    path('', views.landing_page, name='landing_page'),

    # 2. ROLE SELECTION HUBS
    path('choose-login/', views.welcome_role, name='welcome_role'),
    path('choose-signup/', views.role_selection, name='choose_signup'),

    # 3. LOGIN FORMS
    path('login/admin/', views.admin_login, name='admin_login'),
    path('login/warden/', views.warden_login, name='warden_login'),
    path('login/worker/', views.worker_login, name='worker_login'),
    path('login/supplier/', views.supplier_login, name='supplier_login'),

    # 4. SIGNUP FORMS
    path('signup/worker/', views.worker_signup_view, name='worker_signup'),
    path('signup/warden/', views.warden_signup_view, name='warden_signup'),
    path('signup/supplier/', views.supplier_signup_view, name='supplier_signup'),

    # 5. SYSTEM PATHS (Admin and Language)
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]