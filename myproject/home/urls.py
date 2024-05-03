from django.urls import path
from home.views import index,show_all_books


urlpatterns = [
    path('',index, name='home-index'),
    
]