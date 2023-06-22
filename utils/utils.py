""" Common Utilities

Returns:
    _type_: _description_
"""
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    """
        Generate Token for Registration
    """
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


generate_token = TokenGenerator()
