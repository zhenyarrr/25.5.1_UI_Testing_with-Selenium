import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_pets_have_name_age_gender(show_my_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Получаем элементы с данными о питомцах
    pets_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')


    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pets_data)):
         data_pet = pets_data[i].text.replace('\n', '').replace('×', '')
         split_data_pet = data_pet.split(' ')
         result = len(split_data_pet)
         assert result == 3


    #print('\ndata_pet==', data_pet)