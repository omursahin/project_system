"""project_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.models import MyUser


# Duzeltmek icin ctrl+alt+L
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['url', 'identication_number', 'first_name', 'last_name',
                  'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    @action(methods=('GET',), detail=False, url_path='me', url_name='me')
    def me(self, request, *args, **kwargs):
        User = get_user_model()
        self.object = get_object_or_404(User, pk=request.user.id)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Project System API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/account/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/account/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    path('api/v1/semesters/', include('semester.urls')),
    path('api/v1/courses/', include('course.urls')),
    path('api/v1/semester_courses/', include('semester_course.urls')),
    path('api/v1/semester_course_students/',
         include('semester_course_student.urls')),
    path('api/v1/groups/', include('group.urls')),
    path('api/v1/reports/', include('report.urls')),
    path('api/v1/group_projects/', include('group_project.urls')),
    path('api/v1/group_member/', include('group_member.urls')),
    path('api/v1/project_reports/', include('project_report.urls')),
]
