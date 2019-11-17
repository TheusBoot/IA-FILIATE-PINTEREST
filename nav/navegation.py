from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Driver:
	def __init__(self):
		"""Estou Utilizando o Firefox, mas você pode usar o que bem entender"""
		self.driver = webdriver.Firefox()

	def logar(self,user_name_or_email, passoword):
		self.user_name_or_email = user_name_or_email
		self.passoword = passoword
		if self.user_name_or_email and self.passoword:

			"""Caso exista O user e a senha dele"""

			self.driver.get('https://br.pinterest.com')
			sleep(4)

			us = self.driver.find_element_by_id('email')
			us.send_keys(self.user_name_or_email)

			ps = self.driver.find_element_by_id('password')
			ps.send_keys(self.passoword)
			ps.send_keys(Keys.ENTER)
			sleep(4)

		else:
			print(f'''Error ao efetuar seu login, sua senha pode tá errada
				Login: {self.user_name_or_email}
				Passowrd{self.password}''')

	def _Using_User(self,User, pasta):
		url = f'https://br.pinterest.com/{User}/{pasta}/'
		self.driver.get(url)
		sleep(4)
		selc = Select(self.driver.find_element_by_xpath("//button[@class='x8f INd _O1 gjz mQ8 OGJ YbY']"))
		selc.selec_by_index(1).click()

Page = Driver()
Page.logar('emailmartingcf1@gmail.com','Matheuslorencia123')

Page._Using_User('emailmartingcf1','vegan-receitas')