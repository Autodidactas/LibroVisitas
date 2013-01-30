from django.db import models

class Comentario(models.Model):
	autor = models.CharField(max_length=150)
	comentario = models.TextField()

	def __unicode__(self):
		return self.autor