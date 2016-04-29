class User:
    def __init__(self, name, password, money, contact, offers, history_buy, history_sell):
        self.name = name
        self.password = password
        self.money = money
        self.contact = contact
        self.offers = offers
        self.history_buy = history_buy
        self.history_sell = history_sell

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

def signup():
    usr_name = input("Въведете потребителско име! ")
    usr_password = input("Въведете парола: ")
    usr_money = input("Въведете първоначална наличност: ")
    usr_contact = input("Въведете данни за контакт: ")
    usr_offers = []
    usr_history_buy = []
    usr_history_sell = []
    User(usr_name, usr_password, usr_money, usr_contact, usr_offers, usr_history_buy, usr_history_sell)
    
login_signup()

