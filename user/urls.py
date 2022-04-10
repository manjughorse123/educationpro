from django.urls import path
from .views import *

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user_create'),
    path('verifyotp/', ValidateOTP.as_view(), name='verify_otp'),
    path('edit_user/<int:pk>/', UserEditDetail.as_view(), name='verify_user'),
    path('validotp/', ValidateOTP.as_view(), name='verify_user')
   
]