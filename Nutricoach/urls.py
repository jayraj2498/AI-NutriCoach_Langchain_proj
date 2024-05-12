from django.urls import path 
from Nutricoach.views import Home  


urlpatterns= [ 
              path('' , Home.as_view(), name='home') ]