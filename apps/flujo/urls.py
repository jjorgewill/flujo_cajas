from django.urls import path

from apps.flujo import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='view_home'),
    #activos
    path('activo/listar/<int:pk>/', views.ActivoView.as_view(), name='update_modal_activo'),
    path('activo/listar/', views.ActivoView.as_view(), name='view_activo'),
    path('activo/crear/', views.ActivoCreateView.as_view(), name='create_activo'),
    path('activo/editar/<int:pk>/', views.ActivoUpdateView.as_view(), name='update_activo'),
    path('activo/elimnar/<int:pk>/', views.ActivoDeleteView.as_view(), name='delete_activo'),

]
