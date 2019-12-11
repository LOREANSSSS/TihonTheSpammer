import smtplib


email_provider = 'smtp.gmail.com' 
email_address = "tihonthespammer@gmail.com" 
email_port = 587 
password = "dontchangeplease"
msg = "\nThis is SPAM" 
spam20 = 20 
spam50 = 50
spam100 = 100
spam1000 = 1000

def sending():
    print(" ________   __   __   __   ______   __   __                             ")
    print("|__    __| |  | |  | |  | |  __  | |  \ |  |                    ")
    print("   |  |    |  | |  |_|  | | |  | | |   \|  |                      ")
    print("   |  |    |  | |   _   | | |  | | |       |                 ")
    print("   |  |    |  | |  | |  | | |__| | |  |\   |                      ")
    print("   |__|    |__| |__| |__| |______| |__| \__| v.1.0                                       ")
    print(">>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
    print("\nPlease, choose amount of Emails you want to send: \n[20]  [50]  [100]  [1000]")
    print("Example: 50")
    amount = input("Your choise: ")
    print(msg)
    print("Thats the message your victim will became")
    print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
    if amount == "20":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam20):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam20))
        server.quit()

    elif amount == "50":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam50):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam50))
        server.quit()

    elif amount == "100":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam100):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam100))
        server.quit()

    elif amount == "1000":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam100):
            server.sendmail(email_address,target_email,msg)
            print("Sent {}".format(_))
        print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Messages were sent to your victim".format(spam1000))
        server.quit()

    else:
        print("error")


print(" ________   __   __   __   ______   __   __                             ")
print("|__    __| |  | |  | |  | |  __  | |  \ |  |                    ")
print("   |  |    |  | |  |_|  | | |  | | |   \|  |                      ")
print("   |  |    |  | |   _   | | |  | | |       |  BY              ")
print("   |  |    |  | |  | |  | | |__| | |  |\   |  CMD                    ")
print("   |__|    |__| |__| |__| |______| |__| \__|  v.1.0                                       ")
print(">>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
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
                print("\n>>>>>>>>>>>>>>THE RUSSIANN SPAMMER<<<<<<<<<<<<<<<<                        ")
                print("Error")
else:
    sending()

                

