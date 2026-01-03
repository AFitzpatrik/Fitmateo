from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    age = models.PositiveIntegerField()
    city = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sports = models.ManyToManyField(
        "Sport",
        blank=True
    )

    def __str__(self):
        return f"Profile of {self.user.email}"
        '''

#NÁVRH DODĚLAT POZDĚJI