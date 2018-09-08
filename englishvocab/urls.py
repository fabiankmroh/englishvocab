from django.contrib import admin
from django.urls import path, include

from vocab import views

urlpatterns = [
    path('vocab/', include('vocab.urls')),
    path('admin/', admin.site.urls),
]
