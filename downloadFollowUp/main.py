import os.path
from pathlib import Path
from datetime import datetime
import linecache
import time
import loginLib
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    horaInicio = datetime.now()

    caminhoAcessos = Path("acessos.txt")

    if caminhoAcessos.is_file():
        if os.path.getsize("acessos.txt") == 0:
            acessos = open("acessos.txt", "w")
            acessos.write("1")
            acessos.close()
            loginLib.__gerarChaveCriptografica()
            print("Para o primeiro acesso, favor informar seu usuário e senha.")
            loginLib.__armazenarLogin()
        else:
            acessos = open("acessos.txt", "r")
            qtAcessos = int(linecache.getline("acessos.txt", 1))
            acessos.close()
            acessos = open("acessos.txt", "w")
            acessos.write(str(qtAcessos + 1))
            acessos.close()
    else:
        acessos = open("acessos.txt", "w")
        acessos.write("1")
        acessos.close()
        loginLib.__gerarChaveCriptografica()
        print("Para o primeiro acesso, favor informar seu usuário e senha.")
        loginLib.__armazenarLogin()

    usuario = loginLib.__descriptografarLogin()[0]
    senha = loginLib.__descriptografarLogin()[1]

    firefox_opcoes = webdriver.FirefoxOptions()
    firefox_opcoes.add_argument("--headless")
    firefox_opcoes.add_argument("--start-maximized")
    firefox_opcoes.add_argument("--disable-infobars")
    firefox_opcoes.add_argument("--disable-extensions")
    firefox_opcoes.add_argument("--no-sandbox")
    firefox_opcoes.add_argument("--disable-application-cache")
    firefox_opcoes.add_argument("--disable-gpu")
    firefox_opcoes.add_argument("--disable-dev-shm-usage")
    firefox_opcoes.set_preference("security.insecure_field_warning.contextual.enabled", False)
    firefox_opcoes.set_preference("security.insecure_field_warning.contextual.enabled", False)
    driver = webdriver.Firefox(options=firefox_opcoes)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)

    driver.get("http://portalsim.lider.lan/FollowUp/")

    driver.find_element(By.ID, "Login").send_keys(usuario)

    driver.find_element(By.ID, "Senha").send_keys(senha)

    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    driver.find_element(By.XPATH, "//i[@class='fa fa-flag']").click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-pesquisar-followup")))

    driver.find_element(By.ID, "btn-pesquisar-followup").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Pesquisar']")))

    driver.find_element(By.XPATH, "//*[@title='Pesquisar']").click()

    time.sleep(10)

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "btn-exportar-dados")))

    driver.find_element(By.ID, "btn-exportar-dados").click()

    time.sleep(300)

    arquivoFinal = ""

    for arquivo in os.listdir(r"C:\Users\ddias\Downloads"):
        i = 0
        if os.path.basename(os.path.join(r"C:\Users\ddias\Downloads", arquivo)).__contains__("FOLLOWUP-" + datetime.today().strftime("%Y-%m-%d") + "-"):
            if i == 0:
                arquivoFinal = arquivo
                i += 1
            if datetime.fromtimestamp(os.path.getctime(os.path.join(r"C:\Users\ddias\Downloads", arquivo))).strftime("%d/%m/%Y %H:%M:%S") >= datetime.fromtimestamp(os.path.getctime(os.path.join(r"C:\Users\ddias\Downloads", arquivoFinal))).strftime("%d/%m/%Y %H:%M:%S"):
                arquivoFinal = arquivo


    os.system("start excel.exe " + os.path.join(r"C:\Users\ddias\Downloads", arquivoFinal))