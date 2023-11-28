from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.conf.urls.i18n import i18n_patterns
from members.views import download_app
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),]
urlpatterns += i18n_patterns(
    
    path('posts/', include('posts.urls')),
    path('crm/', include('crm.urls')),
    path('products/', include('products.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    


)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = "errorpages.views.error_500"
handler404 = "errorpages.views.error_404"
