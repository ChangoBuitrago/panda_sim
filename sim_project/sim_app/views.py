from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from django.http import Http404
from sim_project.sim_app.models import Read
from sim_project.sim_app.api import test_sim
from django.core import serializers
from sim_project.sim_app.serializers import ActivePowerSerializer, ReactivePowerSerializer, TaskSerializer

class Tasks(APIView):
    """
    POST request that launches the simulation using the aforementioned Python module. 
    he response should include the active and reactive power of the load in JSON format
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny ,)

    def post(self, request, format=None):
        """
        Launches the simulation
        """
        result = test_sim.run_simulation()

        # Validate sim result
        # NB: Thorough validation required.
        if not isinstance(result, tuple):
            return Response({ 'status': 'Simulation failing.' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Saving read 
        ( active_power, reactive_power ) = result
        
        read = Read.objects.create(
            active_power=active_power, 
            reactive_power=reactive_power
        )
        serializer = TaskSerializer(read)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivePower(APIView):
    """
    GET request that reads the active power of the previously executed simulation
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny ,)

    def get_object(self):
        try:
            return Read.objects.latest('latest_status')
        except Read.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
        Return Acttive Power reads.
        """
        read = self.get_object()
        serializer = ActivePowerSerializer(read)
        return Response(serializer.data)


class ReactivePower(APIView):
    """
    GET request that reads the reactive power of the previously executed simulation
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny ,)

    def get_object(self):
        try:
            return Read.objects.latest('latest_status')
        except Read.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
        Return Reactive Power reads.
        """
        read = self.get_object()
        serializer = ReactivePowerSerializer(read)
        return Response(serializer.data)