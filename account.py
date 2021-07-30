class Account(object):
    def __init__(self, first_name: str,
                 second_name: str,
                 country: str,
                 birthday: str,
                 login: str,
                 password: str):
        self.first_name = first_name
        self.second_name = second_name
        self.country = country
        self.birthday = birthday
        self.login = login
        self.__password = password

        self.__chats = {}  # чаты аккаунта

    def return_password(self) -> str:
        return self.__password

    def change_info(self):
        # TODO: Реализовать изменение личных данных (логин, пароль)
        pass

    def add_chat(self, login: str) -> None:
        self.__chats[login] = {}  # добавляется переписка(пустая) в виде типа данных дикт
