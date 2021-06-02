from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from Eform.views import Omepage
from django.urls import resolve
#For Models testing
from .models import Item, User

class OmeTest(TestCase):

	def html_Omepage(self):
		found = resolve('/')
		self.assertEqual(found.func, Omepage)

		
	def test_Omepage_returns_correct_view(self):
		request = HttpRequest()
		response = Omepage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Omepage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'Omepage.html')

		self.assertIn('<html>', html)
		self.assertIn('<head>', html)

		self.assertIn('<title>Enrollment Form</title>', html)
		self.assertIn('</head>', html)
		self.assertIn('<body bgcolor= "lightblue">', html)

		self.assertTemplateUsed(response, 'Omepage.html')
#unittest ng Omepage ko
		self.assertIn('<center>', html)
		self.assertIn('<form class="gedaria"action="#" method="post">', html)
		self.assertIn('<h1 style="color:blue; font-size:35px;"> <center>Enrollment Form</center> </h1>', html)
		self.assertIn('<hr>', html)
		self.assertIn('<br>', html)
		self.assertIn('<b><label for="Grade_Level" id="glabel1">Grade Level:</label><b>', html)
		self.assertIn('<input bold type="text" id="gradelevel" name="gradelevel" placeholder= "Grade Level">', html)
		self.assertIn('<label for="Name" id="glabel2">Name:</label>', html)
		self.assertIn('<input bold type="text" id="name" name="name" placeholder= "Name (SN, FN, M)">', html)
		self.assertIn('<b><label for="LRN" id="glabel3">LRN:</label><b>', html)
		self.assertIn('<input bold type="text" id="lrn" name="lrn" placeholder= "Learner Reference Number">', html)
		self.assertIn('<label for="Birthday" id="glabel4">Birthday:</label>', html)
		self.assertIn('<input bold type="text" id="birthday" name="birthday" placeholder= "Birthday (M/D/Y)">', html)
		self.assertIn('<label for="Address" id="glabel5">Address:</label>', html)
		self.assertIn('<input bold type="text" id="address" name="address" placeholder="Address"></left><br><br><br>', html)
		self.assertIn('<input type="submit" name="enroll" onclick="myFunction()" value="Enroll"style="color:red;">', html)
		self.assertIn('<script>function myFunction() {alert("Enrolled Successfully!");}', html)
		self.assertIn('</script>', html)
		self.assertIn('<center>', html)
		self.assertIn('<table id="idListTable">', html)
		self.assertIn('</form>', html)
		self.assertIn('</center>', html)
		self.assertIn('</body>', html)


		self.assertTrue(html.strip().endswith('</html>'))
		self.assertTrue(html.strip().endswith('</html>'))


#unittest ng inputs ko
class ABG1(TestCase):
	def test_input(self):
		Item1 = Item()
		Item1.gradelevel = 'Grade 10'
		Item1.save()
		Item2 = Item()
		Item2.name = 'Gedaria, Arlene B.'
		Item2.save()
		Item3 = Item()
		Item3.lrn = '191817152512'
		Item3.save()
		Item4 = Item()
		Item4.address = 'Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite'
		Item4.save()
		Item5 = Item()
		Item5.birthday = '3/31/99'
		Item5.save()

		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]

		self.assertEqual(Item1.gradelevel, 'Grade 10')
		self.assertEqual(Item2.name, 'Gedaria, Arlene B.')
		self.assertEqual(Item3.lrn, '191817152512')
		self.assertEqual(Item4.address, 'Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite')
		self.assertEqual(Item5.birthday, '3/31/99')


