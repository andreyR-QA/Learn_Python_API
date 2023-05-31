# Выбираем пароли без повторений для ускорения работы скрипта в HW2_5.py
# Из файла passwords.txt, полученного копипастом из википедии, выбираем список паролей без повторов, чтобы быстрее выполнялся подбор

allpass = open('passwords.txt', 'r')
newpass1 = open('pass_out.txt', 'w+')
try:

    all_passwords = allpass.read()
    income_word: list[str] = all_passwords.split()      # Парсим хотичный список паролей на слова
    outpass: list[str] = [income_word[0]]               # определяем массив для удобства работы и чтобы не дергать файл
    i = 0
    while i < 225:                                        # цикл по индексу массива
        n = 0
        end_of_list = False
        while end_of_list == False:                                     # в данном цикле сравнивается одно слово исходного набора паролей с создаваемым массивом паролей без дулей
            if income_word[i] == outpass[n]:                            # если пароли совпали, то цикл завершается и переходим к следующему исходному паролю
                end_of_list = True
            elif n < len(outpass)-1 and income_word[i] != outpass[n]:    # если пароли не совпали и просмотрен не весь массив, то переходим к следующему элементу
                n += 1
            elif n == len(outpass)-1 and income_word[i] != outpass[n]:   # если пароли не совпали и просмотрен весь массив, то добавляем найденное слово в список паролей
                outpass.append(income_word[i])
                print(income_word[i], file=newpass1)
        i += 1
    print(i)                                        # счетчик-индикатор :)

finally:
    newpass1.close()
    allpass.close()
