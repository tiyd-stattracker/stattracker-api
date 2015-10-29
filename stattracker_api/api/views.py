from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin,UpdateModelMixin,ListModelMixin
from .permissions import IsOwner
from .models import Activity, Log
from .serializers import ActivitySerializer, ActivityDetailSerializer, LogSerializer, UserSerializer
from datetime import datetime, timedelta, date
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg



# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsOwner)
    queryset = Activity.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivitySerializer
        else:
            return ActivityDetailSerializer

class LogViewSet(viewsets.GenericViewSet, CreateModelMixin,DestroyModelMixin,UpdateModelMixin):
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

class UserViewSet(viewsets.GenericViewSet, CreateModelMixin,ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET'])
# def whoami(request):
#     user = request.user
#     if user.is_authenticated():
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     else:
#         return Response('', status=status.HTTP_404_NOT_FOUND)


def unset_graph(request, activity_pk):
    start_date = request.GET.get('start_date', datetime.today()-timedelta(days=30))
    if type(start_date) == str:
        d = time.strptime(start_date, "%Y-%m-%d")
        start_date = date(d[0],d[1],d[2])
    end_date = request.GET.get('end_date', datetime.today())
    if type(end_date) == str:
        d = time.strptime(end_date, "%Y-%m-%d")
        end_date = date(d[0],d[1],d[2])
    logs = Log.objects.filter(activity=activity_pk, activity_date__gte=start_date, activity_date__lte=end_date)
    dates = [log.activity_date for log in logs]
    counts = [log.activity_count for log in logs]
    f = plt.figure(figsize=(5,4))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.bar(dates, counts)
    plt.title('Activity Count for Selected Period')
    plt.xlim(start_date, end_date)
    plt.xticks(rotation=60)
    plt.yticks([0]+[x+1 for x in range(max(counts))])
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(f)
    return response
