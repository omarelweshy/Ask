from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question = models.CharField(_("Question"), max_length=300)

    def __str__(self):
        return self.name
