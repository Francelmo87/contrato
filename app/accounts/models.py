from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    cpf = models.CharField('CPF', max_length=14, unique=True, blank=True, null=True)
    registration = models.CharField('Matrícula', max_length=20,  blank=True, null=True)
    phone = models.CharField('Contato', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
  