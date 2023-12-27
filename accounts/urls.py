from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'accounts'
router = routers.SimpleRouter()
router.register(prefix='user', viewset=views.UserViewSet, basename='user')
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('', include(router.urls)),
]
