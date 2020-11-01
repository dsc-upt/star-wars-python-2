from getpass import getpass
import yagmail

def main():
    username = "alexandra.andreea683@gmail.com"
    password = getpass()
    print(password)
    mail_client = yagmail.SMTP(username, password)  # simple mail transfer protocol
    receiver = input('Insert email: ')
    if '@' not in receiver:
        print('Email invalid!')
    else:
        mail_client.send(receiver, "Test mail", "Mail body")
        print("Mail sent")

if __name__== '__main__':
    main()
