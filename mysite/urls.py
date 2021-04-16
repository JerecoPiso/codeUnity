from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	#   url(r'^$', views.index, name='index'),
	  url(r'^', include('blog.urls')),
	  url(r'^user/', include('blog.user_urls')),
	  url(r'^dashboard/', include('blog.dashboard_urls')),
	  url(r'^adminUser/', include('blog.admin_urls')),
      url('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)