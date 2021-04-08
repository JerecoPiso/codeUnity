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
	password = models.CharField(max_length=80)
	# photo = models.FileField(upload_to="media/")
	uname = models.CharField(max_length=255, blank=True)


	def __str__(self):
		return self.email + " " + self.password + " " + self.uname

	# def delete(self, *args, **kwargs):
	# 	self.photo.delete()
	# 	super().delete(*args,**kwargs)

class Jobs(models.Model):
	company_name = models.CharField(max_length=255)
	poster_id = models.IntegerField()
	job_description = models.TextField()
	location = models.TextField()
	skills_needed = models.CharField(max_length=500)
	job_situation = models.CharField(max_length=155)

	def __str__(self):
		return self.company_name + " " + self.poster_id + " " + self.job_description + " " + self.location + " " + self.skills_needed + " " + self.job_situation

class Language(models.Model):
	language = models.CharField(max_length=255)
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.language + " " + self.category

class Projects(models.Model):
	project_name = models.CharField(max_length=255)
	uploader_id = models.IntegerField()
	downloads = models.IntegerField(blank=True)
	language = models.CharField(max_length=100,blank=True)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	about = models.TextField(blank=True)
	photo = models.FileField(upload_to="media/", blank=True)
	views = models.IntegerField(blank=True)

	def __str__(self):
		return self.project_name + " " + self.uploader_id + " " + self.downloads + " " + self.language + " " + self.about + " " + self.photo + " " + self.views

	def delete(self, *args, **kwargs):
		self.photo.delete()
		super().delete(*args,**kwargs)


class Questions(models.Model):
	question = models.CharField(max_length=355)
	asker_id = models.IntegerField(null=True)
	code = models.TextField(blank=True)
	language = models.CharField(max_length=155)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	likes = models.IntegerField()
	category = models.CharField(max_length=255)
	comments = models.IntegerField(null=True)
	

	def __str__(self):
		return self.question + " " + self.asker_id + " " + self.code + " " + self.language + " " + self.likes + " " + self.category + " " + self.comments


class Question_Category(models.Model):
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.category
