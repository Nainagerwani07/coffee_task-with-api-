from hr.api.viewsets import MachineViewSet, AvilabelOptionViewSet, TypeViewSet, WaterLineViewSet, FlavourViewSet, PackSizeViewSet, CoffeePodViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Machine',MachineViewSet)
router.register('Type',TypeViewSet)
router.register('WL',WaterLineViewSet)
router.register('Flavour',FlavourViewSet)
router.register('PackSize',PackSizeViewSet)
router.register('Coffee_Pod',CoffeePodViewSet)
router.register('Category',AvilabelOptionViewSet)
