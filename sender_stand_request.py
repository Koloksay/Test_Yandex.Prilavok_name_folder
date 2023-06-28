import configuration
import requests
import data

#получение токена
def get_auth():
    auth = post_new_user(data.user_body).json()["authToken"]
    return auth

#создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставялем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

#создание нового набора
def post_products_set(kit_body):
    #копируем заголовки из файла data.py в переменную head
    head = data.headers.copy()
    #меняем значение строчки Authorization на нужный формат, подствляя токен
    head["Authorization"] = "Bearer " + get_auth()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_SET,
                         json=kit_body,
                         headers=head)