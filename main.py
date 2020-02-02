#Team CoffeeLovers
#CPSC 4392 Capstone
#February 1, 2020
#A main function for working out the algorithm for the application.

from Instructor import Instructor, loadInstructors
from AcademicClass import AcademicClass, loadClasses

instructorFile = 'spring2020Instructors.csv'
classFile = 'spring2020Classes.csv'

spring2020Instructors = []
spring2020Classes = []

spring2020Instructors=loadInstructors(instructorFile,spring2020Instructors)
spring2020Classes=loadClasses(classFile,spring2020Classes)

def isQualified(instructorDisciplines,classDisciplines):  #tells you if an instructor is qualified
    intersectionList=[disc for disc in instructorDisciplines if disc in classDisciplines]
    if not intersectionList:
        return False
    else:
        return True

#demonstrates that Matt Kennett not qualified to teach Game Development
print(isQualified(spring2020Instructors[11].disciplines, spring2020Classes[9].disciplines))

#demonstrates that Prof Milanova is qualified to teach AI
print(isQualified(spring2020Instructors[9].disciplines, spring2020Classes[6].disciplines))

