from django.urls import path

from semester import views

urlpatterns = [
    path('', views.SemesterList.as_view()),
    path('<str:pk>/', views.SemesterDetail.as_view()),
]
