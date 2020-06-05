from django.db import models
from django.utils import timezone
from django_cryptography.fields import encrypt


class User(models.Model):
    username = models.CharField(max_length=70)
    firstName = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 25)
    email = models.CharField(max_length = 70)
    phone = models.CharField(max_length = 15, blank=True, null=True, default=None)
    img = models.ImageField(upload_to='images/user/', default='images/user/no_photo.jpg')
    password = encrypt(models.CharField(max_length = 25))
    position = models.CharField(max_length=10, default="user")
    blocked = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    dateRegistr = models.DateTimeField(default=timezone.now)
    lastAttended = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Publications(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User_ID")

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    publications = models.ForeignKey(Publications, on_delete=models.CASCADE, verbose_name="Publication_id")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User_id")

    def __str__(self):
        return self.text


class Articles(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    hide = models.BooleanField(default=False)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User_ID")

    def __str__(self):
        return self.title


class Photos(models.Model):
    img = models.CharField(max_length=255)
    hide = models.BooleanField(default=False)
    date = models.DateTimeField()
    general = models.BooleanField(default=False)
    publications = models.ForeignKey(Publications, on_delete=models.SET_NULL,blank=True, null=True, verbose_name="publication_id")
    articles = models.ForeignKey(Articles, on_delete=models.SET_NULL,blank=True, null=True, verbose_name="article_id")

    def __str__(self):
        return self.img


class Timetable(models.Model):
    description = models.TextField()
    address = models.CharField(max_length=255)
    date = models.DateTimeField()
    addedDate = models.DateTimeField()

    def __str__(self):
        return self.description