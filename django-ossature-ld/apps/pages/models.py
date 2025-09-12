from django.db import models
from django.core.exceptions import ValidationError

import re


# Create your models here.
regex = r"([a-zA-Z])"


def validate_even(value):
    if not re.search(regex, value):
        value = str(value)
        output = "%s is not a valid entry" % (str(value))
        raise ValidationError(output)


# Create your models here.
class ContactUsMessage(models.Model):
    first_name = models.CharField(max_length=50, validators=[validate_even])
    last_name = models.CharField(max_length=50, validators=[validate_even])
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class FaqQuestionAnswer(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    weight = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.question} {self.weight}"

    class Meta:
        ordering = ["-weight", "question"]

