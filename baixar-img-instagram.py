from selenium import webdriver
from time import sleep
from urllib.request import urlretrieve
import os
from selenium.webdriver import ActionChains

caminho_d = 'C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img'


hashtags = ['emagrecer._.rapido']
#'', '', '', '', 'trilhas', 'brutas', 'brutos', 'churrasco'
for htg in hashtags:
    hashtag = htg
    
    navegador = webdriver.Firefox()

    link = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    link_hashtag = 'https://www.instagram.com/'



    navegador.get(link_hashtag + hashtag)
    sleep(1.0)
    qt_download = 100
    desc_pixel= 1500 
    prim_vez = True
    old = 0
    tent = 0
    ocorr = 0
    pagina_a_rolar = 10
    
    while qt_download:
        if prim_vez:
            with open('links_download.txt', mode='w', encoding='UTF-8') as getlink:
                print('DB links Criado!')
                prim_vez = False
            
        cards_link = navegador.find_elements_by_css_selector('.Nnq7C.weEfm > .v1Nh3.kIKUG._bz0w > a')
        
        with open('links_download.txt', mode='a', encoding='UTF-8') as getlink:
            for clnk in set(cards_link):    
                get_lnk = clnk.get_attribute('href')
                getlink.write(f'{get_lnk}\n')
            
        with open('links_download.txt', mode='r', encoding='UTF-8') as checklink:
            check = checklink.readlines()
            links_semrep = len(set(check))
            if links_semrep > qt_download:
                qt_download = False
            elif links_semrep == tent:
                ocorr += 1
            elif ocorr == 5:
                print('Não conseguimos carregar o total de fotos!')
                print('Provavelmente o usuário não tem esse quantidade de fotos postadas!')
        navegador.execute_script(f'window.scrollTo(0, {str(desc_pixel)});')

        cards_link = None
        desc_pixel += 920
        sleep(2.5)

    # Limpando..

    with open('links_download.txt', mode='r') as limp:
        buff = limp.readlines()
        with open('links_download.txt', mode='w') as ado:
            for i in set(buff):
                ado.write(i)
        

    with open('links_download.txt', mode='r') as check:
        links = check.readlines()
        
        for crd in range(len(links)):
            navegador.get(links[crd])
            sleep(0.3)
            midias = navegador.find_elements_by_css_selector('img.FFVAD')
            user = navegador.find_element_by_css_selector('.BrX75').text        
                
             # navegador.find_element_by_css_selector('.BrX75 > a').get_attribute('href')
            
            for dwn in range(len(midias)):
                source = midias[dwn].get_attribute('src')
                if len(midias) > 0:
                    print(f'Downloading carrosel: {dwn + 1} imagens')
                print(f'{crd}_{user}')
                print('Realizando Download')
                
                os.chdir(f'{caminho_d}')
                if hashtag in os.listdir(f'{caminho_d}'):
                    pass
                else:
                    os.mkdir(f'{hashtag}')
                    
                os.chdir(f'{caminho_d}\\{hashtag}')
                
                urlretrieve(url=f'{source}', filename=f'{crd}_{user}_{dwn}.jpg')
                sleep(1)
    navegador.quit()
