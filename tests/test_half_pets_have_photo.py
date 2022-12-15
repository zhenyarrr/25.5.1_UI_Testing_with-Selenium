import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_half_pets_have_photo(show_my_pets):
    '''Тест на проверку, что у половины питомцев есть фото на странице со списком питомцев'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))

    # Получаем количество питомцев из статистики пользователя
    all_my_pets_number = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]


    # Получаем элементы с атрибутом img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')


    # Получаем половину от количества питомцев
    half = int(all_my_pets_number)//2

    # Находит количество питомцев с фото
    number_a_photo = 0
    for i in  range(len(images)):
        if images[i].get_attribute('src') != '':
            number_a_photo += 1

    # Проверяем, что количество питомцев с фото больше или равно половине количества питомцев пользователя
    assert number_a_photo >= half
    print('\nКоличество питомцев с фото=', number_a_photo)
    print(f'Половина от числа питомцев= {half}')



