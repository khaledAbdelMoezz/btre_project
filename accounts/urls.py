from . import views
from django.urls import path



urlpatterns = [
    path('login/', views.login_user, name ="login"),
    path('register/', views.register_user, name ="register"),
    path('dashboard/', views.dashboard, name ="dashboard"),
    path('logout/', views.logout_user, name ="logout"),
]
