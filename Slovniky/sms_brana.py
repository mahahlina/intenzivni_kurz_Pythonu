
phone_number = input("Zadejte číslo, kam chcete zprávu zaslat ").replace(" ", "")
if phone_number.startswith("+420"):
    phone_number = phone_number.replace("+", "")
    if phone_number.isnumeric():
        sms_text = input("Zadejte zprávu, kterou chce zaslat ")
        price = len(sms_text) / 180 * 3
        print(f"zpráva bude stát {price} Kc")
    else:
        print("telefonni číslo obsahuje nejen čísla")
else: print("Zadejte spravne telefonni cislo ve formatu +420 XXX XXX XXX")

