from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/en/", permanent=True)),
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("crm/", include("crmsb.urls")),
    path("products/", include("product.urls")),
    path("pages/", include("corepages.urls")),
    path("account/", include("account.urls")),
    path("", include("home.urls")),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = "home.views.custom_500"
handler404 = "home.views.custom_404"
