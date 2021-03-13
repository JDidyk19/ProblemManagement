from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MyProblemView.as_view(), name='problems'),
    path('add-problem/', views.AddProblemView.as_view(), name='add_problem'),
    path('<str:slug>/', views.DetailProblemView.as_view(), name='problem'),
    path('edit-problem/<str:slug>/', views.EditProblemView.as_view(), name='edit_problem'),
    path('delete-problem/<str:slug>/', views.DeleteProblemView.as_view(), name='delete_problem'),
    path('edit-notate/<int:notate_id>/', views.EditNotateView.as_view(), name='edit_motate'),
    path('delete-notate/<int:notate_id>/', views.DeleteNotateView.as_view(), name='delete_notate'),
]