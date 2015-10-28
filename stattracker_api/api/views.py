from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin,UpdateModelMixin
from .permissions import IsOwner
from .models import Activity, Log
from .serializers import ActivitySerializer, ActivityDetailSerializer, LogSerializer, UserSerializer
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg



# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = Activity.objects.all()
    # permission_classes = (permissions.IsOwner)
=======
    queryset = Activity.objects.filter(user=request.user)
>>>>>>> master

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

class UserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def whoami(request):
    user = request.user
    if user.is_authenticated():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_404_NOT_FOUND)

def activity_month_graph(request, activity_pk):
    then = datetime.date(datetime.today()) - timedelta(days=30)
    logs = Log.objects.filter(activity=activity_pk, activity_date__gte=then)
    dates = [log.activity_date for log in logs]
    counts = [log.activity_count for log in logs]
    f = plt.figure(figsize=(5,4))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.bar(dates, counts)
    plt.title('Activity Count for Last 30 Days')
    plt.xlim(then, datetime.date(datetime.today()))
    plt.xticks(rotation=60)
    plt.yticks([0]+[x+1 for x in range(max(counts))])
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(f)
    return response
