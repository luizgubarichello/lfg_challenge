from django.db import models
from django.contrib.auth.models import User


class ProposalField(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=[('text', 'Texto'), ('number', 'Número'), ('date', 'Data')])
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class ProposalFieldValue(models.Model):
    field = models.ForeignKey(ProposalField, on_delete=models.CASCADE) 
    value = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.field.label}: {self.value}'


class Proposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('approved', 'Aprovada'),
        ('denied', 'Negada'),
        ('human', 'Humana'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    fields = models.ManyToManyField(ProposalFieldValue) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Proposta #{self.id}'
