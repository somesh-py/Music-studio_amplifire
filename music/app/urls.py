from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .api import apiviews

urlpatterns = [
    path('',views.index),
    path('song/<int:id>',views.song,name='song'),
    path('registersongform',views.registersongform,name="registersongform"),
    path('registersong/',views.registersong),
    path('playlistdata/<int:id>',views.playlistadd,name="playlistdata"),
    path('playlist/',views.playlist),
    path('removesong/<int:id>',views.removesong,name="removesong"),
    # api path urls

    path('api/',apiviews.ListCreateAPIView.as_view()),
    path('api/<pk>',apiviews.UpdateDeleteRetriveAPIView.as_view()),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
