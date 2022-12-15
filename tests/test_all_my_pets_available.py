import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_all_my_pets_available(show_my_pets):
   '''Проверяем что на странице со списком питомцев пользователя присутствуют все питомцы'''

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "#all_my_pets table tbody tr")))

   #Получаем количество питомцев из таблицы
   all_my_pets_in_table = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets table tbody tr')
   #time.sleep(5)

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))

   #Получаем количество питомцев из статистики пользователя
   all_my_pets_number = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]
   #time.sleep(5)

   assert len(all_my_pets_in_table) == int(all_my_pets_number)
   print('\nall_my_pets = ', len(all_my_pets_in_table), ',', 'all_my_pets_number =', all_my_pets_number)
