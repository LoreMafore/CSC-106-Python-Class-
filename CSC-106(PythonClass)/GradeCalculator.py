while True:
    # 1.Class Attendence
    ca = float(input("What is your Class Attendence Score? "))
    if ca > 120 or ca < 0:
        print("Inavlid Answer. Try Again")

    # 2.Quizzes
    quiz = float(input("What is your Quiz Score? "))
    if quiz > 120 or quiz < 0:
        print("Inavlid Answer. Try Again")

    # 3.Lab Assignments
    la = float(input("What is your Lab Assignments Score? "))
    if la > 120 or la < 0:
        print("Inavlid Answer. Try Again")

    # 4.Programming Assignments
    pa = float(input("What is your Programming Assignments Score? "))
    if pa > 120 or pa < 0:
        print("Inavlid Answer. Try Again")

    # 5.Examinations
    exam = float(input("What is your Exam Score? "))
    if exam > 120 or exam < 0:
        print("Inavlid Answer. Try Again")

    # Your Overall Grade
    grade = ca * .10 + quiz * .15 + la * .15 + pa * .30 + exam * .30

    # Finding what your grade level is
    if grade >= 92:
        print("You have an A , your class grade is", grade)
        break

    elif grade == 90 or grade == 91:
        print("You have an A-, your class grade is", grade)
        break

    elif grade == 88 or grade == 89:
        print("You have an B+, your class grade is", grade)
        break

    elif grade >= 82 and grade <= 87:
        print("You have an B, your class grade is", grade)
        break

    elif grade == 80 or grade == 81:
        print("You have an B-, your class grade is", grade)
        break

    elif grade == 78 or grade == 79:
        print("You have an C+, your class grade is", grade)
        break

    elif grade >= 72 and grade <= 77:
        print("You have an C, your class grade is", grade)
        break

    elif grade == 70 or grade == 71:
        print("You have an C-, your class grade is", grade)
        break

    elif grade == 68 or grade == 69:
        print("You have an D+, your class grade is", grade)
        break

    elif grade >= 62 and grade <= 67:
        print("You have an D, your class grade is", grade)
        break

    elif grade == 60 or grade == 61:
        print("You have an D-, your class grade is", grade)
        break

    elif grade <= 59:
        print("You have an F, your class grade is", grade)
        break