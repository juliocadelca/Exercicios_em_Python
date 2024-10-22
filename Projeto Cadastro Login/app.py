
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl as op

driver = webdriver.Chrome()
# 1 - Navegar até o site https://contabilidade-devaprender.netlify.app
driver.get('https://contabilidade-devaprender.netlify.app')
sleep(5)
# 2 - Digitar o email
email = driver.find_element(By.XPATH, "//input[@type='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')
# 3 - Digitar a senha
senha = driver.find_element(By.XPATH, "//input[@type='password']")
senha.send_keys('contabilidade123456')
sleep(2)
# 4 - Clicar em entrar
entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
entrar.click()
sleep(10)
# 5 Extrair as informações da planilha
empresas = op.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']
# 6 - Clicar em cada campo e preemcher com dados da planilha.
# 7 - Clicar em cadastrar
for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, oemail, telefone, endereço, cnpj, area_de_atuação, quantidade_funcionarios, data_fundação = linha

    driver.find_element(By.ID, "nomeEmpresa").send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID, "emailEmpresa").send_keys(oemail)
    sleep(1)
    driver.find_element(By.ID, "telefoneEmpresa").send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID, "enderecoEmpresa").send_keys(endereço)
    sleep(1)
    driver.find_element(By.ID, "cnpj").send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID, "areaAtuacao").send_keys(area_de_atuação)
    sleep(1)
    driver.find_element(By.ID, "numeroFuncionarios").send_keys(quantidade_funcionarios)
    sleep(1)
    driver.find_element(By.ID, "dataFundacao").send_keys(data_fundação)
    sleep(1)
    driver.find_element(By.ID, "Cadastrar").click()
