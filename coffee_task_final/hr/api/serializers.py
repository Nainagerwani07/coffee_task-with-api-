from rest_framework import serializers
from hr.models import Machine, Type, WL, Flavour, PackSize, Coffee_Pod, Category

class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machine
        fields = ('name',)

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Type
    	fields = ('name',)

class WaterLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = WL
    	fields = ('name',)

class FlavourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Flavour
    	fields = ('name',)

class PackSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = PackSize
    	fields = ('name',)

class CoffeePodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Coffee_Pod
    	fields = ('name',)

class AvilabelOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Category
    	fields = ('option',)