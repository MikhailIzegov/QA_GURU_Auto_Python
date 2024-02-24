import allure
from allure_commons.types import Severity


# BBD - Behaviour-Driven Development, круто для менеджеров
def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('НЕавторизованный пользователь НЕ может создать задачу')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'ms_izegov')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass
