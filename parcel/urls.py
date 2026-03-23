from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_parcel, name='add_parcel'),
    path('list/', views.parcel_list, name='parcel_list'),
    
    
    path('track/', views.track_parcel, name='track_parcel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<int:id>/', views.update_status, name='update_status'),
]