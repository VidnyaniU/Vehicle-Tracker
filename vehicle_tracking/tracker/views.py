from rest_framework import viewsets
from .models import Vehicle, Journey
from .serializers import VehicleSerializer, JourneySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import calculate_route

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


@api_view(['POST'])
def get_route(request):
    origin = request.data.get('origin')
    destination = request.data.get('destination')
    if not origin or not destination:
        return Response({"error": "Origin and destination are required."}, status=400)

    route = calculate_route(origin, destination)
    return Response(route)
