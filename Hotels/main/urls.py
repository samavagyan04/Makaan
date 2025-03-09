from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterPage,name='register'),
    path('login/',LoginPage,name='login'),
    path('logout/',Logout,name='logout'),
    #---------------------------------------------------
    path('',HomeListView.as_view(),name='home'),
    path('about/',AboutListView.as_view(),name='about'),
    path('pr_list/',PropertyListView.as_view(),name = 'pr_list'),
    path('pr_type/',PropertyType.as_view(),name = 'pr_type'),
    path('pr_agent/',PropertyAgents.as_view(),name = 'pr_agent'),
    path('testimonial/',Testimonial.as_view(),name = 'testimonial'),
    path('contact/',ContactPage.as_view(),name = 'contact'),
    path('search/',SearchItem,name='search'),
]