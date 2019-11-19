from c import Pinterest
import time
import random
from os.path import isfile, join
import os
from os import listdir
import os.path

titulo_1 = ['emagrecer rapido nunca foi tão fácil',
	'veja o que os famosos estão fazendo para emagrecer rápido',
	'entenda melhor a forma de emagrecer rapido e sem esforço',
	'veja as formas de emagrecer rapido e com pouco dinheiro',
	'emagrecer de uma forma aceitável pode custar muito a sua saúde', 
	'pensando nisso criamos essa receita',
	'veja as melhores forma de emagrecer', 
	'entenda melhor como faustão faz para emagrecer', 
	'O resultado dos famosos não depende só deles',
	'A melhor escolha para emagrecer nunca foi ficar parado',
	'emagrecer mortivacao e também motivado é um custo baixo e você tem que pagar', 
	'nada pode parar sua superação de vencer e conseguir emagrecer', 
	'nem tudo na vida vai fazer você conseguir emagrecer de forma simples', 
	'As maiores batalhes tem os melhores resultados',
	'As pessoas vão duvidar de você emagrecer', 
	'emagrecer com gosto e estilo']

descricao_1 = ["Emagreça com estilo e sabedoria, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Salve esse Pin e clique 2x na Imagem , #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Voê quer emagrecer de fato ? clique no link , #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Saiba como emagrecer de fato, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Clica no Link para saber como emagrecer de fato , #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Entenda melhor como emagrecer em menos de 17 dias , #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"O Principal segredo para você poder emagrecer , #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio #emagrecerrapidoemumasemana #emagrecerantesedepois #emagrecerbarriga",
	"Saiba como emagrecer de fato, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios #emagrecerrapidocardapio",
	"Saiba como emagrecer de fato, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidoexercicios",
	"Saiba como emagrecer de fato, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrap",
	"veja como você pode tá emagrecendo de fato!, #emagrecerrapido #emagrecer #emagrecermotivacao #emagrecerrapidocardapio"]

#title_1 = titulo_1 , titulo_2 , titulo_3
#titulo_ = random.choice(titulo_1,titulo_2,titulo_3) 

#descr = random.choice(descricao_1,descricao_2, descricao_3, descricao_4, descricao_5,descricao_6,descricao_7,descricao_8,descricao_9,descricao_10,descricao_11)

PhotoPath = "C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img\\marvel_braa"

link_de_destino_ = 'https://sites.google.com/view/emagrecer17diass'

Bot = Pinterest()

Bot.logar('login_or_email','password')

os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])

print(f'Existe: {ListFiles} Fotos')

for i in ListFiles:
	photo = os.path.abspath(i)
	print(photo)
	print(f'lis {ListFiles}')
	titulo_ = random.choice(titulo_1)
	descr = random.choice(descricao_1)
	Bot.upload_pin(
	pasta='emagrecer',
	titulo=titulo_,
	descricao=descr,
	link_de_destino=link_de_destino_,
	path_photo=photo
	)
	os.remove(photo)
	time.sleep(random.randint(300,400)) #voocê pode escolher o tempo que quiser aqui, recomendo upar uma IMG por minuto... além disso você pode tomar ban.
  
