from django.db import models
from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.
GENDER_CHOICES = (
    (0, 'not specified'),
    (1, 'male'),
    (2, 'female'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        # img = Image.open(self.image.path)

        # if img.height > 512 or img.width > 512:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
