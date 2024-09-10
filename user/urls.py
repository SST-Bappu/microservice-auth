from django.urls import path

from user.views.registration_view import UserRegistrationView

urlpatterns = [
    # user views
    path('register/', UserRegistrationView.as_view(), name='register'),
]
