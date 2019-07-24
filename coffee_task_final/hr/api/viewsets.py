from hr.models import Machine, Type, WL, Flavour, PackSize, Coffee_Pod, Category
from .serializers import MachineSerializer, AvilabelOptionSerializer, TypeSerializer, WaterLineSerializer, FlavourSerializer, PackSizeSerializer, CoffeePodSerializer
from rest_framework import viewsets

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class WaterLineViewSet(viewsets.ModelViewSet):
    queryset = WL.objects.all()
    serializer_class = WaterLineSerializer

class FlavourViewSet(viewsets.ModelViewSet):
    queryset = Flavour.objects.all()
    serializer_class = FlavourSerializer

class PackSizeViewSet(viewsets.ModelViewSet):
    queryset = PackSize.objects.all()
    serializer_class = PackSizeSerializer

class CoffeePodViewSet(viewsets.ModelViewSet):
    queryset = Coffee_Pod.objects.all()
    serializer_class = CoffeePodSerializer

class AvilabelOptionViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AvilabelOptionSerializer
