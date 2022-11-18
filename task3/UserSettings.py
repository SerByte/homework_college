class UserSettings:

    def __init__(self):
        self.__is_2FA_enabled = False

    def is_2FA_enabled(self):
        return self.__is_2FA_enabled