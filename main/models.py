import base64
import datetime
import os
import re
from io import BytesIO

from django.core.files.base import ContentFile
from django.db import models

from emmre.settings import BASE_DIR


class PricePlan(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    button = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=25, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.title}, color {self.color}"


class FAQ(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    # img = models.ForeignKey(Image, related_name='faq', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Question -- {self.question}'


