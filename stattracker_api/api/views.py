from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Activity, Log
from .serializers import ActivitySerializer, LogSerializer
from datetime import datetime

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def get_queryset(self):
        activity_pk = self.kwargs['activity_pk']
        activity = get_object_or_404(Activity, pk=activity_pk)
        return self.queryset.filter(activity=activity)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['activity_id'] = self.kwargs['activity_pk']
        return context