#unittest ng inputs ko
class ABG2(TestCase):
	def test_input(self):
		Item1 = Item()
		Item1.gradelevel = 'Grade 10'
		Item1.save()
		Item2 = Item()
		Item2.name = 'Gedaria, Arlene B.'
		Item2.save()
		Item3 = Item()
		Item3.lrn = '191817152512'
		Item3.save()
		Item4 = Item()
		Item4.address = 'Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite'
		Item4.save()
		Item5 = Item()
		Item5.birthday = '3/31/99'
		Item5.save()

		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]

		self.assertEqual(Item1.gradelevel, 'Grade 10')
		self.assertEqual(Item2.name, 'Gedaria, Arlene B.')
		self.assertEqual(Item3.lrn, '191817152512')
		self.assertEqual(Item4.address, 'Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite')
		self.assertEqual(Item5.birthday, '3/31/99')


class ABG3(TestCase):
	def test_input(self):
		Item.objects.create( gradelevel='gradelevel', name='name',lrn='lrn', address='address', birthday='birthday')
		response = self.client.get('/app/views.Omepage.html/')


#BAGONGTESSSSTTTTTT



class ListViewTest(TestCase):

	def test_uses_list_template(self):
		enroll = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Omepage.html')

	def test_uses_home_template(self):
		response = self.client.get('/students/')
		#self.assertTemplateUsed(response,'students.html')

	def test_displays_all_list_items(self):
		enroll = User.objects.create()

		gradelevel = Item.objects.create(gradelevel='Grade 10')
		lrn = Item.objects.create(lrn='191817152512')
		name = Item.objects.create(name='Gedaria, Arlene B.')
		address = Item.objects.create(address='Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite')
		birthday = Item.objects.create(birthday='3/31/99')
		
		response = self.client.get('/')
		self.assertIn('gradelevel', response.content.decode())
		self.assertIn('lrn', response.content.decode())
		self.assertIn('name', response.content.decode())
		self.assertIn('address', response.content.decode())
		self.assertIn('birthday', response.content.decode())
	
		gradelevel = Item.objects.get(gradelevel="Grade 10")
		lrn = Item.objects.get(lrn="191817152512")
		name = Item.objects.get(name="Gedaria, Arlene B.")
		address = Item.objects.get(address="Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite")
		birthday = Item.objects.get(birthday="3/31/99")

		self.assertEqual(Item.objects.count(), 5)

		
class Views(TestCase):
	def setUp(self):
		gradelevel = Item.objects.create()
		lrn = Item.objects.create()
		name = Item.objects.create()
		address = Item.objects.create()
		birthday = Item.objects.create()
		
		
		Item.objects.create(
			gradelevel = 'Grade 10',
			lrn = '191817152512',
			name = 'Gedaria, Arlene B.',
			address = 'Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite',
			birthday = '3/31/99',
			)
		self.client.post('/students/', name='Gedaria, Arlene B.')
		

		self.client.post('/students/')

		self.assertEqual(Item.objects.count(), 6)


	def test_redirect_view(self):
		gradelevel = Item.objects.get(gradelevel="Grade 10")
		lrn = Item.objects.get(lrn="191817152512")
		name = Item.objects.get(name="Gedaria, Arlene B.")
		address = Item.objects.get(address="Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite")
		birthday = Item.objects.get(birthday="3/31/99")
		

		response = self.client.post('/students/')



class URL(TestCase):

	def urls(self):
		found = resolve()
		self.assertEqual(found.func, Omepage)
		self.assertEqual(found.func, leng)

		url = reverse('Omepage')
		self.assertEqual(resolve(url).func, Omepage)

		url = reverse('students')
		self.assertEqual(resolve(url).func, leng)



class Models(TestCase):

	def models(self, 
		enroll="test1", 
		gradelevel="test2", 
		lrn="test3", 
		name="test4", 
		address="test5", 
		birthday="test6"): 
		
		
		return User.objects.create()
		return Item.objects.create(
			enroll="enroll", 
			gradelevel="gradelevel", 
			lrn="lrn", 
			name="name", 
			address="address", 
			birthday="birthday", )

	def test_whatever_creation(self):
		leng = self.models()
		self.assertTrue(isinstance(leng, User))
		self.assertFalse(isinstance(leng, Item))













