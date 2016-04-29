##Ревизия 1: Първоначална функционалност за влизане в системата
##Ревизия 2: Основно меню
##Ревизия 3: Добавяне на обява и премахване на обява
##Ревизия 4: Начало на работата по функцията за търсене
##TO-DO: "купуване", допълване на личния баланс, смяна на паролата, запис на файл, админ панел и инсталационен модул за админи

import json
from time import sleep

##Синтаксис на отделния user - потребителско име,парола,пари,контакти,предлагани услуги,история като потребител,история като продавач,админ ли е]
users = [{"name":"ivan","password":"abcd","money":500,"contact":"088 123 123","offer":[{"почистване на килими":100}], "last_bought":[],"last_sold":[],"is_admin":False},
         {"name":"dragan","password":"bcde","money":2500,"contact":"088 223 223","offer":[{"програмиране на python":200}], "last_bought":[],"last_sold":[],"is_admin":True}]
##N.B! ^Hardcoded for now

print("Добре дошли в системата за електронно търсене и предлагане на услуги!")


def login_signup():
    log_or_sign = input("Имате ли потребителско име? Ако да - натиснете L. За да се регистрирате, натиснете S ")
    log_or_sign.lower()
    if log_or_sign == "l":
        login()
    elif log_or_sign == "s":
        signup()
    else:
        print("Грешка!")
        login_signup()


def login():
    usr = input("Въведете потребителско име! ")
    usr_arr = []
    for u in range(len(users)):
        usr_arr.append(users[u]["name"])
    if usr in usr_arr:
        global globusr
        globusr = usr_arr.index(usr)
        print("Добре дошъл,",usr)
        pword = input("Въведете парола! ")
        pword.lower()
        if pword == users[usr_arr.index(usr)]["password"]:
            print("Ok!")
            main_screen()
        else:
            print("Not OK")
            login()
    else:
        print("Непознат потребител!")
        login()

def signup():
    usr = input("Въведете потребителско име!")
    for i in range(len(users)):
        if usr.lower() != users[i]["name"].lower():
            usr_pass = input("Въведете парола! ")
            usr_money = int(input("Въведете първоначален кредит! "))
            usr_contacts = input("Въведете данни за контакт! ")
            users.append({"name":usr,"password":usr_pass,"money":usr_money,"contact":usr_contacts, "offer":[], "last_bought":[],"last_sold":[],"is_admin":False})
            print("Ти си {0}, имаш {1} лева и можем да те намерим на {2}".format(usr,usr_money,usr_contacts))
            usr_arr = []
            for u in range(len(users)):
                usr_arr.append(users[u]["name"])
            if usr in usr_arr:
                global globusr
                globusr = usr_arr.index(usr)
            main_screen()
        else:
            print("Това потребителско име е заето!")
            signup()

def main_screen():
    print("ОСНОВНО МЕНЮ")
    print("(1) Моите оферти (2) Търсене (3) Потребителски профил")
    cmnd = int(input("Задайте команда (1/2/3): "))
    if cmnd == 1:
        browse_offer()
    elif cmnd == 2:
        search_offer()
    elif cmnd == 3:
        print("3")
    else:
        print("Грешка!")
        main_screen()

def browse_offer():
    iterat = 1
    for offer in users[globusr]["offer"]:
        print("({0}). {1}".format(iterat,offer))
        iterat +=1
    print("(1) Добавяне на обяви (2) Премахване на обяви")
    cmnd = int(input("Задайте команда (1/2): "))
    if cmnd == 1:
        add_offer()
    elif cmnd == 2:
        remove_offer()
    else:
        print("Грешка!")
        browse_offer()

def add_offer():
    offr = input("Разкажете какво предлагате: ")
    offr_price = int(input("Колко лева ще струва: "))
    users[globusr]["offer"].append({offr:offr_price})
    print("Към момента предлагате: ")
    iterat = 1
    for offer in users[globusr]["offer"]:
        print("({0}). {1}".format(iterat,offer))
        iterat +=1
    cmnd = int(input("Искате ли да добавите още? Да (1) или Не (2)?: "))
    if cmnd == 1:
        add_offer()
    elif cmnd == 2:
        main_screen()
    else:
        print("Грешка!")
        browse_offer()

def remove_offer():
    if len(users[globusr]["offer"]) > 0:
        iterat = 1
        for offer in users[globusr]["offer"]:
            print("({0}). {1}".format(iterat,offer))
            iterat +=1
        dell = int(input("Въведете номера на обявата, която искате да изтриете: "))
        if 0 < dell <= len(users[globusr]["offer"]):
            del users[globusr]["offer"][dell-1]
            print("Премахнато!")
            cmnd = int(input("Искате ли да премахнете още? Да (1) или Не (2)?: "))
            if cmnd == 1:
                remove_offer()
            elif cmnd == 2:
                main_screen()
            else:
                print("Грешка!")
                browse_offer()
        else:
            print("Грешка")
            remove_offer()
    else:
        print("Нямате обяви!")
        main_screen()

def search_offer():
    rzlt = False
    query = input("Какво си търсите? ")
    qlist = query.split(" ")
    for q in qlist:
        print("Вие търсите " + q)
    for i in range(0, len(users)):    
        for q in qlist:
            for o in range(0, len(users[i]["offer"])):
                for l in list(users[i]["offer"][o].keys()):
                    if q == l:
                        rzlt == True
    if rzlt == False:
        print("Нямаме съвпадение!")
    else:
        print("Имаме съвпадение!")

##def db_save():
##    pass
##def search_offers:
##    pass
##def profile_edit():
##    pass
##def admin_panel():


login_signup()


