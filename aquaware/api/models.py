from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Profile(models.Model):

    CLIENT_NUMBER_MAX_LENGTH = 6
    PHONE_NUMBER_MAX_LENGTH = 10

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile',
                                blank=True,
                                null=True)

    first_name = models.CharField(max_length=30,
                                  blank=True,
                                  null=True)

    last_name = models.CharField(max_length=30,
                                 blank=True,
                                 null=True)

    email = models.EmailField(blank=True,
                              null=True)

    client_number = models.PositiveIntegerField(validators=[MaxValueValidator(10 ** CLIENT_NUMBER_MAX_LENGTH - 1)],
                                                blank=True,
                                                null=True)

    phone_number = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH,
                                    blank=True,
                                    null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username if self.user else "Profile"



