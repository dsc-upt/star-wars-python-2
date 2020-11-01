from getpass import getpass

import yagmail


def main():
    username = "crisstian.prodan@gmail.com"
    password = getpass()
    print(password)
    mail_client = yagmail.SMTP(username, password)
    receiver = input("Insert email: ")
    mail_client.send(receiver, "Test mail", "Mail body")


if __name__ == '__main__':
    main()
