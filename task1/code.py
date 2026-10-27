
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def check_eligibility(student):
    reasons = []

    if not student["subjects"]:
        reasons.append("No subject marks provided")
    elif any(mark < 0 or mark > 100
             for mark in student["subjects"]):
        reasons.append("Invalid subject marks")
    elif student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if student["subjects"] and any(
        mark < MIN_SUBJECT_MARKS or mark > 100
        or mark < 0 for mark in student["subjects"]
    ):
        reasons.append("Subject marks must be at least 40%")

    if not 0 <= student["attendance"] <= 100:
        reasons.append("Invalid attendance")
    elif student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] < 0:
        reasons.append("Invalid family income")
    elif student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 250000")

    return reasons


def ranking_key(student):
    # Negative values sort higher scores first.
    return (
        -student["aggregate"],
        -student["priority_subject"],
        -student["attendance"],
        student["income"],
        student["application_order"],
        student["id"]
    )


def allocate_scholarships(students, quota):
    if quota < 0:
        raise ValueError("Scholarship quota cannot be negative")

    eligible = []
    rejected = []

    for student in students:
        reasons = check_eligibility(student)

        if not reasons:
            eligible.append(student)
        else:
            rejected.append((student, reasons))

    eligible.sort(key=ranking_key)
    winners = eligible[:quota]

    return eligible, winners, rejected


def main():
    students = []
    n = int(input("Enter number of applicants: "))
    quota = int(input("Enter available scholarships: "))

    if n < 0 or quota < 0:
        print("Applicant count and quota cannot be negative.")
        return

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        student_id = int(input("Student ID: "))
        name = input("Student name: ")
        count = int(input("Number of subjects: "))

        if count <= 0:
            print("Number of subjects must be positive.")
            return

        marks = [
            float(input(f"Marks in subject {j + 1}: "))
            for j in range(count)
        ]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Marks must be between 0 and 100.")
            return

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income (Rs.): "))

        if not 0 <= attendance <= 100 or income < 0:
            print("Invalid attendance or income.")
            return

        students.append({
            "id": student_id,
            "name": name,
            "subjects": marks,
            "aggregate": sum(marks) / len(marks),
            "priority_subject": marks[0],
            "attendance": attendance,
            "income": income,
            "application_order": i + 1
        })

    eligible, winners, rejected = allocate_scholarships(
        students, quota
    )

    print("\n--- FINAL RANKING ---")
    if not eligible:
        print("No eligible applicants.")

    for rank, student in enumerate(eligible, start=1):
        print(
            f"{rank}. {student['name']} "
            f"(ID: {student['id']}) - "
            f"Aggregate: {student['aggregate']:.2f}%"
        )

    print("\n--- SCHOLARSHIP RECIPIENTS ---")
    if not winners:
        print("No scholarships awarded.")

    for student in winners:
        print(f"{student['id']} - {student['name']}")

    print("\n--- INELIGIBLE APPLICANTS ---")
    if not rejected:
        print("None")

    for student, reasons in rejected:
        print(f"{student['name']}: {'; '.join(reasons)}")


if __name__ == "__main__":
    main()

