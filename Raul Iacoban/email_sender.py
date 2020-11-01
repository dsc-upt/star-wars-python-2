from getpass import getpass
import yagmail

def main():
    username = "iacoban.raul08@gmail.com"
    password = getpass()
    print(password)
    mail_client = yagmail.SMTP(username, password) # SMTP simple mail transfer protocol

    receiver = input("insert email: ")
    #if "@" not in receiver:
       # print("email invalid. Exiting")
   # else
    mail_client.send(receiver, "titlu", "cf boss")


if __name__ == '__main__':
    main()