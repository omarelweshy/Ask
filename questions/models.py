import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from author.decorators import with_author


@with_author
class Question(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    question = models.CharField(_("Question"), max_length=300)
    date = models.DateTimeField(_("Time"), auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.question


@with_author
class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name=_(
        "Answer"), on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer
