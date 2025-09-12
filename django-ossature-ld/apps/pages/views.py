from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.messages import get_messages
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import json

from django.views.decorators.http import require_POST

from .forms import ContactForm
from .models import ContactUsMessage, FaqQuestionAnswer


class HomePageView(TemplateView):
    template_name = "pages/home/index.html"


class FaqView(ListView):
    template_name = "pages/faq/faq.html"
    model = FaqQuestionAnswer
    paginate_by = 20


class PrivacyPolicyView(TemplateView):
    template_name = "pages/privacy-policy/privacy_policy.html"


class TermsConditionsView(TemplateView):
    template_name = "pages/terms-conditions/terms_conditions.html"


# @require_http_methods(["GET", "POST"])
# @csrf_protect
# def contact_us(request):
#     form = ContactForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             data = form.cleaned_data
#
#             # Sauvegarde en base
#             ContactUsMessage.objects.create(**data)
#
#             # Envoi email
#             context = {
#                 "fname": data["first_name"],
#                 "lname": data["last_name"],
#                 "email": data["email"],
#                 "subject": data["subject"],
#                 "message": data["message"],
#             }
#             subject = f"[{(timezone.now().year + timezone.now().month + timezone.now().day) // 2}] {data['subject']}"
#             msg_txt = get_template("pages/contact-us/email.txt").render(context)
#             msg_html = get_template("pages/contact-us/email.html").render(context)
#
#             email = EmailMultiAlternatives(
#                 subject,
#                 msg_txt,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [data["email"]],
#                 [settings.EMAIL_OPTOLOGIC_RECEIVER],
#             )
#             email.attach_alternative(msg_html, "text/html")
#             email.send()
#
#             # Message de succès
#             messages.success(request, _("Votre message a été envoyé avec succès."))
#
#             if request.htmx:
#                 # Envoi mini-template de succès pour remplacer le formulaire
#                 html = render_to_string(
#                     "pages/contact-us/_success_message.html",
#                     {"first_name": data["first_name"]},
#                 )
#                 response = HttpResponse(html)
#                 response["HX-Trigger"] = json.dumps(
#                     {"refresh-messages": {}, "reset-form": {"form_id": "contact-form"}}
#                 )
#                 response["HX-Reswap"] = "innerHTML"
#                 response["HX-Target"] = "#form-container"
#                 return response
#             return redirect("contact_us")
#
#         else:
#             # Gestion erreur formulaire
#             messages.error(
#                 request, _("Erreur dans le formulaire. Veuillez corriger les champs.")
#             )
#
#             if request.htmx:
#                 html = render_to_string(
#                     "pages/partials/messages.html",
#                     {"messages": messages.get_messages(request)},
#                 )
#                 return HttpResponse(html)
#
#     return render(request, "pages/contact-us/contact_us.html", {"form": form})
#
#
# def messages_initial(request):
#     """Renvoie toutes les toasts en attente pour l’utilisateur (HTMX)."""
#     storage = messages.get_messages(request)  # consomme les messages
#     html = "".join(
#         render_to_string(
#             "pages/partials/_toast.html",
#             {
#                 "message": m,
#                 "level": m.tags or m.level_tag,
#                 "timeout": 5000,
#                 "require_confirm": False,
#                 "oob": False,  # cible déjà #htmx-messages
#             },
#             request,
#         )
#         for m in storage
#     )
#     return HttpResponse(html or "", status=200 if html else 204)
