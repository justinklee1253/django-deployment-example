from django.urls import path
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app' #tell django to look under basic_app and find url that matches

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
