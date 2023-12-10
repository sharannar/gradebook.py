def avg(gradepoints):
    average = sum(gradepoints)/len(gradepoints)
    return average



def main():
    #Create a magical dictionary to store your grades
    grades = {}
    # Ask the user for grades in different subjects
    grades['English'] = int(input('Enter your English grade:'))
    grades['Math']= int(input( 'Enter your Math grade:'))
    grades ['Global Studies'] = int (input('Enger your Global Studies:'))
    grades ['Art'] = int (input('Enter your Art grade:'))
    grades ['Music'] = int (input('Enter your Music grade:'))
    #Calculate the average grade
    average_grade = sum(grades.values())/len(grades)
    #Tell the user the magical result
    gradepoints = grades.values()
    average = avg(gradepoints)
    print(f'Your average grade is:{average_grade}')
    #Cast the spell to make it work
    
    subject = input('Choose a subject to change your grade:')
    new_grade = input('What is your new' + subject + 'grade?')
    grades[subject] = int(new_grade)
    average = avg (gradepoints)
    print('Your new average is', average)
                                    
                              
                                  
                                  
    main()
