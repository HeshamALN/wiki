from django.db import models
# from pages import views

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=105)
	content = models.CharField(max_length=105)
	last_update = models.DateField(auto_now_add=True)

	def get_absolute_url(self):
		return "detail/%s" % self.id

	def __str__(self):
		return self.title