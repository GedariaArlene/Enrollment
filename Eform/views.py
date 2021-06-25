from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, Requirements, Schedule, Specialization, Modality


# Create your views here.


def EStudent(request):

	if request.method == 'POST':

		Student.objects.create(
			name = request.POST['name'], 
			birthday = request.POST['birthday'],
			age = request.POST['age'], 
			address = request.POST['address'],
			gradelevel = request.POST['gradelevel'],
			lrn = request.POST['lrn'],
			)

		return redirect('students')
		
		abg = Student()
		abg.name = name
		abg.birthday = birthday
		abg.age = age
		abg.address = address
		abg.gradelevel = gradelevel
		abg.lrn = lrn
		abg.requirement = requirement
		abg.save()

	return render(request,'EStudent.html')

def List(request):

	abg = Student.objects.all().order_by('name')
	return render(request,'students.html', {'abg': abg})


def EditList(request, id):
	abg = Student.objects.get(id=id)
	context = {'abg':abg}
	return render(request, 'update.html', context)


def UpdateList(request, id):
	abg = Student.objects.get(id=id)
	abg.name = request.POST['name']
	abg.birthday = request.POST['birthday']
	abg.age = request.POST['age']
	abg.address = request.POST['address']
	abg.gradelevel = request.POST['gradelevel']
	abg.lrn = request.POST['lrn']
	abg.save ()
	return redirect('students')

def DeleteList(request, id):
	abg = Student.objects.get(id=id)
	abg.delete()
	return redirect('students')





def Requirements(request):

	 # Image = Requirements.objects.create(

	 # reportcard = request.POST['reportcard'],
	 # psa = request.POST['psa'],)

	return render(request,'requirement.html')


def Specialization(request):

	# specialz = Specialization.objects.create(

	# specials = request.POST['specialization'],)

	# return redirect('Sched')

	return render(request,'specialization.html')

def Modality(request):
	# modal = Modality.objects.create()
	return render(request,'modality.html')


def Schedule(request):
	# specialz = Specialization.objects.filter()
	return render(request,'schedule.html')


def Done(request):
	return render(request,'Done.html')



