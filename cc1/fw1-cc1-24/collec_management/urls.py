from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.presentation , name ="presentation"),
    path('new/', views.nouvelle_collec , name ="nouvelle_collec"),
    path('collec/<int:id>/', views.collection_detail, name='collection_detail'),
    path('all/', views.collection_list, name='collection_list'),
    path('', views.principal, name='principal'),
    path('change/<int:collec_id>', views.edit_collec, name="edit"),
    path("delete/<int:id>", views.delete_collection, name="delete_collection"),
]

