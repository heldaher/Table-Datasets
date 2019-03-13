from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class TodoItem(models.Model):
# 	content = models.TextField()
#
#
# class SubItem(models.Model):
# 	title = models.TextField()
# 	mainItem = models.ForeignKey(TodoItem, on_delete=models.CASCADE, related_name='tasks')

# need to expand post so that it includes description, csv, (eventually excel and keywords)
class Post(models.Model):
	title = models.TextField()
	description = models.TextField(default="")
	keywords = models.TextField()
	source = models.TextField()
	dataset = models.FileField()
	data_crop_html = models.TextField()
	data_html = models.TextField()
	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')