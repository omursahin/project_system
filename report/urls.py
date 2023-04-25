from django.urls import path
from report.views import ReportList, ReportDetail


urlpatterns = [
    path('', ReportList.as_view()),
    path('<int:pk>/', ReportDetail.as_view()),
]
