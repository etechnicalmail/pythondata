from django.shortcuts import get_object_or_404
from .models import Poll
from django.http import JsonResponse

def PollList(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by", "pub_date"))}
    return JsonResponse(data)

def PollDetail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
    "question": poll.question,
    "created_by": poll.created_by.username,
    "pub_date": poll.pub_date
    }}
    return JsonResponse(data)

