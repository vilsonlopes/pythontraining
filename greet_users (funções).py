def greet_users(names):
    """
    Exibe uma saudação simples a casa usuário da lista.
    :param names:
    :return:
    """
    for name in names:
        msg = 'Hello, ' + name.title()
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'michael']
greet_users(usernames)
