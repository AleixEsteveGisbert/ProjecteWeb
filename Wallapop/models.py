from django.db import models


# Create your models here.
# Class user
class User(models.Model):
    username = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    password = models.TextField()
    description = models.TextField(null=True)
    avatar = models.TextField(null=True)


# Class Ad
class Ad(models.Model):
    product_name = models.TextField()
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    id_ad_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name + ' - ' + str(self.price)


# Class Comment
class Comment(models.Model):
    id_comment_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    id_comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
