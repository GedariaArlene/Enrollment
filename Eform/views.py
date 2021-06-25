from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, Requirements, Schedule, Specialization


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


def Schedule(request):
	# specialz = Specialization.objects.filter()
	return render(request,'schedule.html')


def Done(request):
	return render(request,'Done.html')

'''

def edit(request, id):  
    myfrm = Student.objects.get(id=id)  
    return render(request,'students.html', {'myfrm':myfrm})  

def update(request, id):  
    myfrm = Student.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = myfrm)  
    if form.is_valid():  
        form.save()  
        return redirect("/students")  
    return render(request, 'students.html', {'myfrm': myfrm}) 

def destroy(request, id):  
    myfrm = Student.objects.get(id=id)  
    myfrm.delete()  
    return redirect("/students")  '''



