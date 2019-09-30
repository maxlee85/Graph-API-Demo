from django.urls import path

from . import views

urlpatterns = [
  # /tutorial
  path('', views.home, name='home'),
  path('signin', views.sign_in, name='signin'),
  path('callback', views.callback, name='callback'),
  path('signout', views.sign_out, name='signout'),
  path('calendar', views.calendar, name='calendar'),
  path('onedrive_details', views.onedrive_details, name='onedrive_details'),
  path('onedrive_directory', views.onedrive_directory, name='onedrive_directory'),
  path('directory_contents', views.directory_contents, name='directory_contents'),
]
