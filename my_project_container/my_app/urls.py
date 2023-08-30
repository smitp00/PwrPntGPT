from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('admin/', admin.site.urls),
    path('upload_ppt/', views.upload_ppt, name='upload_ppt'),
    path('upload_word/', views.upload_word, name='upload_word'),
    path('', views.home, name='home'),  # Note this new line
]