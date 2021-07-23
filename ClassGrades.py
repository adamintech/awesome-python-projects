print(
'''*'-.-'*'-.-'*'-.-'*'--'*
    Project: Unit_03 
     Version: 5.0 
  Author: Adam Berman
 Email: uhicfii@gmail.com
  Date: July 21st, 2021
*'-.-'*'-.-'*'-.-'*'--'*''')
print("." * 25)
print()
print()

#--------------------#

# grade = input("Enter the score you recieved on the final exam: (1-100)")

finalGrade = int(input("What was your score on the final exam (1-100)?"))
if finalGrade >=90 and finalGrade <=100:
    message = "A"
elif finalGrade >=80 and finalGrade <=89:
    message = "B"
elif finalGrade >=70 and finalGrade <=79:
    message = "C"
elif finalGrade >=60 and finalGrade <=69:
    message = "D"
elif finalGrade <=59:
    message = "F"    
else:
    message = "You must enter a number between 1 and 100"

import random
billyScore = random.randint(61,100)

billyGrade = billyScore
if billyGrade >=90 and billyGrade <=100:
    message1 = "A"
elif billyGrade >=80 and billyGrade <=89:
    message1 = "B"
elif billyGrade >=70 and billyGrade <=79:
    message1 = "C"
elif billyGrade >=60 and billyGrade <=69:
    message1 = "D"
elif billyGrade <=59:
    message1 = "F"   


# gradeStudent = finalGrade % 10
# if gradeStudent >=5 and finalGrade >=60:
#   message3 = "+"
# elif gradeStudent <=4 and finalGrade >=60:
#   message3 = "-"  

if finalGrade >= 60:
    studentPlus = finalGrade % 10
    if studentPlus >=5:
        message3 = "+"
    elif studentPlus <=4:
        message3 = "-"
else:
    message3 = " "

# billyPlus = billyGrade % 10
# if billyPlus >=5 and billyGrade >=60:
#   message4 = "+"
# elif billyPlus <=4 and billyGrade >=60:
#   message4 = "-"    

if billyGrade >= 60:
    billyPlus = billyGrade % 10
    if billyPlus >=5:
        message4 = "+"
    elif billyPlus <=4:
        message4 = "-" 

print(f"You earned a score of {message}{message3}in this class. Of course Billy the loudmouth \
managed to obtain a score of {billyScore}, granting him a grade of {message1} {message4}. Let's all applaud Billy <silent clap>")