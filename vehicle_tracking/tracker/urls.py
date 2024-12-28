from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, JourneyViewSet,get_route

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'journeys', JourneyViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('route/', get_route),
]
