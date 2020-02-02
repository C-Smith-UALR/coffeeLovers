#Team CoffeeLovers
#CPSC 4392 Capstone
#February 1, 2020
#A class that represents an instructor for the 2020 semester.  a program to read
#data from a csv file into a class for further manipulation.

class Instructor:
    def __init__(self,**kwargs):
        # print(kwargs)
        if 'fname' in kwargs:
            self.fname = kwargs['fname']
        else:
            self.fname = ''
        if 'lname' in kwargs:
            self.lname = kwargs['lname']
        else:
            self.lname = ''
        if 'maxClassLoad' in kwargs:
            self.maxClassLoad = kwargs['maxClassLoad']
        else:
            self.maxClassLoad = 0
        if 'disciplines' in kwargs:
            self.disciplines = kwargs['disciplines']
        else:
            self.disciplines = []

    def __str__(self):
            return_string = 'My name is: %s %s\n' % (self.fname, self.lname)
            return return_string

    def convertToList(self):        #this function same as the one for AcademicClass class
        tempDisciplines = []
        if ',' in self.disciplines:
            for currDisc in self.disciplines.split(','):
                tempDisciplines.append(currDisc)
            self.disciplines = tempDisciplines

        else:
            tempDisciplines.append(self.disciplines)
            self.disciplines = tempDisciplines
        self.disciplines[-1] = self.disciplines[-1].strip()

def loadInstructors(filename, instructorList):
    with open(filename, 'rt') as file:
        next(file)  # skips the header line
        index = 0
        for line in file:
            line = line.split(',', 3)
            tempDisciplines = []
            if ',' in line[3]:
                for currDisc in line[3].split(','):
                    tempDisciplines.append(currDisc)
                line[3] = tempDisciplines
            else:
                tempDisciplines.append(line[3])
                line[3] = tempDisciplines
            line[3][-1] = line[3][-1].strip()
            instructorList.append(
                Instructor(fname=line[0], lname=line[1], maxClassLoad=line[2], disciplines=line[3]))
            index += 1
        return instructorList



# spring2020Instructors = []

# instructor_01 = Instructor(fname='Sean', lname='Orme', maxClassLoad=2, disciplines=['Programming - C++','Data Structures and Algorithms'])
# print(instructor_01)
# instructor_02=Instructor(fname='Matt')
# print(instructor_02)
# print(type(instructor_01.disciplines))
# print(instructor_01.disciplines[1])

# with open('spring2020Instructors.csv', 'rt') as file:
#     next(file) #skips the header line
#     index=0
#     for line in file:
#         line=line.split(',', 3)
#         tempDisciplines=[]
#         if ',' in line[3]:
#             for currDisc in line[3].split(','):
#                 tempDisciplines.append(currDisc)
#             line[3]=tempDisciplines
#         else:
#             tempDisciplines.append(line[3])
#             line[3]=tempDisciplines
#         line[3][-1]=line[3][-1].strip()
#         spring2020Instructors.append(Instructor(fname=line[0], lname=line[1], maxClassLoad=line[2],disciplines=line[3]))
#         # print(line)
#         print(spring2020Instructors[index])
#         index +=1
#
# print(spring2020Instructors[11].disciplines)
# print(type(spring2020Instructors[11].disciplines))
# print(spring2020Instructors[11].disciplines[2])