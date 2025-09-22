age=int(input("Your Age"))
if age>18 and age<75:
   print(f"""Vote""")

else:
   print("Not vote")


score = int(input("Enter the score: "))

if score >= 90 and score <= 100:
    print("Grade: A+")
elif score >= 80 and score < 90:
    print("Grade: A")
elif score >= 70 and score < 80:
    print("Grade: B")
elif score >= 60 and score < 70:
    print("Grade: C")
elif score >= 50 and score < 60:
    print("Grade: D")
elif score >= 0 and score < 50:
    print("Grade: F")
else:
    print("Invalid score")




