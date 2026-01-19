from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from viewer.views import EventListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('events/', EventListView.as_view(template_name='events.html'), name='events'),

    # API
    path('', include('places.urls')),
]


'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''