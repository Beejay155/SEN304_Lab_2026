def calculate_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def main():
    try:
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        

        grade = calculate_grade(score)

        print("\nStudent Result")
        print("----------------")
        print(f"Name : {name}")
        print(f"Score: {score}")
        print(f"Grade: {grade}")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()