from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from datetime import datetime

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
