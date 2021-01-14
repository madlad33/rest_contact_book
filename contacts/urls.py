from django.urls import path,include
from rest_framework import routers
from .views import ContactView,CreateContactView,GetAllContactsView

urlpatterns = [
    path('detail/<int:pk>/',ContactView.as_view(),name='update'),
    path('create/',CreateContactView.as_view(),name='create'),
    path('all/',GetAllContactsView.as_view(),name='get_all'),

]
