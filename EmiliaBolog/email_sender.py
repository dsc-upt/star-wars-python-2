from getpass import getpass

import yagmail


def main():
    username = "bologemilia@gmail.com"
    password = getpass()
    mail_client = yagmail.SMTP(username, password)
    receiver = input("Insert mail: ")
    if "@" not in receiver:
        print("Email invalid!!! ")
    else:
        mail_client.send(receiver, "Test mail from loaclhost")
        print("Mail sent")


if __name__ == '__main__':
    main()