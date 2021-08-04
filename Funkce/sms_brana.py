def check_phone_number(phone_number):
    if phone_number.startswith("+420"):
        phone_number = phone_number.replace("+", "")
        if phone_number.isnumeric():
            return True
        else:
            return False


def calculate_price(sms_text):
    price = len(sms_text) / 180 * 3
    return price


phone_number = input("Zadejte číslo, kam chcete zprávu zaslat ").replace(" ", "")
if check_phone_number(phone_number):
    sms_text = input("Zadejte zprávu, kterou chce zaslat ")
    price = calculate_price(sms_text)
    print(f"zpráva bude stát {price} Kc")
else:
    print("Zadejte spravne telefonni cislo")
