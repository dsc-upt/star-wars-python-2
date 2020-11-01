from getpass import  getpass
import  yagmail


def main():
    username = "alex.gaita99@gmail.com"
    password=getpass()
    mail_client=yagmail.SMTP(username, password)
    receiver = input("Insert email: ")
    if "@" not in receiver:
        print("Email invalid")
    else:
        mail_client.send(receiver, "Test","body")
        print("Mail sent")


if __name__ == '__main__':
    main()
