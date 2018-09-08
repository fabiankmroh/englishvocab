from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vocab_id>/', views.detail, name = 'detail'),
    path('insert', views.insert, name='insert' ),
    path('vocab_insert', views.vocab_insert, name='vocab_insert'),
]
