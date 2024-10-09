res = True
while res is True:
    # Validating the Student Name
    while True:
        sname = input('Enter Student Name: ')
        # Splitting the string into words
        words = sname.split()
        name = True
        for word in words:
            if not word.isalpha():
                name = False
                break
        if name:
            break
        else:
            print(f'{sname} is an invalid name. Try again..')

    # Validating the Roll Number
    while True:
        try:
            sno = int(input('Enter Student Roll Number: '))
            if sno in range(100, 201):
                break
            else:
                print(f'{sno} is invalid. Try again..')
        except ValueError:
            print("Don't enter alnums, strs and symbols for Roll Number.")

    subjects = ['C Language', 'C++', 'Java', 'Python'] # List of subjects

    marks = {} # Dictionary to store marks for each subject

    # Validating marks for each subject
    for subject in subjects:
        while True:
            try:
                # Input for subject marks
                mark = int(input(f'Enter the marks obtained in {subject}: '))
                if mark in range(0, 101):
                    marks[subject] = mark  # Store the marks in the dictionary
                    break
                else:
                    print(f'{mark} is invalid marks in {subject}. Try again..')
            except ValueError:
                print(f'Invalid input. Please enter numeric marks for {subject}.')

    # Calculating the total marks and percentage
    tot = sum(marks.values())
    percentage = (tot / 400) * 100

    # Check if the student has failed in any subject (marks below 40)
    if all(mark >= 40 for mark in marks.values()):
        if tot in range(320, 401):
            grade = 'excellent'.upper()
            if all(mark >= 60 for mark in marks.values()):
                grade = 'distinction'.upper()
        elif tot in range(280, 320):
            grade = 'first'.upper()
        elif tot in range(200, 280):
            grade = 'second'.upper()
        elif tot in range(160, 200):
            grade = 'third'.upper()
    else:
        grade = 'fail'.upper()

    # Display the Student Record
    print('\n\t\tThe Student Progress Report'.upper())
    print('-' * 50)
    print(f'Student Name: {sname}')
    print(f'Student Roll Number: {sno}')

    # Display the Student Marks Report
    for subject, mark in marks.items():
        print(f'Student marks in {subject}: {mark}')
    print(f'Total Marks: {tot}')
    print(f'Percentage: {percentage:.2f}%')
    print(f'Grade: {grade}')
    print('#' * 50)
    # Ask if the user wants to input another student's info
    ch = input('Do you want to enter another Student info (Yes/No): ')
    if ch.lower() == 'yes':
        res = True
    else:
        res = False
else:
    print('Thanks for using the application. Bye..')
