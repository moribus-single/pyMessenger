from pydantic import BaseModel


class AccountDb(BaseModel):
    """For validating data in '/registration' - server.sign_up()"""
    first_name: str
    second_name: str
    country: str
    birthday: str
    login: str
    password: str


class AccountLogIn(BaseModel):
    """For validating data in '/login' - server.login()"""
    login: str
    password: str


class Message(BaseModel):
    """For validating data in '/send' - server.send_msg()"""
    sender: str
    message: str
