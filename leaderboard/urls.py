from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from example import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^', include('example.urls'))
]