import re
from django.db import models
from sorl.thumbnail import ImageField
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=False)
    age = models.IntegerField('Idade', blank=True, null=True)
    qnt = models.IntegerField('Quanto(a)s vezes você foi no Conecades:', blank=True, null=True)
    city = models.CharField('Cidade', max_length=50, blank=True)
    email = models.EmailField('E-mail', unique=True)
    about = models.TextField('Do que você mas gosta no conecades', blank=True)
    photo = models.ImageField('Foto', upload_to='fotos', blank=True, null=True)
    is_staff = models.BooleanField('Ativo', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

