import time
import os
from anticaptchaofficial.recaptchav2proxyless import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("user-data-dir=D:/Sanofi/rpascripts/SP/User Data")

def procuraGoogle(email):

    driver = webdriver.Chrome(options = chrome_options)

    driver.get('http://google.com.br')

    driver.find_element_by_name('q').send_keys(email+' site:pastebin.com')

    driver.find_element_by_name('btnK').submit()

    time.sleep(3)

    try:

        driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3/span').click()

        textos = 'Conta vazada! Visite esse link para mais informações: '+driver.current_url

    except:

        textos = 'Parabéns! Sua conta não foi vazada.'

    driver.quit()

    return textos

def haveIBeenPwned(email):

    driver = webdriver.Chrome(options = chrome_options)

    driver.get('https://haveibeenpwned.com/')

    driver.find_element_by_name('Account').send_keys(email)

    driver.find_element_by_id('searchPwnage').click()

    time.sleep(5)

    try:

        vazamentos = driver.find_elements_by_class_name('col-sm-10')

        textos = []

        dadosVazados = []

        for vazamento in vazamentos:

            textos.append('Responsável pelo vazamento: '+vazamento.find_element_by_class_name('pwnedCompanyTitle').text+':\n')

            dadosVazados.append(vazamento.find_element_by_class_name('dataClasses').text+'\n')

        dados = ''

        aux = 0

        for texto in textos:

            dados = dados+texto+dadosVazados[aux]

            aux +=1
    
    except:

        dados = 'Parabéns! Sua conta não foi vazada.'

    driver.quit()

    return dados

def weLeakInfo(email):

    driver = webdriver.Chrome(options = chrome_options)

    driver.get('https://weleakinfo.to/v2/')

    wait(driver,5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login"))).click()

    time.sleep(5)

    driver.find_element_by_id('username').send_keys('FiapCyber')

    driver.find_element_by_id('password').send_keys('FiapCyber100')

    driver.find_element_by_xpath('//*[@id="header"]/div/div/div/form/div[3]/button').click()

    time.sleep(5)

    wait(driver,5).until(EC.visibility_of_element_located((By.ID, "query"))).send_keys(email)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[3]/div[3]/div/button').click()

    time.sleep(5)

    try:

        resultados = driver.find_element_by_xpath('//*[@id="msg"]/div/div/div/div/table').text

        resultados = resultados[resultados.find('\n')+1:]

        resultados = 'O seguinte vazamento foi encontrado: '+resultados
    
    except:

        resultados = 'Parabéns! Sua conta não foi vazada.'

    driver.quit()

    return resultados

email = input(str('Digite o e-mail que você deseja verificar:\n'))

textosGoogle = procuraGoogle(email)
textosHave = haveIBeenPwned(email)
resultados = weLeakInfo(email)

arquivo = open('Senhas.txt', 'w')

arquivo.writelines('Pastebin:\n'+str(textosGoogle)+'\n\n' +
'Have I Been Pwned:\n'+str(textosHave)+'\n' + 
'We Leak:\n'+str(resultados)+'\n')

arquivo.close()

