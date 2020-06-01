from rest_framework import serializers
from sim_project.sim_app.models import Read

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ('active_power', 'reactive_power', 'latest_status')

class ActivePowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ('active_power', 'latest_status')

class ReactivePowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ('reactive_power', 'latest_status')