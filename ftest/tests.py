from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()


	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Enrollment Form', self.browser.title)

		Head = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Enrollment Form', Head)

		form = self.browser.find_element_by_tag_name('form')

		label1 = self.browser.find_element_by_id('glabel1').text
		self.assertIn('Grade Level:', label1)

		label2 = self.browser.find_element_by_id('glabel2').text
		self.assertIn('Name:', label2)

		label3 = self.browser.find_element_by_id('glabel3').text
		self.assertIn('LRN:', label3)

		label4 = self.browser.find_element_by_id('glabel4').text
		self.assertIn('Birthday:', label4)

		label5 = self.browser.find_element_by_id('glabel5').text
		self.assertIn('Address:', label5)

		input1 = self.browser.find_element_by_id('gradelevel')  
		self.assertEqual(input1.get_attribute('placeholder'),'Grade Level')
		input1 = self.browser.find_element_by_id('gradelevel').send_keys("Grade 10")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('name')  
		self.assertEqual(input2.get_attribute('placeholder'),'Name (SN, FN, M)')
		input2 = self.browser.find_element_by_id('name').send_keys("Gedaria, Arlene B.")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('lrn')  
		self.assertEqual(input3.get_attribute('placeholder'),'Learner Reference Number')
		input3 = self.browser.find_element_by_id('lrn').send_keys("191817152512")
		time.sleep(1)

		input4 = self.browser.find_element_by_id('birthday')  
		self.assertEqual(input4.get_attribute('placeholder'),'Birthday (M/D/Y)')
		input4 = self.browser.find_element_by_id('birthday').send_keys("3/31/99")
		time.sleep(1)

		input5 = self.browser.find_element_by_id('address')  
		self.assertEqual(input5.get_attribute('placeholder'),'Address')
		input5 = self.browser.find_element_by_id('address').send_keys("Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('enroll').click()
		time.sleep(2)

		self.browser.quit()

	def test_browser_bardugalan(self):
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)


		input1 = self.browser.find_element_by_id('gradelevel')  
		self.assertEqual(input1.get_attribute('placeholder'),'Grade Level')
		input1 = self.browser.find_element_by_id('gradelevel').send_keys("Grade 10")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('name')  
		self.assertEqual(input2.get_attribute('placeholder'),'Name (SN, FN, M)')
		input2 = self.browser.find_element_by_id('name').send_keys("Gedaria, Arlene B.")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('lrn')  
		self.assertEqual(input3.get_attribute('placeholder'),'Learner Reference Number')
		input3 = self.browser.find_element_by_id('lrn').send_keys("191817152512")
		time.sleep(1)

		input4 = self.browser.find_element_by_id('birthday')  
		self.assertEqual(input4.get_attribute('placeholder'),'Birthday (M/D/Y)')
		input4 = self.browser.find_element_by_id('birthday').send_keys("3/31/99")
		time.sleep(1)

		input5 = self.browser.find_element_by_id('address')  
		self.assertEqual(input5.get_attribute('placeholder'),'Address')
		input5 = self.browser.find_element_by_id('address').send_keys("Blk 79 Lot 8 Barangay San Eteban Dasmarinas Cavite")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('enroll').click()
		time.sleep(2)
		self.browser.quit()



'''if __name__ == '__main__':
	unittest.main()

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''


#MAX_WAIT = 10