from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class ConsecutivelyRepeatingCharacterValidator:
    """
    Rejects passwords that contain the same character repeated consecutively
    for a minimum of `length` times.
    """

    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        for i in range(len(password) - self.length + 1):
            if all(password[i] == password[i + j] for j in range(self.length)):
                raise ValidationError(
                    _(
                        "The password contains characters that are consecutively repeating, "
                        'e.g. "aaa" or "111".'
                    ),
                    code="password_consecutively_repeating",
                )

    def get_help_text(self):
        return _(
            "Your password must not contain consecutively repeating characters "
            '(e.g. "aaa" or "111").'
        )


class ConsecutivelyIncreasingIntegerValidator:
    """
    Rejects passwords that contain strictly increasing sequences of digits
    of a minimum specified `length`.
    """

    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        digits = [int(c) for c in password if c.isdigit()]
        for i in range(len(digits) - self.length + 1):
            if all(
                digits[i + j] + 1 == digits[i + j + 1] for j in range(self.length - 1)
            ):
                raise ValidationError(
                    _(
                        "The password contains consecutively increasing integers, "
                        'e.g. "12345".'
                    ),
                    code="password_consecutively_increasing",
                )

    def get_help_text(self):
        return _(
            "Your password must not contain consecutively increasing integers "
            '(e.g. "12345").'
        )


class ConsecutivelyDecreasingIntegerValidator:
    """
    Rejects passwords that contain strictly decreasing sequences of digits
    of a minimum specified `length`.
    """

    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        digits = [int(c) for c in password if c.isdigit()]
        for i in range(len(digits) - self.length + 1):
            if all(
                digits[i + j] - 1 == digits[i + j + 1] for j in range(self.length - 1)
            ):
                raise ValidationError(
                    _(
                        "The password contains consecutively decreasing integers, "
                        'e.g. "54321".'
                    ),
                    code="password_consecutively_decreasing",
                )

    def get_help_text(self):
        return _(
            "Your password must not contain consecutively decreasing integers "
            '(e.g. "54321").'
        )


class ContextValidator:
    """
    Rejects passwords that contain terms related to a specific context (e.g. company name).
    """

    def __init__(self, context=None):
        self.context = context or ["context_word_to_reject"]

    def validate(self, password, user=None):
        for word in self.context:
            if word.lower() in password.lower():
                raise ValidationError(
                    _("The password contains a variation of the company name."),
                    code="password_context_word",
                )

    def get_help_text(self):
        return _(
            "Your password must not contain a variation of the company name or related terms."
        )
