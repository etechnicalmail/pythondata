from .models import Poll
from django.http import JsonResponse
from .serializers import PollSerializer

from rest_framework import viewsets

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
