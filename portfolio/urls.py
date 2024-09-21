from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('contact/', views.contact_view, name='contact'),

]