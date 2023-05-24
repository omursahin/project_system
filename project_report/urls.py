from django.urls import path
from project_report.views \
    import ProjectReportList, \
    ProjectReportDetail

urlpatterns = [
    path('', ProjectReportList.as_view()),
    path('<int:pk>/', ProjectReportDetail.as_view()),
]
