#lex_auth_012693819159732224162

def check_palindrome(word):
    #pass
    #Remove pass and write your logic here
    if ( word == word[::-1]):
        return 1
    else:
        return 0
    

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")