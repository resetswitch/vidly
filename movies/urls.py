from django.urls import path
from . import views # Note, due to how django loads modules, import views, will not work

app_name = 'movies' #new

# urlpattern is 
urlpatterns = [
    path('', views.index, name='index'),                #modified
    path('<int:movie_id>', views.detail, name='detail') #modified
]
