import pytest
from django.core.exceptions import ValidationError

from apps.accounts.validators import (
    ConsecutivelyRepeatingCharacterValidator,
    ConsecutivelyIncreasingIntegerValidator,
    ConsecutivelyDecreasingIntegerValidator,
    ContextValidator,
)


@pytest.mark.parametrize("password", ["aaa", "111", "xxxyyy", "zzzz"])
def test_repeating_characters_invalid(password):
    validator = ConsecutivelyRepeatingCharacterValidator(length=3)
    with pytest.raises(ValidationError):
        validator.validate(password)


@pytest.mark.parametrize("password", ["abc", "xyz", "test", "hello123"])
def test_repeating_characters_valid(password):
    validator = ConsecutivelyRepeatingCharacterValidator(length=3)
    # Should not raise
    validator.validate(password)


@pytest.mark.parametrize("password", ["123", "0123", "a123b", "xx456yy"])
def test_increasing_sequence_invalid(password):
    validator = ConsecutivelyIncreasingIntegerValidator(length=3)
    with pytest.raises(ValidationError):
        validator.validate(password)


@pytest.mark.parametrize("password", ["159", "a1b3", "8888"])
def test_increasing_sequence_valid(password):
    validator = ConsecutivelyIncreasingIntegerValidator(length=3)
    validator.validate(password)


@pytest.mark.parametrize("password", ["987", "a765z", "543", "x321y"])
def test_decreasing_sequence_invalid(password):
    validator = ConsecutivelyDecreasingIntegerValidator(length=3)
    with pytest.raises(ValidationError):
        validator.validate(password)


@pytest.mark.parametrize("password", ["123", "515", "070", "9a7b5"])
def test_decreasing_sequence_valid(password):
    validator = ConsecutivelyDecreasingIntegerValidator(length=3)
    validator.validate(password)


@pytest.mark.parametrize(
    "password, context_word",
    [
        ("opto2025", "opto"),
        ("mylogicisgood", "logic"),
        ("companyname123", "company"),
    ],
)
def test_context_word_invalid(password, context_word):
    validator = ContextValidator(context=[context_word])
    with pytest.raises(ValidationError):
        validator.validate(password)


def test_context_word_valid():
    validator = ContextValidator(context=["Opto", "Logic"])
    validator.validate("thisisasecurepassword123")
