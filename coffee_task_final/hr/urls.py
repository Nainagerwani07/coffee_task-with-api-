from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_changelist'),
    path('add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('<int:pk>/', views.CategoryUpdateView.as_view(), name='category_change'),
    path('ajax/load_cities/', views.load_cities, name='ajax_load_cities'),
    path('add/json_File/',views.json_File),
]
