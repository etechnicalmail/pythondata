from django.urls import path
from school_app.views import *
from rest_framework.routers import DefaultRouter
from .views import TutorViewSet, SchoolViewSet, CoachingViewSet

router = DefaultRouter()
router.register('tutors', TutorViewSet)
router.register('schools', SchoolViewSet)
router.register('coaching', CoachingViewSet)

urlpatterns = [
    path('', home, name='home_page'),
    ]
urlpatterns += router.urls
