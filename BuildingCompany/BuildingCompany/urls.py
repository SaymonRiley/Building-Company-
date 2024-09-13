from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import index  # Импортируем только функцию index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Используем просто index
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
