#!/usr/bin/python

from django.conf import settings
from django.db import models


class CoreModel(models.Model):
    """
    All models inherited from here
    """

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="create_%(app_label)s_%(class)s_related",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="update_%(app_label)s_%(class)s_related",
    )

    class Meta:
        abstract = True
