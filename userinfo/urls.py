from django.urls import path
from userinfo import views

urlpatterns = [
    path('register/',views.register),

]
