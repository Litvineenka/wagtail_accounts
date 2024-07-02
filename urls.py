from django.urls import path
from .views import register, login_view, account_settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home_page'), name='logout'),
    path('account_settings/', account_settings, name='account_settings')
]

