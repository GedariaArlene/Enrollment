from django.db import models

#Info ni Student

class Student(models.Model):
#	enroll = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=30, null=True)
	birthday = models.CharField(max_length=30, null=True)
	age = models.CharField(max_length=2, null=True)
	address = models.CharField(max_length=30, null=True)
	gradelevel = models.CharField(max_length=2, null=True)
	lrn = models.CharField(max_length=11, null=True)
	def __str__(self):
		return str(self.name)
		#return self.name 


class Requirements(models.Model):

	require = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	reportcard = models.FileField(default='none', blank=True)
	psa = models.FileField(default='none', blank=True)

	def __str__(self):
		return str(self.reportcard)
		#return self.reportcard


#Students_Specialization
class Specialization(models.Model):

	specialz = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	#ICT #COOKERY #TECHFRAFT #ELECTRICAL
	Option =(
		('ICT', 'ICT'), 
		('COOKERY', 'COOKERY'),
		('TECHFRAFT', 'TECHFRAFT'),
		('ELECTRICAL', 'ELECTRICAL'),)

	specials =models.CharField(max_length=10, choices=Option, default='none')

	def __str__(self):
		return str(self.firstchoice)
		#return self.firstchoice


#Students_Specialization
class Modality(models.Model):

	modals = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)

	Option =(
		('Modular', 'Modular'), 
		('Online', 'Online'),
		('Blended', 'Blended'),)

	modality =models.CharField(max_length=10, choices=Option, default='none')

	def __str__(self):
		return str(self.modality)


#Students_Schedules
class Schedule(models.Model):

	scheds = models.ForeignKey(Student, default=None, on_delete=models.CASCADE, null=True)
	
	name = models.CharField(max_length=30, null=True)
	gradelevel = models.CharField(max_length=30, null=True)
	Option =(('am', 'Morning Shift'), ('pm', 'Afternon Shift'))
	cshifts =models.CharField(max_length=10, choices=Option, default='none')

	def __str__(self):
		return str(self.name)
		#return self.name
