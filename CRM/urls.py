
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from leads.views import landing_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing_page,name='landing-page'),
    path('leads/', include('leads.urls', namespace="leads")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)