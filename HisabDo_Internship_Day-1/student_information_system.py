# Welcome Function
def welcome():
    print("=" * 50)
    print("                  STUDENT INFORMATION SYSTEM")
    print("=" * 50)

# Function for checking Eligibility
def check_eligibility(age):
   if age >= 18:
       return "Eligible for Internship"
   else:
       return "Not Eligible"

# Function to Display Profile 
def display_profile(name,age,city,university,skills):
    print("\n")
    print("=" * 50)
    print("           STUDENT PROFILE")
    print("=" * 50)
    print(f"Name        :{name}")
    print(f"Age        :{age}")
    print(f"City        :{city}")
    print(f"University        :{university}")
    print("\nSkills: ")
    for skill in skills:
        print(f"{skill}")

    print("\nStatus:")
    print(check_eligibility(age))
    print("=" * 50)

# Main Program

welcome()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
university = input("Enter your University: ")
print("\n Enter your 3 Skills:")
skills = []
for i in range(3):
    skill = input(f"Skill {i+1}: ")
    skills.append(skill)

display_profile(name,age,city,university,skills)

print(f"Thank you {name} for using our system")

