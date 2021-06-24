#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here

                
    if (num1 + num2<=num3 or num2+num3<=num1 or num3+num1<=num2):
        return failure
    else:
        return success
    

    #Use the following messages to return the result wherever necessary
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)