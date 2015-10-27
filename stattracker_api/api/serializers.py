from rest_framework import serializers
from .models import Activity, Log

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'activity_name','start_date')

class LogSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True,source='activity')

    class Meta:
        model = Log
        fields = ('id', 'activity_id', 'activity_date','activity_count')

    def create(self, validated_data):
        validated_data['activity_id'] = self.context['activity_id']
        log = Log.objects.create(**validated_data)
        return log
