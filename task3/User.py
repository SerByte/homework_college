from UserSettings import UserSettings


class User:

    def __init__(self, name, password, image):
        self.__name = name
        self.__password = password
        self.__image = image
        self.__settings = UserSettings()

    def login_user(self):
        print("User was successfully logged in")

    def save(self):
        print("User was successfully saved")

    def equals(self, user):
        if self.__class__ != user.__class__:
            return False
        if self.__name == user.__name and self.__image == user.__image and self.__password == user.__password:
            return True
        return False

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_image(self):
        return self.__image

    def get_settings(self):
        return self.__settings
