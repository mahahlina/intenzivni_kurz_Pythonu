sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

code = input("Zadejte kód součástku ")
if code in sklad:
    if sklad[code]:
        count = int(input("Zadejte počet součástku "))
        if count <= sklad[code]:
            print("Poptávku lze uspokojit")
            sklad[code] -= count
        else:
            print(f"lze prodat pouze {sklad[code]} kusů")
else:
    print("není součástka skladem")

print(sklad)