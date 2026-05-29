    # Day 9: Conditionals Practice - Grading System
    
    # 1. Basic if-else
    age = 18
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are too young to vote.")
    
    # 2. The if-elif-else ladder
    score = 85
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Your score is {score}, which is a grade: {grade}")
    
    # 3. Logical Operators (and, or)
    is_weekend = True
    is_sunny = False
    
    if is_weekend and is_sunny:
        print("Let's go to the beach!")
    elif is_weekend and not is_sunny:
        print("It's the weekend, but maybe stay inside and code.")
    else:
        print("It's a workday, back to the office!")
    
    # 4. Nested Conditionals
    # Checking if a number is positive and then if it is even
    number = 10
    
    if number > 0:
        print("The number is positive.")
        if number % 2 == 0:
            print("It is also an even number.")
        else:
            print("It is an odd number.")
    else:
        print("The number is not positive.")
