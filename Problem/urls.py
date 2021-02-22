from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MyProblemView.as_view(), name='problems'),
    path('add-problem/', views.AddProblemView.as_view(), name='add_problem'),
    path('delete-problem/<str:slug>/', views.DeleteProblemView.as_view(), name='delete_problem')
]