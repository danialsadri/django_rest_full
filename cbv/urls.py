from django.urls import path
from . import views


app_name = 'cbv'
urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('list/', views.CarListView.as_view(), name='car_list'),
    path('retrieve/<str:my_name>/', views.CarRetrieveView.as_view(), name='car_retrieve'),
    path('delete/<str:my_name>/', views.CarDeleteView.as_view(), name='car_delete'),
    path('update/<str:my_name>/', views.CarUpdateView.as_view(), name='car_update'),
    path('list_create/', views.CarListCreateView.as_view(), name='car_list_create'),
    path('retrieve_update_destroy/<str:my_name>/', views.CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_destroy'),
    path('generic/<int:pk>/', views.CarGenericView.as_view(), name='car_generic'),
]
