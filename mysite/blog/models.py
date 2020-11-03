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
	uname = models.CharField(max_length=255, blank=True)


	def __str__(self):
		return self.email + " " + self.password + " " + self.photo + " " + self.uname

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args,**kwargs)

class Projects(models.Model):
	project_name = models.CharField(max_length=255)
	uploader_id = models.IntegerField()
	downloads = models.IntegerField(blank=True)
	language = models.CharField(max_length=100,blank=True)
	about = models.TextField(blank=True)

	def __str__(self):
		return self.project_name + " " + self.uploader_id + " " + self.downloads + " " + self.language + " " + self.category + " " + self.about

class Questions(models.Model):
	question = models.CharField(max_length=355)
	asker_id = models.IntegerField(null=True)
	code = models.TextField(blank=True)
	language = models.CharField(max_length=155)
	likes = models.IntegerField()
	category = models.CharField(max_length=255)

	def __str__(self):
		return self.question + " " + self.code + " " + self.language + " " + self.likes + " " + self.category
		