# -*- coding: utf8 -*-
from django.conf.urls import url
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Bookshelf API",
      default_version='v1',
      description="A very simple bookshelf API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="royarzun@sgmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('', include('social_django.urls', namespace='social')),
   path('api', include('apps.api.urls')),
]
