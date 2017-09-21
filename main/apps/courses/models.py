from __future__ import unicode_literals

from django.db import models


class course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<course object: {} {}>".format(self.name, self.desc)
