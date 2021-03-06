from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Django', 'Django'),
        ('Python', 'Python'),
        ('C++', 'C++'),
        ('Graphics', 'Graphics'),
        ('TextEditor', 'Text Editor'),
        ('Spreadsheet', 'Spreadsheet'),
        ('DataBase', 'Data Base'),
        ('WebDesign', 'Web Design'),
    )

    LEVEL_CHOICES = (
        ('Unknown', 'Unknown'),
        ('Advanced', 'Advanced'),
        ('Intermediate', 'Intermediate'),
        ('Basic', 'Basic'),
    )

    STATUS_CHOICES = (
        ('Work In Progress', 'Work-In-Progress'),
        ('Not Approved Yet', 'Not-Approved-Yet'),
        ('Approved', 'Approved'),
    )

    title = models.CharField(max_length=50, unique=True)
    synopsis = models.TextField(max_length=500)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    category_abbr = models.CharField(max_length=100, default='')
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default="Unknown")
    content = MDTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    authorized = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Not-Approved-Yet")
    numbers_of_entries = models.IntegerField(default=0)
    ratings = GenericRelation(Rating)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text


class Document(models.Model):
    name = models.CharField(max_length=100, unique=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    postId = models.IntegerField()

    def get_absolute_url(self):
        return reverse('post-upload-detail', kwargs={'pk': self.pk})


class Cycle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, default="Brak opisu")
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title
