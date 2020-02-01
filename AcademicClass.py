#Team CoffeeLovers
#CPSC 4392 Capstone
#January 31, 2020
#A class that represents an academic class for the spring 2020 semester.


import datetime


class AcademicClass:
    #constructor
    def __init__(self,classdata):
        self.title, self.department, self.courseNo, self.days, self.beginHour, self.beginMin,\
            self.endHour,self.endMin, self.instructor, self.disciplines = classdata

    def __repr__(self):
        #this function outputs class information when print() is invoked on an object
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.title, self.department, self.courseNo, self.days, self.beginHour, self.beginMin,\
            self.endHour,self.endMin, self.instructor, self.disciplines)

    def convertToList(self):        #this function creates a list for the disciplines, since its possible
        tempDisciplines = []        #that a class has more than 1 discipline associated with it
        if ',' in self.disciplines:
            for currDisc in self.disciplines.split(','):
                tempDisciplines.append(currDisc)
            self.disciplines = tempDisciplines

        else:
            tempDisciplines.append(self.disciplines)
            self.disciplines = tempDisciplines
        self.disciplines[-1] = self.disciplines[-1].strip() #this took a while to figure out, but it
                                                            #removes the \n at the end of the line in
                                                            #the data file, which 'comes over' when you
                                                            #read in the data

    def getStartTime(self):  #function to return datetime object for start time
        return datetime.time(int(self.beginHour), int(self.beginMin))

    def getEndTime(self): #get end time
        return datetime.time(int(self.endHour), int(self.endMin))




spring2020classes = []
#list of classes

with open('spring2020Classes.csv', 'rt') as file:
    next(file) #skips the header line
    for line in file:
        spring2020classes.append(AcademicClass(line.split(',', 9)))  #creates new class object for each line in file
                                                                    #split() separates line at the ',' and passes separated
# for curClass in range(len(spring2020classes)):                      #attribute to the constructor
#     tempDisciplines = []
#     if ',' in spring2020classes[curClass].disciplines:
#         for curDisc in spring2020classes[curClass].disciplines.split(','):
#             tempDisciplines.append(curDisc)
#         spring2020classes[curClass].disciplines = tempDisciplines
#         spring2020classes[curClass].disciplines[-1] = spring2020classes[curClass].disciplines[-1].strip()
#         print(spring2020classes[curClass])
#     else:
#         tempDisciplines.append(spring2020classes[curClass].disciplines)
#         spring2020classes[curClass].disciplines = tempDisciplines
#         spring2020classes[curClass].disciplines[-1] = spring2020classes[curClass].disciplines[-1].strip()
#         print(spring2020classes[curClass])
        # spring2020classes[curClass].disciplines = spring2020classes[curClass].disciplines.strip()

    # print(curClass)

#DELETEME ^^^ above is old code before I moved it to a function within the class.  will delete eventually

for curClass in spring2020classes:
    curClass.convertToList()  #convert the disciplines attribute from string to list
    print(curClass)
    start = curClass.getStartTime()
    end = curClass.getEndTime()  #print class time.  these functions return datetime.time objects
    print('%s:%s-%s:%s' % (start.hour, start.minute, end.hour, end.minute))

