from django.urls import path
from .views import PollList, PollDetail

urlpatterns = [
    path("polls/", PollList, name="polls_list"),
    path("polls/<int:pk>/", PollDetail, name="polls_detail"),
]

