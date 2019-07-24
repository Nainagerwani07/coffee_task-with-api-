from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from hr import views
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(pattern_name='category_changelist'), name='home'),
    path('hr/', include('hr.urls')),
]
