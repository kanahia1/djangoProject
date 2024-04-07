from django.contrib import admin
from django.urls import path

from djangoProject import views

urlpatterns = [
    path('', views.home),
    path('process_text/', views.process_text),
    path('admin/', admin.site.urls),
]
