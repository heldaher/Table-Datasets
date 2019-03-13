from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.TextField()
	description = models.TextField(default="")
	keywords = models.TextField()
	source = models.TextField()
	dataset = models.FileField()
	data_crop_html = models.TextField()
	data_html = models.TextField()
	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')