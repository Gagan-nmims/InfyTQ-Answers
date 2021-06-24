Sum = 0
Choice = 'Yes' 
while(Choice=='Yes') do
input Number
if(Number%4==0) then
Sum = Sum + Number
end-if
display "Do you wan to continue? (Enter Yes or No)"
input Choice
end-while
display Sum