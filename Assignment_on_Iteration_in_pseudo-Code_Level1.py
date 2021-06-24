Reverse = 0
input Number
Temp = Number
while(Number!=0) do
Remainder = Number%10
Reverse = Reverse*10+Remainder
Number = Number/10
end-while
if(Temp==Reverse) then
display "Palindrome"
else
display "Not a Palindrome"
end-if