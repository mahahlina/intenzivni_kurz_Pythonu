import wget
import pandas

names = pandas.read_csv("jmena.csv")
students1 = pandas.DataFrame(pandas.read_csv("studenti1.csv")).dropna()
students2 = pandas.DataFrame(pandas.read_csv("studenti2.csv")).dropna()

all_students = pandas.concat([students1, students2])
not_students = all_students["kruh"].isna()

studens_by_obor = all_students.groupby("obor")
count_students_by_obor = studens_by_obor["jméno"].count()

av_result_students_by_obor = studens_by_obor["prospěch"].mean()

#print(all_students.columns)
#print(all_students.head())
#print(not_students.sum())
#print(av_result_students_by_obor)
#print(names.head())

new_all_student = pandas.merge(all_students, names)

print(new_all_student.columns)

men_in_it = new_all_student[new_all_student["pohlaví"] == "m"]
womens_in_it = new_all_student[new_all_student["pohlaví"] == "ž"]
print(f"Womens: {womens_in_it['jméno'].count()}, Men: {men_in_it['jméno'].count()}")