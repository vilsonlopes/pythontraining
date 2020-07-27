def greet_user(): # Exibe uma saudação simples
    print('Hello!')
greet_user()

def greet_user(username):
    print(f'Hello, {username}!')
greet_user('Vilson')

def describe_pet(animal_type, pet_name): # Exibe informações sobre um animal de estiamação.
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type} 's name is {pet_name}.")
describe_pet('Dog', 'Wall')
describe_pet('hamster', 'harry')

def describe_pet(pet_name, animal_type='dog'):
    """
    Exibe informações sobre um animal de estimação
    :param pet_name:
    :param animal_type:
    :return:
    """
    print(f'\nI have a {animal_type}')
    print(f'My {animal_type}`s name is {pet_name}.')
describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='vilson')
