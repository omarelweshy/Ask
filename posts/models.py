from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import auth
from author.decorators import with_author

# Image DIR path at Media
def user_directory_path(instance, image):
    return 'posts_image/{0} {1}/{2}'.format(instance.user.first_name, instance.user.last_name, image)

@with_author
class Post(models.Model):
    # user = models.ForeignKey(auth.get_user_model, verbose_name=_("user"), on_delete=models.CASCADE)
    context = models.CharField(_("context"), max_length=1024, blank=True)
    image = models.ImageField(_("image"), upload_to=user_directory_path, height_field=None, width_field=None, blank=True)

    def __str__(self):
        return self.context
    
    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.pk)])

    # Check at least one field is not null
    def clean(self):
        if not (self.context or self.image):
            raise ValidationError("You must specify either context or image")