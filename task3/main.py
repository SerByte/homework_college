from User import User


def start():
    user_1 = User('Odeyalo', "aboba123", "Image url")
    user_1.save()

if __name__ == '__main__':
    start()
