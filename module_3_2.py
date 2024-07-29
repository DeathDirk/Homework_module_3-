def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if("@" not in recipient or '@' not in sender) or (not recipient.endswith((".com", '.ru', 'net'))
                                                       and not sender.endswith(('.com', '.ru', '.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с  адреса {sender} на адрес {recipient}.")
    else:
    # elif sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
#Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1
# обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в
# консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с
# адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес
# <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!

# if ('@' or (".com" or ".ru" or ".net")) not in (recipient or sender):
#     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
#     return

#error_v = ["@", ".com", ".ru", ".net"]
    # if('@' and (".com" or ".ru" or ".net")) not in (recipient and sender):
    #       print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # if ('@' or ".com" or ".ru" or ".net") not in recipient or ('@' or ".com" or ".ru" or ".net") not in sender:
    #     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    #     return