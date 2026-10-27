# University Scholarship Allocation System

## 1. Problem Statement
1. University Scholarship Allocation: Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules. 

## 2. Algorithm

1. Start.
2. Read the number of applicants and available scholarships.
3. For each applicant, input student ID, name, subject marks, attendance, annual family income, and application order.
4. Calculate aggregate marks as the average of subject marks.
5. Check all eligibility conditions.
6. If any condition fails, mark the applicant as ineligible and record the reason.
7. Otherwise, add the applicant to the eligible list.
8. Sort eligible students using these priorities:
   - Higher aggregate marks.
   - Higher priority-subject marks.
   - Higher attendance.
   - Lower annual family income.
   - Earlier application order.
   - Lower student ID.
9. Award scholarships to the top-ranked eligible students, up to the available quota.
10. Display the ranking, scholarship recipients, and rejected applicants.
11. Stop.

## 3. Flowchart


## 5. Sample Input

Example run with four applicants and two scholarships:

text

```
Enter number of applicants: 4
Enter available scholarships: 2

Applicant 1
Student ID: 101
Student name: Ananya
Number of subjects: 3
Marks in subject 1: 92
Marks in subject 2: 88
Marks in subject 3: 90
Attendance percentage: 95
Annual family income (Rs.): 180000

Applicant 2
Student ID: 102
Student name: Rahul
Number of subjects: 3
Marks in subject 1: 87
Marks in subject 2: 82
Marks in subject 3: 86
Attendance percentage: 90
Annual family income (Rs.): 200000

Applicant 3
Student ID: 103
Student name: Priya
Number of subjects: 3
Marks in subject 1: 75
Marks in subject 2: 65
Marks in subject 3: 70
Attendance percentage: 90
Annual family income (Rs.): 150000

Applicant 4
Student ID: 104
Student name: Kiran
Number of subjects: 3
Marks in subject 1: 90
Marks in subject 2: 35
Marks in subject 3: 89
Attendance percentage: 98
Annual family income (Rs.): 100000
```

## 6. Sample Output

text

```
--- FINAL RANKING ---
1. Ananya (ID: 101) - Aggregate: 90.00%
2. Rahul (ID: 102) - Aggregate: 85.00%

--- SCHOLARSHIP RECIPIENTS ---
101 - Ananya
102 - Rahul

--- INELIGIBLE APPLICANTS ---
Priya: Aggregate marks below 75%
Kiran: Subject marks must be at least 40%
```



