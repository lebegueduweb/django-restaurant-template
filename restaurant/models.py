# -*- coding: utf-8 -*-

import random
import glob
import os
import shutil
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class MotGerante(models.Model):
    mot = models.TextField()

class Carousel(models.Model):
    diaporama_image = models.ImageField(upload_to='images/')
    diaporama_description = models.TextField()

    def __str__(self):
        return self.diaporama_description

class Service(models.Model):
    nom_service = models.CharField(max_length=300)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return 'Service: {} {}  '.format(self.nom_service, self.service_description)

class Post(models.Model):
    post_image = models.ImageField(upload_to='images/')
    post_titre = models.CharField(max_length=300)
    date_de_publication = models.DateTimeField(auto_now_add=True)
    post_description = models.TextField()

    # function to return the selected object and his title
    def __str__(self):
        return self.title

    # returns the content of body up to 100 characters
    def summary(self):
        return self.body[:100]

    # function to display the date without the publication hour on template
    def pub_date_noHour(self):
        return self.date_de_publication.strftime('%b %e %Y')

