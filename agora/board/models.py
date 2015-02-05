from django.db import models

# Create your models here.

class Post(models.Model):
	text = models.CharField(max_length=300)
	time = models.DateField(null=True)
	tag = models.CharField(max_length=20)
	score = models.IntegerField(null=True)
	comments = models.ForeignKey('Post', null=True)
	
class User(models.Model):
	name = models.CharField(max_length=25)
	birthday = models.DateField()
	score = models.SmallIntegerField()
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	posts = models.ForeignKey('Post')