# ozon_bank_task

Задание https://github.com/eshmargunov/tech_intreview_task

Список основных проблем в коде:

1. Токен передаётся в открытом виде
2. Данные не очищаются после теста, что засоряет папку и фейлит последующие тесты
3. После загрузки картинок нет проверки, что они все прогрузились (или хотя бы time.sleep()), из-за чего тест падает, т.к. сразу же запрашивается содержимое папки
4. Дублирование кода:
   - не вынесены в отдельную переменную headers, урлы, test_folder, response.json()['_embedded']['items'], token (для токена к тому же в тесте используется f-строка без переменной);
   - одинаковый цикл for в тесте и для if, и для else;
   - вызов функции get_sub_breeds 3 раза в тесте (2 раза напрямую и 1 раз внутри загрузки картинок), когда достаточно 1
5. Логика тестов и реализация - всё в одном файле
6. Практически одни и те же входные данные при каждом прогоне теста
7. Странные непонятные места:
   - assert True (зачем?);
   - \# проверка (что имеется в виду?);
   - def u (неговорящее название);
   - def test_proverka_upload_dog (proverka лишнее)
8. Отсутствие необязательных, но желательных элементов, таких как:
   - заголовок теста;
   - сообщения об ошибках в ассертах;
   - аннотации в функциях
9. Разный стиль для одинаковых вещей:
   - одинарные и двойные кавычки;
   - именованные параметры с лишними пробелами headers = headers и headers=headers;
   - названия переменных res, resp, response
10. Методы create_folder и upload_photos_to_yd в классе YaUploader:
    - resp и response не используются
    - ни self не используется, ни методы не отмечены как @staticmethod



