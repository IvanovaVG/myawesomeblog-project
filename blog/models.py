from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length = 100)
	blog_date = models.DateField()
	blog_text = models.CharField(max_length=300)
	blog_image = models.ImageField(upload_to='mblog_images/')