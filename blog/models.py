from django.db import models


# Create your models here.
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/', blank=True)

    def __str__(self):
        return self.username + " " + self.password + " " + self.file.name
	
    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)

class Developers(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=255)
	photo = models.FileField(upload_to="media/")
	uname = models.CharField(max_length=255, blank=True)


	def __str__(self):
		return self.email + " " + self.password + " " + self.photo + " " + self.uname

	def delete(self, *args, **kwargs):
		self.photo.delete()
		super().delete(*args,**kwargs)


class Comments(models.Model):
	commentor = models.IntegerField()
	post_id = models.IntegerField()
	comment = models.TextField(blank=True)
	date = models.CharField(max_length=50)
	answer = models.TextField(blank=True)

	def __str__(self):
		return str(self.commentor) + " " + str(self.post_id) + " " +  self.comment + " " + self.date + " " + self.answer

class Replies(models.Model):
	commentor = models.IntegerField()
	post_id = models.IntegerField()
	comment_id = models.IntegerField()
	reply = models.TextField(blank=False)

	def __str__(self):
		return self.commentor + " " + self.post_id + " " + self.comment_id + " " + self.reply

class Language(models.Model):
	language = models.CharField(max_length=255)
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.language + " " + self.category
class Frameworks(models.Model):
	language_id = models.IntegerField(blank=False)
	framework = models.CharField(max_length=255)

	def __str__(self):
		return self.language_id + " " + self.framework
		
class Projects(models.Model):
	project_name = models.CharField(max_length=255)
	uploader_id = models.IntegerField()
	downloads = models.IntegerField(blank=True)
	language = models.CharField(max_length=100,blank=True)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	about = models.TextField(blank=True)
	photo = models.FileField(upload_to="media/", blank=True)
	views = models.IntegerField(blank=True)
	more = models.TextField(blank=True)

	def __str__(self):
		return self.project_name + " " + self.uploader_id + " " + self.downloads + " " + self.language + " " + self.about + " " + self.photo + " " + self.views + " " + self.more

	def delete(self, *args, **kwargs):
		self.photo.delete()
		super().delete(*args,**kwargs)


class Questions(models.Model):
	question = models.CharField(max_length=355)
	asker_id = models.IntegerField(null=True)
	code = models.TextField(blank=True)
	language = models.CharField(max_length=155)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	date = models.CharField(max_length=50)
	likes = models.IntegerField()
	category = models.CharField(max_length=255)
	comments = models.IntegerField()
	

	def __str__(self):
		return self.question + " " + self.asker_id + " " + self.code + " " + self.language + " " + self.date + " " + self.likes + " " + self.category + " " + self.comments

class QuestionTags(models.Model):
	question_id = models.IntegerField()
	tag = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.question_id + " " + self.tag
		
class Question_Category(models.Model):
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.category
