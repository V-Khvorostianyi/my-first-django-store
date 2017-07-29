from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length = 200)
	
	def __str__(self):
		return "user:%s email:%s" % (self.name, self.email)
	
	class Meta:
		verbose_name = "MySubscriber"
		verbose_name_plural = "A lot of Subscribers"
	
	
