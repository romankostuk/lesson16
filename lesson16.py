def send_email(message, recipient, sender = "university.help@gmail.com"):
    for i in recipient:
        if '@' in recipient or '.com' in recipient:
            if '.ru' in recipient:
                if '.net' in recipient:
                    if '@' in sender or '.com' in sender:
                        if '.ru' in sender:
                            if '.net' in sender:
                                if sender == university.help@gmail.com:
                                    print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
                                else:
                                    print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

