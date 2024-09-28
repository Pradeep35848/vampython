#conditional statement will check the condition is true or not
#To check the condition we use if else

#WAP to check user eligible for voting
userAge  = int(input("Enter your age"))
#Note the default input function return type is string
#For vote userAge must be greater than 18
if userAge > 18:
    print("You'r eligible for voting")
else:
    print("You'r not eligible for voting")

#To check the user can sit in the first compartment in metro
userGender = input("Enter your gender")
#to check user is male or female
# if userGender == "male":
#     print("You can't sit in first compartment")
# elif userGender == "female":
#     print("You can sit in the first compartment")
# else:
#     print("you can sit any compartment")

#WAP if gender is female and age greater than 18 -> govt job apply
#else male age greater than 18 -> private job apply
if userAge > 18:
    if userGender == "male":
        print("you can apply for private job")
    elif userGender == "female":
        print("you can apply for govt job")
    else:
        print("sry there is no opening")
else:
    print("you'r under age")
