from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')
        if password is None:
            raise TypeError('Users must set a password.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_student = False
        user.is_sponsor = False
        user.save()
        return user

    def create_student_user(self, username, email, password):
        return self.create_user(username, email, password)

    def create_sponsor_user(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = False
        user.is_staff = False
        user.is_sponsor = True
        return user
