from django.contrib import admin
from .models import Tutor
from.models import School
from.models import Coaching


admin.site.register(Tutor)
admin.site.register(School)
admin.site.register(Coaching)