from django.urls import path
from . import views
urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('home/',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('packages/',views.packages,name='packages'),
    path('partners/',views.partners,name='partners'),
    path('events/',views.events,name='events'),
    path('trips/',views.trips,name='trips')
]