marks=int(input("Enter marks out of 100:"))
if marks>=90 and marks<95:
    print(f"Grade=A (marks={marks})")
elif marks>=80 and marks<90:
    print(f"Grade=B (marks={marks})")
elif marks>=70 and marks<80:
    print(f"Grade=C (marks={marks})")
elif marks>=60 and marks<70:
    print(f"Grade=D (marks={marks})")
else:
    print(f"Grade=E")