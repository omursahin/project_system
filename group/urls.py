from django.urls import path

urlpatterns = [
    path('', GroupListView.as_view(), name='group-list'),
    path('<int:pk>', GroupRetrieveUpdateDestroyView.as_view(), name='group-detail'),
]