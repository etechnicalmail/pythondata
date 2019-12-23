from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor,School ,Coaching
from django.http import JsonResponse
from .serializers import TutorSerializer,SchoolSerializer,CoachingSerializer
from rest_framework import generics

from rest_framework import viewsets


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CoachingViewSet(viewsets.ModelViewSet):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer


def home(request):
    api_data = {
        "Tutor Urls":{
            "List of Tutors [GET Request]": "http://localhost:8000/tutors/",
            "Add Tutor [POST Request]": "http://localhost:8000/tutors/",
            "Get Perticular Tutor [GET Request]": "http://localhost:8000/tutors/<id>",
            "Update Tutor [PUT Request]": "http://localhost:8000/tutors/<id>",
            "Delete Tutor [DELETE Request]": "http://localhost:8000/tutors/<id>"
        },
        "School Urls": {
            "List of Schools [GET Request]": "http://localhost:8000/schools/",
            "Add School [POST Request]": "http://localhost:8000/schools/",
            "Get Perticular School [GET Request]": "http://localhost:8000/schools/<id>",
            "Update School [PUT Request]": "http://localhost:8000/schools/<id>",
            "Delete School [DELETE Request]": "http://localhost:8000/schools/<id>"
        },
        "Coaching Urls": {
            "List of Coachings [GET Request]": "http://localhost:8000/coaching/",
            "Add Coaching [POST Request]": "http://localhost:8000/coaching/",
            "Get Perticular Coaching [GET Request]": "http://localhost:8000/coaching/<id>",
            "Update Coaching [PUT Request]": "http://localhost:8000/coaching/<id>",
            "Delete Coaching [DELETE Request]": "http://localhost:8000/coaching/<id>"
        }
    }
    return JsonResponse(api_data)
