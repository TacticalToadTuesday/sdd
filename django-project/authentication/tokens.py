from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp)  # Concatenate the user's primary key and timestamp as the hash value
        )

generate_token = TokenGenerator()  # Create an instance of the TokenGenerator class for generating tokens
