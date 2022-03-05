from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


def my_year_validator(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


