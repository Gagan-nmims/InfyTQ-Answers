#lex_auth_01269441913243238467

def create_largest_number(number_list):
    #pass
    #remove pass and write your logic here
    number_list.sort()
    res = ""
    for i in number_list:
        res = str(i) + res
    return (int(res))

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)