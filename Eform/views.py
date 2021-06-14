from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, Teacher, Requirements, ClassShift, Schedule, Specialization, StudentProfile
# Create your views here.


def EStudent(request):

	if request.method == 'POST':

		enroll = Student.objects.create()
		Student.objects.create(
			name = request.POST['name'], 
			gradelevel = request.POST['gradelevel'],
			lrn = request.POST['lrn'],
			birthday = request.POST['birthday'], 
			address = request.POST['address'],
			)

		return redirect('students')
		
		abg = Student()
		abg.name = name
		abg.gradelevel = gradelevel
		abg.lrn = lrn
		abg.birthday = birthday
		abg.address = address
		abg.requirement = requirement
		abg.save()

	return render(request,'EStudent.html')

def Page(request):

	abg = Student.objects.all().order_by('name')
	return render(request,'students.html', {'abg': abg})






def Requirements(request):

	if request.method == 'POST':

		require = Requirements.objects.create()
		Requirements.objects.create(
			reportcard = request.POST['reportcard'], 
			psa = request.POST['psa'],
			)

		return redirect('shifts.html')

		abg = Requirements()
		abg.reportcard = reportcard
		abg.psa = psa
		abg.save()

	return render(request,'students.html')

def Page(request):

	abg = Requirements.objects.all().order_by('reportcard')
	return render(request,'shifts.html', {'abg': abg})




def ClassShift(request):

	if request.method == 'POST':

		classshift = ClassShift.objects.create()
		ClassShift.objects.create(
			cshifts = request.POST['cshifts'], 
			)

		return redirect('schedule.html')

		abg = ClassShift()
		abg.cshifts = cshifts
		abg.save()
		
	return render(request,'schedule.html')

def Page(request):

	abg = ClassShift.objects.all().order_by('cshifts')
	return render(request,'schedule.html', {'abg': abg})












	
'''
def Page(request):
	#return render(request,'students.html')

	#return render(request,'students.html', {'abg': abg})

	abg = Item.objects.all().order_by('gradelevel')
	return render(request,'students.html', {'abg': abg})






def EStudent(request):

	if request.method == 'POST':

		enroll = Student.objects.create()
		Student.objects.create(
			name = request.POST['name'], 
			gradelevel = request.POST['gradelevel'],
			lrn = request.POST['lrn'],
			birthday = request.POST['birthday'], 
			address = request.POST['address'],
			)

		return redirect('students')

def Fourth(request):

	officerId=officer.objects.create(
		firstname = request.POST['name'],
		middle = request.POST['middle'],
	)
	return render(request,'.html')


def Fifth(request):

	resortId=Resort.objects.create(
		resort = request.POST['resort'])

	admitId=Admission.objects.create(
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		)

	cottageId=Cottage.objects.create(
		cottage = request.POST['cottage'])

	return render(request,'receipt.html')'''





















'''
def Student(request):


	if request.method == 'POST':
		return render(request,'Student.html')		

		student = Student.objects.create()
		StudentUser.objects.create(
			gradelevel = request.POST['gradelevel'],
			name = request.POST['name'], 
			lrn = request.POST['lrn'],
			birthday = request.POST['birthday'], 
			address = request.POST['address'],
			)
		
		return redirect('studentlist')
			
		vax = Student()
		vax.gradelevel = gradelevel
		vax.name = name
		vax.lrn = lrn
		vax.birthday = birthday
		vax.address = address
		vax.save()

		return render(request,'Student')

def Page(request):
	#return render(request,'students.html')

	#return render(request,'students.html', {'abg': abg})

	vax = StudentUser.objects.all().order_by('gradelevel')
	return render(request,'studentlist.html', {'vax': vax})'''



'''
	if request.method == 'POST':

		enroll = User.objects.create()
		Item.objects.create(
			gradelevel = request.POST['gradelevel'],
			name = request.POST['name'], 
			lrn = request.POST['lrn'],
			birthday = request.POST['birthday'], 
			address = request.POST['address'],
			)
		return redirect('students')'''
		


'''
#bagooooooooo
def Requirement(request):

	if request.method == 'POST':

		require = Requirement.objects.create()
		Item.objects.create(
			reportcard = request.POST['reportcard'],
			psa = request.POST['psa'], 
			)
		return redirect('requirement')
		

		abg = Item()
		abg.reportcard = reportcard
		abg.psa = psa
		abg.save()

	return render(request,'students.html')'''











'''
from django.shortcuts import redirect, render
from .models import Item, User

# Create your views here.
def Omepage(request):

	if request.method == 'POST':

		enroll = User.objects.create()
		Item.objects.create(
			gradelevel = request.POST['gradelevel'],
			name = request.POST['name'], 
			lrn = request.POST['lrn'],
			birthday = request.POST['birthday'], 
			address = request.POST['address'],
			)
		return redirect('students')
		

		abg = Item()
		abg.gradelevel = gradelevel
		abg.name = name
		abg.lrn = lrn
		abg.birthday = birthday
		abg.address = address
		abg.save()

	return render(request,'Omepage.html')

def Page(request):
	#return render(request,'students.html')

	#return render(request,'students.html', {'abg': abg})

	abg = Item.objects.all().order_by('gradelevel')
	return render(request,'students.html', {'abg': abg})'''



