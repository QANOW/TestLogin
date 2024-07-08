from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver
driver = webdriver.Chrome()

# Função para abrir a página de login
def open_login_page():
    driver.get("http://www.cashpago.com.br/login")  # URL fictícia para fins de simulação
    time.sleep(2)  # Espera a página carregar

# Função para testar login com credenciais válidas
def test_valid_login():
    open_login_page()
    driver.find_element(By.ID, "user_login").send_keys("usuario_valido")
    driver.find_element(By.ID, "user_pass").send_keys("senha_valida")
    driver.find_element(By.ID, "wp-submit").click()
    time.sleep(2)  # Espera o login ser processado
    assert "Página Inicial" in driver.title  # Verifica se foi redirecionado para a página inicial

# Função para testar login com credenciais inválidas
def test_invalid_login():
    open_login_page()
    driver.find_element(By.ID, "user_login").send_keys("usuario_invalido")
    driver.find_element(By.ID, "user_pass").send_keys("senha_invalida")
    driver.find_element(By.ID, "wp-submit").click()
    time.sleep(2)  # Espera o login ser processado
    error_message = driver.find_element(By.ID, "login_error").text
    assert error_message == "Usuário ou senha inválidos"

# Função para testar login com campos vazios
def test_empty_fields_login():
    open_login_page()
    driver.find_element(By.ID, "wp-submit").click()
    time.sleep(2)  # Espera o login ser processado
    error_message = driver.find_element(By.ID, "login_error").text
    assert error_message == "Campos obrigatórios não podem estar vazios"

# Executa os testes
try:
    test_valid_login()
    print("Teste de login com credenciais válidas passou.")
except AssertionError:
    print("Teste de login com credenciais válidas falhou.")

try:
    test_invalid_login()
    print("Teste de login com credenciais inválidas passou.")
except AssertionError:
    print("Teste de login com credenciais inválidas falhou.")

try:
    test_empty_fields_login()
    print("Teste de login com campos vazios passou.")
except AssertionError:
    print("Teste de login com campos vazios falhou.")

# Fecha o WebDriver
driver.quit()
