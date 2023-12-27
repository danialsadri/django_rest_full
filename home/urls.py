from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('question/list/', views.QuestionListView.as_view(), name='question_list'),
    path('question/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/update/<int:question_id>/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/delete/<int:question_id>/', views.QuestionDeleteView.as_view(), name='question_delete'),
]
