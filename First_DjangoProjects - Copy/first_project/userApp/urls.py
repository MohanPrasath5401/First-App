from django.urls import path, include
from .views import Register,UpdateProfile ,user_change_pass

urlpatterns = [
    path('register/', Register,name="register"),
    path('update/', UpdateProfile,name="update"),
    path('updatepass/', user_change_pass,name="updatepass"),
]