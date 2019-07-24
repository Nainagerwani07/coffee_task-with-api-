from django.contrib import admin
from hr.models import Machine , Category , Flavour , Coffee_Pod , Type , PackSize , WL
# Register your models here.
admin.site.register(Machine)
admin.site.register(Category)
admin.site.register(Flavour)
admin.site.register(Coffee_Pod)
admin.site.register(Type)
admin.site.register(PackSize)
admin.site.register(WL)

