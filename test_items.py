﻿from selenium import webdriver
import time

def get_link():    # Метод, передающий ссылку на сайт
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    return link


def test_should_be_button_basket(browser):
    link = get_link()    # Получение ссылки 
    browser.get(link)    # Передача ссылки в метод get
    time.sleep(30)    # Ожидание - для проверки текста в кнопке
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "There isn't button basket on the site"    # Проверка


 