from django.urls import path
from  .import views
from main.views import*


app_name = "main"


urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.aboutus, name='aboutus'),
    path('training/', views.training, name='training'),
    path('supplies/', views.eqpt, name='eqpt')
]