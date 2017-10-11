'''
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой
из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

форк PyCrypto, который ставится на любую машину без проблем: https://github.com/Legrandin/pycryptodome

Для установки simplecrypt:
1. pip install pycryptodome
2. pip install simple-crypt
'''

from simplecrypt import encrypt, decrypt, DecryptionException

f = open("passwords.txt", "r")

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

for line in f:
    passwd = line.rstrip()
    try:
        plaintext = decrypt(passwd, encrypted)
    except DecryptionException:
        continue
    print(plaintext)

f.close()