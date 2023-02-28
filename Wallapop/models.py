from django.db import models


# Create your models here.
# Class user
from django.urls import reverse
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    avatar = models.FileField(upload_to=user_directory_path)




# Class Ad
class Ad(models.Model):
    product_name = models.TextField()
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    id_ad_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ad-details', kwargs={'adid':self.id})

    def __str__(self):
        return self.product_name + ' - ' + str(self.price)


# Class Comment
class Comment(models.Model):
    id_comment_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    id_comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
