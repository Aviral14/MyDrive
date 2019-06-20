from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Filedata(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	userfile=models.FileField(upload_to='user_files')
	filename=models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return self.user.username
