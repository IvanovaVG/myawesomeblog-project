from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	date = models.DateField()
	text = models.TextField()
	image = models.ImageField(upload_to='mblog_images/')