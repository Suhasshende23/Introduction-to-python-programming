import csv

name=input("whats your name :")
home=input("where's your home")


with open("student_csv_writer.csv","a") as file:
    writer =csv.writer(file)
    writer.writerow([name,home])