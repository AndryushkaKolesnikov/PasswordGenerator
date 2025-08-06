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
        if not input_value.isdigit():
            input_value = input_value.lower()
            if input_value == 'да':
                return True
            else:
                return False
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
            

def main():
    object_PasswordGenerator = PasswordGenerator()
    while True:
        object_PasswordGenerator.get_user_input()
        flag = object_PasswordGenerator.check_categories_char()
        if flag:
            break
    

if __name__ == "__main__":
    main()