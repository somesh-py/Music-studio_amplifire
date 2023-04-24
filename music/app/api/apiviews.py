from rest_framework import generics
from .serializers import MusicRegSerializer
from ..models import MusicReg



class ListCreateAPIView(generics.ListCreateAPIView):
        queryset=MusicReg.objects.all()
        serializer_class=MusicRegSerializer

class UpdateDeleteRetriveAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset=MusicReg.objects.all()
        serializer_class=MusicRegSerializer