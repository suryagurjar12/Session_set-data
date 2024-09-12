from django.urls import path
from .views import *

urlpatterns = [
    path('',set,name='set'),
    path('get/',get,name='get'),
    path('delete/',delete,name='delete')
    
]
