from selene import browser
from selene import be, have, by
import time

def test_first():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_demoqa_com():
    browser.element(by.id('userName')).type('Mishka')
    browser.element(by.id('userEmail')).type('mikhail.izegov@yandex.ru')
    browser.element(by.id('currentAddress')).type('Moscow, Russia')
    browser.element(by.id('permanentAddress')).type('Moscow, Russia')
    browser.element(by.id('submit')).click()
    browser.element(by.id('output')).should(have.text('Name:Mishka\nEmail:mikhail.izegov@yandex.ru\nCurrent Address :Moscow, Russia\nPermananet Address :Moscow, Russia'))
