from django.urls import path
from . import views

# This means that when the viewer visits the root or the homepage, the default page will be the data.html file as indicated by the views.get_api_data
# views means the file where the data view is coming from.

urlpatterns = [
    path('', views.get_api_data, name='home'),
]
