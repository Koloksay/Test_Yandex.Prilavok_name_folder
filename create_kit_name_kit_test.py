import sender_stand_request
import data

#Функция возвращает копию словаря kit_body из файла data.py и заменяет в нём значение "name" на то,
# что указано при обращении к функции в скобках
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле firstName
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
#    auth = sender_stand_request.auth_token(kit_body)
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_products_set(kit_body)
   # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # В ответе поле name совпадает с полем name в запросе
    assert user_response.json()['name'] == name

# Функция для негативной проверки
def negative_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_products_set(kit_body)
   # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400

# Функция для негативной проверки если передано пустое тело kit_body
def negative_assert_no_name(name):
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_products_set(name)
   # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400

# Тест 1. Успешное создание пользователя
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")

# Тест 2. Успешное создание пользователя
# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.s_511)

# Тест 3. Выводится ошибка 400 если параметр name состоит из 0 символов
def test_create_kit_0_letter_in_name_get_success_response():
    negative_assert("")

# Тест 4. Выводится ошибка 400 если параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert(data.s_512)

# Тест 5. Успешное создание пользователя
# Параметр name состоит из английский букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание пользователя
# Параметр name состоит из кириллицы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание пользователя
# Параметр name состоит из спецсимволов
def test_create_kit_simvol_in_name_get_success_response():
    positive_assert("/№%@")

# Тест 8. Успешное создание пользователя
# Параметр name содержин пробелы
def test_create_kit_probel_in_name_get_success_response():
    positive_assert("Человек и КО")

# Тест 9. Успешное создание пользователя
# Параметр name содержин цифры
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка 400 если параметр "name" не передан в запросе
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    # Иначе можно потерять данные из исходного словаря
    user_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    user_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(user_body)

# Тест 11.Передан другой тип параметра (число)
def test_create_kit_name_is_int_in_name_get_success_response():
    negative_assert(123)