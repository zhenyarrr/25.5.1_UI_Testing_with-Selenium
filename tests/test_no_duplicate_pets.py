import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test_no_duplicate_pets(show_my_pets):
    '''Поверяем что на странице со списком питомцев пользователя нет повторяющихся питомцев'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Получаем элементы с данными о питомцах из таблицы
    pets_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    time.sleep(5)

    # Перебираем данные из pets_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pets_data)):
        data_pet = pets_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    # Склеиваем имя, возраст и породу, получившиеся склеенные слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')
    print(list_line)

    # Превращаем список в множество
    set_list_line = set(list_line)
    print(set_list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b

    # Если количество элементов == 0 значит питомцы с одинаковыми данными отсутствуют
    assert result == 0