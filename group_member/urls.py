from django.urls import path

from group_member.views import GroupMemberList, GroupMemberDetail

urlpatterns = [
    path('', GroupMemberList.as_view(), name='group-member-list'),
    path('<int:pk>/', GroupMemberDetail.as_view(), name='group-member-detail'),
]
