from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
     path('about/',AboutListView.as_view(),name='about')
]