import random

class PasswordGenerator:
    """Простой класс для генерации паролей по 
    заданным пользователем параметрам"""
    lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()'

    def __init__(self):
        # Инициализация атрибутов
        self.len_password = None
        self.available_lowercase_letters = None
        self.available_uppercase_letters = None
        self.available_digits = None
        self.available_special_char = None
        self.password = None

    @staticmethod
    def check_user_input(text, check_valid_values):
        """Выводит сообщение пользователю о вводе параметра, если значение 
        недопустимое выдает ошибку и просит ввести ещё раз и выполняет приведение
        данные к общему виду"""
        while True:
            print(text, end='   ')
            input_value = input()
            if check_valid_values(input_value):
                break
            else:
                print('Недопустимое значение параметра! Попробуйте ещё раз')
        if not input_value.isdigit():
            input_value = input_value.lower()
            return input_value == 'да'
        else:
            return int(input_value)

    def get_user_input(self):
        """Реализует диалог с пользователем и сохранияет настройки
        генерации пароля в атрибуты объекта класса"""
        self.len_password = \
            self.check_user_input('Введите длину пароля:',
                                  lambda x: x.isdigit() and int(x) > 0)
        avalible_answer = lambda x: x.lower() in ['да', 'нет']
        self.available_lowercase_letters = \
            self.check_user_input('Включать ли строчные буквы? (да/нет)',
                                  avalible_answer)
        self.available_uppercase_letters = \
            self.check_user_input('Включать ли заглавные буквы? (да/нет)',
                                  avalible_answer)
        self.available_digits = self.check_user_input('Включать ли цифры? (да/нет)',
                                                       avalible_answer)
        self.available_special_char = self.check_user_input('Включать ли специальные символы? (да/нет)', 
                                                            avalible_answer)

    def check_categories_char(self):
        "Реализует проверку что пользователь выбрал хотя-бы одну из категорий символов"
        categories = [
            self.available_lowercase_letters,
            self.available_uppercase_letters,
            self.available_digits,
            self.available_special_char
        ]
        if any(categories):
            return True
        else:
            print('Для генерации пароля выберите хотя-бы одну категорию символов')
            return False

    def generate_password(self):
        """Реализует генерацию пароля по параметрам, следит чтобы в пароле присутствовали
        символы выбранных категорий"""
        print('Идёт генерация пароля...')
        count_categories = 0
        password = []
        list_available_values = []

        # Добавляем обязательные символы для каждой категории 
        # и формируем список доступных символов
        if self.available_lowercase_letters:
            list_available_values.extend(self.lower_case_letters)
            password.append(random.choice(self.lower_case_letters))
            count_categories += 1
        if self.available_uppercase_letters:
            list_available_values.extend(self.upper_case_letters)
            password.append(random.choice(self.upper_case_letters))
            count_categories += 1
        if self.available_digits:
            list_available_values.extend(self.digits)
            password.append(random.choice(self.digits))
            count_categories += 1
        if self.available_special_char:
            list_available_values.extend(self.special_chars)
            password.append(random.choice(self.special_chars))
            count_categories += 1

        # Проверка на соответствие длины пароля количеству категорий
        if count_categories > self.len_password:
            return False

        # Добавляем оставшиеся символы
        for _ in range(self.len_password - len(password)):
            password.append(random.choice(list_available_values))

        # Перемешиваем символы
        random.shuffle(password)

        # Сохраняем результат в атрибут
        self.password = ''.join(password)
        return True


def main():
    print('Программа для генерации пароля')
    while True:
        generator = PasswordGenerator()
        while True:
            generator.get_user_input()
            if generator.check_categories_char():
                if generator.generate_password():
                    break
                else:
                    print('Длина пароля должна быть больше или равна количеству выбранных категорий!')
        print(f'Сгенерированный пароль: {generator.password}')
        if not PasswordGenerator.check_user_input('Хотите сгенерировать ещё пароль? (да/нет)',
                                                  lambda x: x.lower() in ['да', 'нет']):
            return


if __name__ == "__main__":
    main()