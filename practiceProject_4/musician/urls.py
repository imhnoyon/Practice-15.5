from django.urls import path
from . import views
urlpatterns = [
    path('',views.musician,name='musician'),
   path('edit/<int:id>',views.edited,name='edited'),
    
]