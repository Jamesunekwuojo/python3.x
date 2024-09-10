from statistics import *

def Login():
    username = input("Enter your username: ")

    password = input("Password:")

    if username == 'python' and password == 999: 
        print("Welcome, " + username + "!")

        def operatopnTemp():

            print("Welcome to Grade Central") # welcome message after a successful login

            print(""" 
                  [1]- Enter Grades
                  [2]- Remove Student
                  [3]- Student Average
                  [4]= Exit
            
            """)
        
        def operationPrompt():
            operation = input("What would you like to do today?(Enter a number) ") 

            studentName = input("Enter Student Name: ")

            Grade = input('Grade:')



            

            if operation == 1:
                def EnterG():
                   

                    gradeDic = {f"{studentName}: {Grade}"}

                    print('Adding Grade ...')

                    print(gradeDic)

                    return studentName, Grade, gradeDic
            
            elif operation == 2 :
                def RemoveStd():
                    removeByName = input("What student to remove? :")

                    del gradeDic[f"{studentName}"]


    
    else :
        print("Invalid username")

        
    