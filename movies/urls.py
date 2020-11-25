from django.urls import path
from . import views # Note, due to how django loads modules, import views, will not work

# urlpattern is 
urlpatterns = [
    path('', views.index, name='index')
]