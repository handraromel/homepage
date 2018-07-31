from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.


class Bio(models.Model):
    title = models.CharField(max_length=250)
    story_text = HTMLField('Story Text')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        User, related_name='bio_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=250)
    education_years = models.CharField(max_length=250, default='2018')
    education_text = HTMLField('Education Text')
    image = models.ImageField(
        upload_to='media/uploads', default='media/uploads/no-img.jpg')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        User, related_name='education_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=250)
    work_year = models.CharField(max_length=250, default='null')
    work_text = HTMLField('Work Text')
    image = models.ImageField(
        upload_to='media/uploads', default='media/uploads/no-img.jpg')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        User, related_name='work_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    project_text = HTMLField('Project Text')
    frontend_dev = models.CharField(max_length=250, default='')
    backend_dev = models.CharField(max_length=250, default='')
    image = models.ImageField(
        upload_to='media/uploads', default='media/uploads/no-img.jpg')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        User, related_name='project_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title