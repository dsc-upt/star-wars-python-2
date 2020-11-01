from getpass import getpass

import yagmail

def main():
    username = "crazylord2001@gmail.com"
    password = getpass()
    mail_client = yagmail.SMTP(username, password)
    receiver = input("Insert email: ")
    if "@" not in receiver:
        print("Email invalid. Exiting")
    else:
        mail_client.send(receiver, "Restricted", "Salut cu respect")
        print("Mail sent")

if __name__ == '__main__':
    main()

