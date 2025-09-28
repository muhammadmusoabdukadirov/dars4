from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Foydalanuvchi"
    )
    users = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategoriya"
    )
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.users.title if self.users else "Kategoriya yo'q"}"


from django.db import models

class Resume(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100, blank=True, null=True)
    yosh = models.IntegerField()
    tugilgan_sana = models.DateField()
    manzil = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    # Tajriba
    tajriba = models.TextField(help_text="Ish tajribangizni kiriting (markaz, oy, vazifalar)")

    # Loyihalar
    loyihalar = models.TextField(help_text="Loyihalaringiz haqida yozing")

    # Qo‘shimcha maydon
    qoshimcha = models.TextField(blank=True, null=True, help_text="Qo‘shimcha ma’lumot (ixtiyoriy)")

    def __str__(self):
        return f"{self.ism} - {self.email}"
