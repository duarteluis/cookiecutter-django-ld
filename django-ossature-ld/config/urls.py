"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static

from django.views.i18n import set_language

from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

from django.contrib.sitemaps.views import sitemap
from apps.pages.sitemaps import StaticSitemap as PagesSitemap
from allauth.account.decorators import secure_admin_login

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

# Title admin website
admin.site.site_header = "LAD - admin website"
admin.site.index_title = "LAD"
admin.site.site_title = "admin website"


sitemaps = {
    "pages": PagesSitemap,
}


def staff_required(view_func):
    """
    Décorateur qui :
    - redirige vers la page de login si non connecté,
    - retourne une erreur 403 personnalisée si l'utilisateur n'est pas staff.
    """

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login

            return redirect_to_login(request.get_full_path())
        elif not request.user.is_staff:
            return HttpResponseForbidden(
                "<h1>403 Forbidden</h1><p>Vous n'avez pas les droits pour accéder à cette documentation.</p>"
            )
        return view_func(request, *args, **kwargs)

    return wrapper


urlpatterns = (
    [
        path("i18n/setlang/", set_language, name="set_language"),
        path("admin/", admin.site.urls),
        # path("tinymce/", include("tinymce.urls")),
        # path("", include("apps.pages.urls")),
        # path("tinymce/", include("tinymce.urls")),
        # path("lead/", tracking_views.lead_form, name="lead_form"),
        # path("thank-you/", tracking_views.thank_you, name="thank_you"),
        # path("track-action/", tracking_views.track_action, name="track_action"),
        # path(
        #     "conversion-report/",
        #     tracking_views.conversion_report,
        #     name="conversion_report",
        # ),
        re_path(r"^robots\.txt", include("robots.urls")),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
        path("accounts/", include("allauth.urls")),
        path("rosetta/", include("rosetta.urls")),
        # path(
        #     "messages/initial/", pages_views.messages_initial, name="messages_initial"
        # ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)

urlpatterns += i18n_patterns(
    path("", include("apps.pages.urls")),
)
