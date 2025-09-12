from django.forms import ModelForm

from .models import ContactUsMessage

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class BaseModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("auto_id", "%s")
        kwargs.setdefault("label_suffix", "")
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({"placeholder": field.help_text})

    def clean(self):
        return self.cleaned_data


class ContactForm(BaseModelForm):

    # captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = ContactUsMessage
        fields = (
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
        )  # 'captcha'
