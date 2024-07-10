from django.db import models
from stdimagem.models impoert StdImageField

#SIGNALS
from django.db.models impoert signails
from django.template.dafaultfilters import slugify

class Base(models.models):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True