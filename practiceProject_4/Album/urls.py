from django.urls import path
from . import views
urlpatterns = [
    path('',views.album,name='album'),
    path('home/',views.home,name='homepages'),
    path('edit/<int:id>',views.edited,name='edits'),
    path('deleted/<int:id>',views.deleted,name='deleted'),
    
    
]