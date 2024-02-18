from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("C:/Users/Rafi/Downloads/DevOps Course 24.12.23/tip_calc/tip_calc/index.html")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
''' dr.find_element(by="id", value="musicQual").send_keys("5") '''
dr.find_element(by="id", value="calculate").click()

actual = dr.find_element(by="id", value="tip").text
expected = "4.00"
assert expected == actual

'''
(assert) if is true - evrything is good, else - throw exeption.
'''

sleep(1000)
