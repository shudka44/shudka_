# filepath: /c:/Users/Honor/Desktop/SHUDKA44/SHUDKA44/SHUDKA44/urls.py
from django.contrib import admin
from django.urls import path, include
from Store import views as store_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store_views.home, name='home'),
    path('store/', include('Store.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)