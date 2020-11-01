from getpass import getpass
import yagmail

def main():
    username = "dean.crainic@gmail.com"
    password = getpass()
    mail_client = yagmail.SMTP(username, password)
    receiver = input("Insert email: ")
    if "@" not in receiver:
        print("Email invalid. Exiting")
    else:
        mail_client.send(receiver, "Test mail from localhost", "Mail body")
        print("Mail sent.")


if __name__ == '__main__':
    main()
