# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=50)
    mensagem = models.TextField('Descrição', blank=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['name']

    def __unicode__(self):
        return self.n
