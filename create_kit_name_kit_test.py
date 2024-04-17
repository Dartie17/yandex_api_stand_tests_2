import sender_stand_request
import data

# Получение токена пользователя
def get_new_user_token():
    user_response = sender_stand_request.post_new_user()
    user_token = user_response.json()["authToken"]
    return user_token

# Копирование тела запроса из файла "data" и замена в нем названия набора
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Позитивная проверка
def positive_assert(name):
    kit_body = get_kit_body(name)
    user_token = get_new_user_token()
    kit_response = sender_stand_request.post_user_kit(kit_body, user_token)
    assert kit_response.status_code == 201
    user_kits_response = sender_stand_request.get_user_kits(user_token)
    assert user_kits_response.json()[0]["name"] == kit_body["name"]

# Негативная проверка
def negative_assert(name):
    kit_body = get_kit_body(name)
    user_token = get_new_user_token()
    kit_response = sender_stand_request.post_user_kit(kit_body, user_token)
    assert kit_response.status_code == 400
    user_kits_response = sender_stand_request.get_user_kits(user_token)
    assert user_kits_response.status_code == 404

# Негативная проверка (параметр "name" не передан)
def negative_assert_no_name():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    user_token = get_new_user_token()
    kit_response = sender_stand_request.post_user_kit(kit_body, user_token)
    assert kit_response.status_code == 400
    user_kits_response = sender_stand_request.get_user_kits(user_token)
    assert user_kits_response.status_code == 404

# Тест № 1. Успешное создание набора пользователя
# Параметр "name" состоит из 1 символа
def test_create_userkit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест № 2. Успешное создание набора пользователя
# Параметр "name" состоит из 511 символов
def test_create_userkit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест № 3. Ошибка
# Параметр "name" состоит из 0 символов
def test_create_userkit_0_letter_in_name_get_error_response():
    negative_assert("")

# Тест № 4. Ошибка
# Параметр "name" состоит из 512 символов
def test_create_userkit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест № 5. Успешное создание набора пользователя
# Параметр "name" состоит из английских букв
def test_create_userkit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест № 6. Успешное создание набора пользователя
# Параметр "name" состоит из русских букв
def test_create_userkit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест № 7. Успешное создание набора пользователя
# Параметр "name" состоит из спецсимволов
def test_create_userkit_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест № 8. Успешное создание набора пользователя
# Параметр "name" состоит из строки с пробелами
def test_create_userkit_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест № 9. Успешное создание набора пользователя
# Параметр "name" состоит из цифр
def test_create_userkit_number_in_name_get_success_response():
    positive_assert("123")

# Тест № 10. Ошибка
# Параметр "name" не передан
def test_create_userkit_no_name_get_error_response():
    negative_assert_no_name()

# Тест № 11. Ошибка
# Параметр "name" передан в другом типе (число)
def test_create_userkit_number_type_in_name_get_error_response():
    negative_assert(123)