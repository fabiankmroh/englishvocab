from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert' ),
    path('vocab_insert', views.vocab_insert, name='vocab_insert'),
    path('<int:vocab_id>/', views.detail, name = 'detail'),
    path('<int:vocab_id>/insert', views.detail_insert, name = 'detail_insert'),
    path('<int:vocab_id>/insert_save', views.detail_insert_save, name = 'detail_insert_save'),
    path('test_start', views.test_start, name = 'test_start'),
    path('test_form', views.test_form, name = 'test_form'),
    path('test_submit', views.test_submit, name = 'test_submit'),
]
