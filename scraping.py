from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import os
import pandas as pd

data = pd.read_csv('input.csv', delimiter=';')

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 10)

url = "https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp"

driver.get(url)

api_key = os.getenv('APIKEY_2CAPTCHA', 'coloque a chave da API')

solver = TwoCaptcha(api_key)

list_cpf = []
list_nome = []
list_nascimento = []
list_situacao = []
list_data_inscricao = []
list_digito_verificador = []
list_comprovante = []

for index, row in data.iterrows():

    try:
        result = solver.hcaptcha(
            sitekey='coloque o sitekey',
            url=url,
        )

    except Exception as e:
        print("Erro ao solicitar solucao do hCaptcha.")

    driver.execute_script(f"document.getElementsByName('h-captcha-response')[0].value = '{result['code']}'")

    cpf = "{:011d}".format(int(row['CPF']))
    data_nascimento = str(row['Data Nascimento'])
    
    wait.until(EC.presence_of_element_located((By.ID, "txtCPF"))).clear()
    driver.find_element(By.ID, "txtCPF").send_keys(cpf)
    
    wait.until(EC.presence_of_element_located((By.ID, "txtDataNascimento"))).clear()
    driver.find_element(By.ID, "txtDataNascimento").send_keys(data_nascimento)
    
    wait.until(EC.element_to_be_clickable((By.ID, "id_submit"))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainComp > div:nth-child(4) > p:nth-child(2)")))

    cpf = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(1) > b").text
    list_cpf.append(cpf)

    nome = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(4) > b").text
    list_nome.append(nome)

    nascimento = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(7) > b").text
    list_nascimento.append(nascimento)

    situacao = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(10) > b").text
    list_situacao.append(situacao)

    data_inscricao = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(13) > b").text
    list_data_inscricao.append(data_inscricao)

    digito_verificador = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(3) > p > span:nth-child(16) > b").text
    list_digito_verificador.append(digito_verificador)

    comprovante = driver.find_element(By.CSS_SELECTOR, "#mainComp > div:nth-child(4) > p:nth-child(2) > span:nth-child(3) > b").text
    list_comprovante.append(comprovante)

    driver.get(url)

driver.quit()

df_result = pd.DataFrame({
    "CPF": list_cpf,
    "Nome": list_nome,
    "Data Nascimento": list_nascimento,
    "Situação Cadastral": list_situacao,
    "Data da Inscrição": list_data_inscricao,
    "Digito Verificador": list_digito_verificador,
    "Código Comprovante": list_comprovante 
    })

df_result.to_excel("output.xlsx", index=False)

print("Finalizado com sucesso.")