from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# iniciar um navegador
navegador = webdriver.Chrome()
time.sleep(3)
# acessar site
navegador.get('https://www.google.com')
time.sleep(3)
# esperar página carregar
time.sleep(3)

# encontrar o campo de busca (usando o nome do elemento)
campo_busca = navegador.find_element(By.NAME, 'q') # busca o campo pelo atributo HTML, e q é o nome do campo do Google

# digitar palavra chave
campo_busca.send_keys('Clima em Fortaleza')

#pressionar enter
campo_busca.send_keys(Keys.RETURN)

#esperar resultado
time.sleep(3)
time.sleep(3)
time.sleep(3)
time.sleep(3)


#tirar print da tela (só pra testar visulamente)
navegador.save_screenshot('D:/Usuário/anderson/Downloads/resultado.png')

#fechar navegador
navegador.quit()
