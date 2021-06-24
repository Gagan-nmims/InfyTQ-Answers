Sum = 0
input number
temp = number
while(number! = 0) Do
remainder = number % 10
Sum = Sum + remainder * remainder *remainder
Number = Number / 10
end-while
if(Temp == Sum) then
display "This is Armstrong Number"
else
display "This is not an Armstrong Number"
end-if