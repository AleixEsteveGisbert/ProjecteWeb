from django.contrib import auth
from django.db import models

# Create your models here.
# Class user
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def ads_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/ads/<filename>
    return 'ads/{0}'.format(filename)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True)


# Class Ad
class Ad(models.Model):
    product_name = models.TextField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=ads_directory, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    id_ad_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('ad-show', kwargs={'ad_id': self.id})

    def __str__(self):
        return self.product_name + ' - ' + str(self.price)


# Class Comment
class Comment(models.Model):
    id_comment_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    id_comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

def get_user_ad_count(self):
    return self.ad_set.all().count()

auth.models.User.add_to_class('get_user_ad_count', get_user_ad_count)
