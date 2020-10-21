from django.db import models


# Create your models here.
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.username + " " + self.password + " " + self.file.name

    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)

class Developers(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=40)
	photo = models.FileField(upload_to="media/")


	def __str__(self):
		return self.email + " " + self.password + " " + self.photo.name

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args,**kwargs)