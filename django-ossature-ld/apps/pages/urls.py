from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path(_("faq/"), views.FaqView.as_view(), name="faq"),
    path(_("privacy/"), views.PrivacyPolicyView.as_view(), name="privacy"),
    path(_("terms/"), views.TermsConditionsView.as_view(), name="terms"),
    # path(_("contact-us/"), views.contact_us, name="contact_us"),
]
