from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vocabs/', include('vocab.urls')),
    path('admin/', admin.site.urls),
]
