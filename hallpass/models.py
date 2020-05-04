from django.db import models

class EncryptedData(models.Model):
	data = models.TextField(default='')
	public_key = models.CharField(max_length=100)
