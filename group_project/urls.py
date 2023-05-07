from django.urls import path
from group_project.views import GroupProjectDetail, GroupProjectList

urlpatterns = [
    path('', GroupProjectList.as_view()),
    path('<int:pk>/', GroupProjectDetail.as_view()),
]
