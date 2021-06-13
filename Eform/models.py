from django.db import models

#Info ni Student

class Student(models.Model):
#	enroll = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=30, null=True)
	gradelevel = models.IntegerField(max_length=30, null=True)
	lrn = models.IntegerField(max_length=11, null=True)
	address = models.CharField(max_length=30, null=True)
	birthday = models.IntegerField(max_length=30, null=True)

	def __str__(self):
		return str(self.name)
		#return self.name 

#Info ni Teacher	
class Teacher(models.Model):
#	teacher = models.ForeignKey(Teacher, default=None, on_delete=models.CASCADE, null=True)

	name = models.CharField(max_length=30, null=True)
	faculty = models.CharField(max_length=11, null=True)
	yearlevel = models.CharField(max_length=30, null=True)
	section = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.name)
		#return self.name

class Requirements(models.Model):

	require = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	reportcard = models.FileField(default="")
	psa = models.FileField(default="")

	def __str__(self):
		return str(self.reportcard)
		#return self.reportcard

class ClassShift(models.Model):

	classshift = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	Option =(('am', 'Morning Shift'), ('pm', 'Afternon Shift'))
	cshifts =models.CharField(max_length=10, choices=Option, default='none')

	def __str__(self):
		return str(self.cshifts)
		#return self.cshifts


#Students_Schedules
class Schedule(models.Model):

	scheds = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)
	
	name = models.CharField(max_length=30, null=True)
	gradelevel = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.name)
		#return self.name


#Students_Specialization
class Specialization(models.Model):

	specialz = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	#ICT #COOKERY #TECHFRAFT #ELECTRICAL

	firstchoice = models.CharField(max_length=30, null=True)
	secondchoice = models.CharField(max_length=30, null=True)


	def __str__(self):
		return str(self.firstchoice)
		#return self.firstchoice


class StudentProfile(models.Model):

	profile = models.ForeignKey(Teacher, default=None, on_delete=models.CASCADE, null=True)
	
	name = models.CharField(max_length=30, null=True)
	age = models.CharField(max_length=11, null=True)
	birthday = models.CharField(max_length=30, null=True)
	address = models.CharField(max_length=30, null=True)
	mothersname = models.CharField(max_length=30, null=True)
	Occupation1 = models.CharField(max_length=30, null=True)
	fathersname = models.CharField(max_length=30, null=True)
	occupation2 = models.CharField(max_length=30, null=True)
	mothersname = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.name)
		#return self.name




#	Teacher=models.ManyToManyField(Teacher)'''

'''
#View_Section_of_Students_MasterList
class Sections(models.Model):

	scheds = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	#
	name = models.CharField(max_length=30, null=True)

	gradelevel = models.CharField(max_length=30, null=True)
	#gradelevel

	def __str__(self):
		return self.name


	class TeacherUser(models.Model):
	teacher1 = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.teacher1


class StudentUser(models.Model):
	student1 = models.CharField(max_length=20, null=True)


	def __str__(self):
		return self.student1'''






'''
class User(models.Model):
	pass

class Item(models.Model):

	enroll = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	#Gradelevel
	gradelevel = models.CharField(max_length=30, null=True)
	#LRN
	lrn = models.CharField(max_length=11, null=True)
	#NAME1
	name = models.CharField(max_length=30, null=True)
	#ADDRESS
	address = models.CharField(max_length=30, null=True)
	#Birthday
	birthday = models.CharField(max_length=30, null=True)


	def __str__(self):
		return self.gradelevel'''