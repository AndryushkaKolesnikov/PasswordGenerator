class PasswordGenerator():    
    """Простой класс для генерации паролей по 
    заданным пользователем параметрам"""
    def __init__(self):
        print('Программа для генерации паролей')


    @staticmethod
    def check_user_input(text, check_valid_values):
        while True:
            print(text, end='   ')
            input_value = input()
            if check_valid_values(input_value):
                break
            else:
                print('Недопустимое значение параметра попробуйте ещё раз')
        return input_value

    
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
        self.avaliable_digits = self.check_user_input('Включать ли цифры? (да/нет)',
                                                       avalible_answer)
        
if __name__ == "__main__":
    object_PasswordGenerator = PasswordGenerator()
    object_PasswordGenerator.get_user_input()