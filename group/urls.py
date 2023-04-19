from django.urls import path
from group.views import GroupDetail, GroupList

urlpatterns = [
    path('', GroupList.as_view(), name='group-list'),
    path('<int:pk>/', GroupDetail.as_view(), name='group-detail'),
]
