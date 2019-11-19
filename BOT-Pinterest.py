from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select


class Pinterest:
	def __init__(self):
		
		self.driver = webdriver.Firefox()

	def logar(self,user_name_or_email, passoword):
		self.user_name_or_email = user_name_or_email
		self.passoword = passoword
		if self.user_name_or_email and self.passoword:

			

			self.driver.get('https://br.pinterest.com/')
			time.sleep(4)

			us = self.driver.find_element_by_id('email')
			us.send_keys(self.user_name_or_email)

			ps = self.driver.find_element_by_id('password')
			ps.send_keys(self.passoword)
			ps.send_keys(Keys.ENTER)
			time.sleep(10)

		else:
			print(f'''Error ao efetuar seu login, sua senha pode tá errada
				Login: {self.user_name_or_email}
				Passowrd{self.password}''')

	def Using_User(self,User, pasta):
		#url = f'https://br.pinterest.com/{self.User}/{self.pasta}/'
		#self.driver.get(url)
		#time.sleep(10)
		#self.driver.refresh()
		#time.sleep(10)
		#selc = self.driver.find_element_by_id("Eqh f03 zI7 iyn Hsu")
		
		#selc = self.driver.find_element_by_css_selector(".F6l.Fje.Jea.fZz.hA-.hs0.k1A.sLG.zI7.iyn.Hsu")
		af = self.driver.find_element_by_xpath("//button[@data-test-id='board-dropdown-select-button']")
		af.click()
		time.sleep(3)
		selec = self.driver.find_element_by_id("pickerSearchField")
		selec.send_keys("emagrecer")
		x = self.driver.find_element_by_css_selector(".rLK.iyn.DI9.BG7.Xs7.gL3.FTD.L4E")
		x.click()
		#select = Select(af)
		#select.select_by_visible_text('emagrecer')
		#af.send_keys('emagrecer').click()
		#selc = Select(af)
		#selc.select_by_visible_text('emagrecer')
		#	.click()

	def upload_pin(self,pasta,titulo,descricao,link_de_destino,path_photo):
		self.driver.get('https://br.pinterest.com/pin-builder/')
		time.sleep(5)

		button_Pesquisa = self.driver.find_element_by_xpath("//button[@data-test-id='board-dropdown-select-button']")
		button_Pesquisa.click()
		time.sleep(3)

		campo_de_pesquisa = self.driver.find_element_by_id("pickerSearchField")
		campo_de_pesquisa.send_keys(pasta)

		nome_past_escolhida = self.driver.find_element_by_css_selector(".rLK.iyn.DI9.BG7.Xs7.gL3.FTD.L4E")
		nome_past_escolhida.click()

		time.sleep(3)
		title = self.driver.find_element_by_css_selector('.TextArea__textArea.TextArea__bold.TextArea__light.TextArea__enabled.TextArea__large.TextArea__wrap')
		title.send_keys(titulo)
		
		descricao_s = self.driver.find_element_by_css_selector('.TextArea__textArea.TextArea__light.TextArea__enabled.TextArea__medium.TextArea__wrap')
		descricao_s.send_keys(descricao)
		time.sleep(3)
		
		link_de_destino_s = self.driver.find_element_by_css_selector('.TextArea__textArea.TextArea__dark.TextArea__enabled.TextArea__medium.TextArea__nowrap')
		link_de_destino_s.send_keys(link_de_destino)
		time.sleep(3)

		path_photo_2 = self.driver.find_element_by_id('media-upload-input')
		path_photo_2.send_keys(path_photo)
		time.sleep(3)

		Save = self.driver.find_element_by_xpath('//button[@data-test-id="board-dropdown-save-button"]')
		Save.click()

		print(f'Imagem Upada com Sucesso: {path_photo}')

