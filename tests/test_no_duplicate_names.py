import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_no_duplicate_names(show_my_pets):
    '''Поверяем, что на странице со списком питомцев пользователя, у всех питомцев разные имена'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Получаем элементы с данными о питомцах из таблицы
    pets_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    time.sleep(5)

    # Перебираем данные из pets_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pets_data)):
        data_pet = pets_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
    # Проверяем, если r == 0 то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)
