from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    ]
urlpatterns += router.urls