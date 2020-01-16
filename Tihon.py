import smtplib
import sys

#DONT CHANGE THE PASSWORD, I`L BECAME YOUR IP AND DDOS YOU
email_provider = 'smtp.gmail.com' 
email_address = "tihonthespammer@gmail.com" 
email_port = 587 
#PASSWORD = 31.173.101.25  213.21.9.27 195.206.183.124   NO, IT ISN PASSWORD, THESE ARE IPS OF ALL BITCHES TRYED TO LOGIN
password = "pleasedontchange" #DONT CHANGE THE PASSWORD, I`L BECAME YOUR IP AND DDOS YOU LIKE THESE: 31.173.101.25  213.21.9.27 195.206.183.124
msg = "\nThis is SPAM" 
spam20 = 20 
spam50 = 50
spam100 = 100
spam1000 = 1000

#Func for sending
def sending():
    #Logo
    print(" ________   __   __   __   ______   __   __                             ")
    print("|__    __| |  | |  | |  | |  __  | |  \ |  |                    ")
    print("   |  |    |  | |  |_|  | | |  | | |   \|  |                      ")
    print("   |  |    |  | |   _   | | |  | | |       |  BY               ")
    print("   |  |    |  | |  | |  | | |__| | |  |\   |  CMD WITH HELP OF LEX                    ")
    print("   |__|    |__| |__| |__| |______| |__| \__|  v.1.1                                       ")
    print(">>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<<                        ")
    print("\nPlease, choose amount of Emails you want to send: \n[20]  [50]  [100]  [1000]")
    print("Example: 50")
    amount = input("Your choise: ")
    print(msg)
    print("Thats the message your victim will became")
    print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
    if amount == "20":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam20):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam20))
        server.quit()
        sys.exit()

    elif amount == "50":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam50):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam50))
        server.quit()
        sys.exit()

    elif amount == "100":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam100):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam100))
        server.quit()
        sys.exit()

    elif amount == "1000":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam100):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam1000))
        server.quit()
        sys.exit()

    else:
        print("error")
        sys.exit()


print(" ________   __   __   __   ______   __   __                             ")
print("|__    __| |  | |  | |  | |  __  | |  \ |  |                    ")
print("   |  |    |  | |  |_|  | | |  | | |   \|  |                      ")
print("   |  |    |  | |   _   | | |  | | |       |  BY              ")
print("   |  |    |  | |  | |  | | |__| | |  |\   |  CMD                    ")
print("   |__|    |__| |__| |__| |______| |__| \__|  v.1.1                                       ")
print(">>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
print("WARNING! USE FOR EDUCATIONAL PURPOSE ONLY!DEVELOPER IS NOT RESPONSIBLE!")
print("RUN AT YOUR OWN RISK!")
print(">>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
target_email = input("Victim email: ")
print(msg)
print("\nThats the message your victim will became")
s = input("Do you wanna change it? y/n : ")
if s == "y":
    msg = input("Your message, for new line write ENTER: ")
    while True:
        if msg.__contains__("ENTER"):
            msg += ("\n")
            msg = msg.replace("ENTER", "")
            print (msg)
            msg += input("\nNext line of the message: ")
        else:
            print(msg)
            sure = input("\nIs this the message you want to send? y/n: ")
            if sure == "y":
                sending()
            else:
                print("\n>>>>>>>>>>>>>>THE RUSSIAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
                print("Error")
                sys.exit()
else:
    sending()

                

