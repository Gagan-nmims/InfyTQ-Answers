Scholarship = 0
for (Counter = 1, Counter <= 500, Counter = Counter + 1)
input Branch_Of_Study, Score, Course_Fee
if (Branch_Of_Study=="Arts") then
if (Score >= 90) then
Scholarship = 50
else if(Score % 2!=0)
Scholarship = 5
end-if
else if(Branch_Of_Study == "Engineering") then
if (Score > 85) then
Scholarship = 50
else if(Score % 7 == 0) then
Scholarship = 5
end-if
end-if
Scholarship_Amount = Course_Fee * Scholarship / 100
Final_Fee = Course_Fee - Scholarship_Amount
display Final_Fee
end-for
