from pages.KP import KP
from selenium import webdriver

email = input("Unesite email adresu :")
password = input("Unesite sifru: ")

naziv_artikla = input("Unesi naziv artikla: ")
cena = input("Unesi cenu artikla: ")
tekst_oglasa = input("Unesi opis artikla: ")


driver = webdriver.Chrome(executable_path='C://chromedriver.exe')


kp = KP(driver=driver)
kp.go()
kp.maximize_window()
kp.element("//*[@id='email']").send_keys(email)
kp.element("//*[@id='password']").send_keys(password)
kp.element("//*[@id='submitButton']").click()

window_after = driver.window_handles[0]
driver.switch_to.window(window_after)

kp.element('//*[@id="leftNav"]/div[2]/a').click()
kp.element('//*[@id="data[group_suggest_text]"]').send_keys(naziv_artikla)
kp.element('//*[@id="group-suggestions-holder"]/div/div[1]/div[2]/div[1]/input').click()
kp.element('//*[@id="groupSuggestionHolderTemplate"][1]').click()
kp.element('//*[@id="conditionForm"]/div[2]/div[1]/label[1]').click()
kp.element("//input[@id='price_number']").send_keys(cena)
kp.element('//*[@id="data[currency]"]/label[2]').click()

iframe = driver.find_element_by_xpath('//*[@id="data[description]_ifr"]')
driver.switch_to.frame(iframe)

kp.element('//*[@id="tinymce"]').send_keys(tekst_oglasa)

driver.switch_to.default_content()

kp.element('//*[@id="adFormInfo"]/div[2]/div[20]/div/input').click()
kp.element('//*[@id="data[currency]"]/label[2]').click()
kp.element('//*[@id="adFormPromo"]/div[4]/div/input').click()
kp.element('//*[@id="adFormDeclaration"]/div[7]/div[2]/div/div/label').click()
kp.element('//*[@id="adFormDeclaration"]/div[8]/div/input').click()

driver.close()
