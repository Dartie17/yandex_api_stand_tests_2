import configuration
import data
import requests

# Запрос на создание нового пользователя
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

# Запрос на создание нового набора
def post_user_kit(kit_body, auth_token):
    client_headers = data.headers.copy()
    client_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=client_headers)

# Запрос на получение всех наборов пользователя
def get_user_kits(auth_token):
    client_headers = data.headers.copy()
    client_headers["Authorization"] = "Bearer " + auth_token
    return requests.get(configuration.URL_SERVICE + configuration.GET_USER_KITS_PATH,
                         headers=client_headers)