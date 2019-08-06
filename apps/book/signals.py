#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Book
@receiver(post_save, sender=Book)
def add_book(sender, instance, **kwargs):
    print('############ Add a book ##############')
    print(instance)



