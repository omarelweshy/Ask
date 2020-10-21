from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse

GENDER_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female')]


class User(AbstractUser):
    first_name = models.CharField(_("First Name"), max_length=20)
    last_name = models.CharField(_("Last Name"), max_length=20)
    location = models.CharField(
        _("Location"), max_length=50, blank=True, editable=True)
    bio = models.TextField(_("Bio"), blank=True, editable=True, max_length=150)
    url = models.URLField(_("URL"), max_length=200, blank=True, editable=True)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    photo = models.ImageField(_("Image"), upload_to="profile_images",
                              max_length=None, default='profile_images/default.jpg', blank=True)
    gender = models.CharField(
        _("Gender"), max_length=50, choices=GENDER_CHOICES)
    # online = models.BooleanField(_("Online"), )

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.slug)])

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
