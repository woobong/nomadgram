from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models


@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Image(TimeStampedModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    captions = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{} - {}'.format(self.location, self.captions)


@python_2_unicode_compatible
class Comment(TimeStampedModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{} - Image Caption: {}'.format(self.creator.username, self.image.captions)
