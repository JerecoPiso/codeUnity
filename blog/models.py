from django.db import models


# Create your models here.
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/', blank=True)

    def __str__(self):
        return self.username + " " + self.password + " " + self.file.name
	
    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)

class Developers(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	photo = models.FileField(upload_to="media/")
	uname = models.CharField(max_length=255, blank=True)
	skills = models.TextField(blank=True)
	aboutme = models.TextField(blank=True)
	expertise = models.CharField(max_length=255,blank=True)
	resume = models.FileField(upload_to="media/", blank=True)
	rate = models.IntegerField(blank=True)
	countryAbbr = models.CharField(max_length=25, blank=True)
	country = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.email + " " + self.password + " " + self.photo + " " + self.uname + " " + self.skills + " " + self.aboutme + " " + self.expertise  + " " + self.resume + " " + self.rate + " " + self.countryAbbr + " " + self.country

	# def delete(self, *args, **kwargs):
	# 	self.photo.delete()
	# 	super().delete(*args,**kwargs)


class Comments(models.Model):
	commentor = models.IntegerField()
	post_id = models.IntegerField()
	comment = models.TextField(blank=True)
	date = models.CharField(max_length=255)
	answer = models.TextField(blank=True)
	status = models.CharField(blank=True,max_length=255)

	def __str__(self):
		return str(self.commentor) + " " + str(self.post_id) + " " +  self.comment + " " + self.date + " " + self.answer + " " + self.status
	
class Replies(models.Model):
	commentor = models.IntegerField()
	post_id = models.IntegerField()
	comment_id = models.IntegerField()
	reply = models.TextField(blank=False)
	date = models.CharField(max_length=255)
	status = models.CharField(blank=True,max_length=255)

	def __str__(self):
		return self.commentor + " " + self.post_id + " " + self.comment_id + " " + self.reply + " " + self.date + " " + self.status

class Language(models.Model):
	language = models.CharField(max_length=255)
	category = models.CharField(max_length=255)

	def __str__(self):
		return self.language + " " + self.category
		
class Frameworks(models.Model):
	language_id = models.IntegerField(blank=False)
	framework = models.CharField(max_length=255)
	category = models.CharField(max_length=255)

	def __str__(self):
		return self.language_id + " " + self.framework + " " + self.category
		
class Projects(models.Model):
	project_name = models.CharField(max_length=255)
	uploader_id = models.IntegerField()
	downloads = models.IntegerField(blank=True)
	language = models.CharField(max_length=255,blank=True)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	date = models.CharField(max_length=255, blank=True)
	about = models.TextField(blank=True)
	photo = models.FileField(upload_to="media/", blank=True)
	views = models.IntegerField(blank=True)
	more = models.TextField(blank=True)
	resume = models.FileField(upload_to='media/', blank=True)
					
	def __str__(self):
		return self.project_name + " " + self.uploader_id + " " + self.downloads + " " + self.language + " " + self.date + " " + self.about + " " + self.photo + " " + self.views + " " + self.more + " " + self.resume

	def delete(self, *args, **kwargs):
		self.photo.delete()
		super().delete(*args,**kwargs)


class Questions(models.Model):
	question = models.CharField(max_length=255)
	asker_id = models.IntegerField(null=True)
	code = models.TextField(blank=True)
	language = models.CharField(max_length=255)
	# language = models.ForeignKey(Language, on_delete=models.CASCADE)
	date = models.CharField(max_length=255)
	views = models.IntegerField()
	category = models.CharField(max_length=255)
	comments = models.IntegerField()
	status = models.CharField(blank=True,max_length=255)
	tags = models.CharField(blank=True,max_length=255)
	

	def __str__(self):
		return self.question + " " + self.asker_id + " " + self.code + " " + self.language + " " + self.date + " " + self.views + " " + self.category + " " + self.comments + " " + self.status + " " + self.tags

class Users_Device(models.Model):
	device_name = models.CharField(max_length=255)
	total_users = models.IntegerField()

	# def save(self, *args, **kwargs):
	# 	if self.device_name != "Desktop" and  self.device_name != "Laptop" and self.device_name != "Tablet" and self.device_name != "Mobile" and  self.device_name != "laptop" and  self.device_name != "desktop" and  self.device_name != "mobile" and  self.device_name != "tablet":
	# 		return "Not Matched!"
	# 	else:
	# 		super().save(*args, *kwargs)

	def __str__(self):
		return self.device_name

		
class Question_Category(models.Model):
	category = models.CharField(max_length=255)

	def __str__(self):
		return self.category

class Yearly_Visitors(models.Model):
	year = models.IntegerField()
	total_visitors = models.IntegerField()

	def __str__(self):
		return self.year + " " + self.total_visitors

class Notifications(models.Model):
	notification = models.CharField(max_length=255)
	notified_id = models.IntegerField(null=False)
	notification_category = models.TextField(null=True)
	date = models.CharField(null=True,max_length=255)
	status = models.CharField(null=True,max_length=25)

	def __str__(self):
		return self.notification + " " + self.notified_id + " " + self.notification_category +  " " + self.date + " " + self.status


class TempPDF(models.Model):
	pdfname = models.CharField(max_length=255)
	time_uploaded = models.DateTimeField()
	expiraton = models.DateTimeField()

	def __str__(self):
		return self.pdfname + " " + self.time_uploaded + " " + self.expiraton