from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	  url(r'^$', views.index, name='index'),
	  url(r'^codeunity/', include('blog.urls')),
	  url(r'^codeunity/user/', include('blog.admin_urls')),
      url('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)