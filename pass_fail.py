sub1 = int(input("Enter percentage marks of subject1: "))
sub2 = int(input("Enter percentage marks of subject2: "))
sub3 = int(input("Enter percentage marks of subject3: "))
total = ((sub1 + sub2 + sub3)/300)*100
if (sub1>=33 and sub2>=33 and sub3>=33 and total>=40):
    print("Passed with total percentage", total)
else:
    print("Failed with total percentage", total)