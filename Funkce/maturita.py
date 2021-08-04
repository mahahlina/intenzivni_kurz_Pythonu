vysledky_maturity = {"Český jazyk": 5, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1}

vysledky_maturity_dva = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]


def ohodnot_studenta(vysledky):
    sum_result = 0
    for subject in vysledky:
        sum_result += int(vysledky[subject])

    average = sum_result / len(vysledky)

    if 5 not in vysledky.values():
        if average <= 1.5 and 3 not in vysledky:
            result = "Prospěl s vyznamenáním"
        else:
            result = "Prospěl"
    else:
        result = "Neprospěl"
    return result


def create_results_of_exam(results):
    for student in results:
        name = student["Jméno"]
        del student["Jméno"]
        result = ohodnot_studenta(student)
        print(f"{name} : {result}")

create_results_of_exam(vysledky_maturity_dva)