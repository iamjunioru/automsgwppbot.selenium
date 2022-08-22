from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas
from selenium.webdriver.common.keys import Keys


excel_data = pandas.read_excel('data.xlsx', sheet_name='data')


driver = webdriver.Chrome()
input("depois de fazer login com o QRcode, aperta ENTER p continuar.")
for column in excel_data['contato'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['contato'][1]) + '&text=' + excel_data['mensagem'][0]  
        driver.get(url)
        xpath_val = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        wait = WebDriverWait(driver, 10)
        sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath_val))).send_keys(Keys.ENTER)
        sleep(5)
        print('mensagem enviada: ' + str(excel_data['contato'][1]))
    except Exception as e:
        print('mensagem enviada: ' + str(excel_data['contato'][1]) + str(e))
driver.quit()
print("script executado c sucesssssssooo!")