from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from . import utils


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    votes = models.IntegerField(default=1)
    host = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def html(self):
        return utils.markdown(self.content)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    content = models.TextField(max_length=9001)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    post = models.ForeignKey(Post)
    votes = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['-votes']

    def __str__(self):
        return "Comment " + str(self.id)
