#1
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0
count_books_hight_rating = 0
for book in books:
    total_pages += book["pages"]
    if book["rating"] >= 8:
        count_books_hight_rating += 1
print(f"Gustav přečetl {total_pages} stran")
print(f"Gustav dal {count_books_hight_rating} knihy hodnocení alespoň 8")



#2
schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

total_score = 0
subjects_with_score_one = []
for subject, score in schoolReport.items():
    total_score += score
    if schoolReport[subject] == 1:
        subjects_with_score_one.append(subject)

print(len(schoolReport))
avarage = total_score / len(schoolReport)
print(f"průměrna známka ze všech předmětů je {avarage}")
print(f"předměty, ve kterých získal student známku 1: {subjects_with_score_one}")



#3
plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

owners_from_plzensky_kraj = []
for number, owner in plates.items():
    if number[1] == "P":
        owners_from_plzensky_kraj.append(owner)

print(f"Majitele, jejichž vozidlo je registrováno v Plzeňském kraji: {owners_from_plzensky_kraj}")