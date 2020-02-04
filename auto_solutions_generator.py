import itertools


class Course:
    def __init__(self, course_number, course_title, course_days, course_time, course_discipline):
        self.courseNumber = course_number
        self.courseTitle = course_title
        self.courseDays = course_days
        self.courseTime = course_time
        self.courseDiscipline = course_discipline


class Instructor:
    def __init__(self, last_name, max_load, discipline_area):
        self.lastName = last_name
        self.maxLoad = max_load
        self.disciplineArea = discipline_area


def get_schedule_criteria():
    days = ['MW', 'TR']
    times = ['08:00 AM - 09:15 AM', '09:25 AM - 10:40 AM', '10:50 AM - 12:05 PM', '12:15 PM - 01:30 PM',
             '01:40 PM - 02:55 PM', '03:05 PM - 04:20 PM', '04:30 PM - 05:45 PM']
    disciplines = ['Programming - C++', 'Programming - Python', 'Game Development', 'Data Structures and Algorithms',
                   'Computer Organization', 'Operating Systems', 'Programming Languages', 'Cybersecurity',
                   'Mobile Applications', 'Artificial Intelligence', 'Networks', 'Theory of Computation',
                   'Parallel and Distributed Systems']

    course1 = Course('CPSC 3300', 'Python Programming I', days[0], times[1], [disciplines[1], disciplines[9]])
    course2 = Course('CPSC 3301', 'Game Design         ', days[1], times[0], [disciplines[2], disciplines[9]])
    course3 = Course('CPSC 3302', 'AI                  ', days[0], times[1], [disciplines[9]])
    course4 = Course('CPSC 3303', 'Computer Security   ', days[1], times[2], [disciplines[7]])
    course5 = Course('CPSC 3304', 'Mobile Apps         ', days[0], times[4], [disciplines[8]])

    instructor1 = Instructor('Lovell', 2, [disciplines[7], disciplines[9]])
    instructor2 = Instructor('Smith', 2, [disciplines[8], disciplines[9]])
    instructor3 = Instructor('McKee', 1, [disciplines[9]])

    courses = [course1, course2, course3, course4, course5]
    instructors = [instructor1, instructor2, instructor3]

    return days, times, courses, instructors


def get_course_schedule(days, times, courses):
    scheduled_courses = []
    for day in days:
        for time in times:
            for course in courses:
                if course.courseDays == day and course.courseTime == time:
                    scheduled_courses.append(course)

    return scheduled_courses


def get_valid_instructor_combinations(instructors):
    all_instructor_combinations = list(itertools.product(instructors, repeat=5))

    invalid_instructor_combinations = []
    for combination in all_instructor_combinations:
        for instructor in instructors:
            if combination.count(instructor) > instructor.maxLoad:
                invalid_instructor_combinations.append(combination)

    instructor_combinations = [list(x) for x in all_instructor_combinations if x not in invalid_instructor_combinations]

    return instructor_combinations


def compare_two_lists(course_disciplines, instructor_disciplines):
    for discipline in course_disciplines:
        if discipline in instructor_disciplines:
            return True

    return False


def get_auto_solutions(instructor_combinations, scheduled_courses):
    all_auto_solutions = []
    for combination in instructor_combinations:
        solution = [(i, j) for i, j in zip(scheduled_courses, combination) if compare_two_lists(i.courseDiscipline, j.disciplineArea)]
        if len(solution) == len(scheduled_courses):
            all_auto_solutions.append(solution)

    invalid_auto_solutions = []
    for solution in all_auto_solutions:
        for i in range(len(solution) - 1):
            for j in range(i + 1, len(solution)):
                if solution[i][0].courseDays == solution[j][0].courseDays and solution[i][0].courseTime == \
                        solution[j][0].courseTime and solution[i][1].lastName == solution[j][1].lastName:
                    invalid_auto_solutions.append(solution)
                    break
            break

    auto_solutions = [x for x in all_auto_solutions if x not in invalid_auto_solutions]

    return auto_solutions


def show_auto_solutions(auto_solutions):
    if len(auto_solutions) == 0:
        print('There are no valid schedules.')
    else:
        for i in range(len(auto_solutions)):
            print('Schedule #' + str(i + 1) + ':')
            for j in range(len(auto_solutions[i])):
                print(auto_solutions[i][j][0].courseNumber + '\t' + auto_solutions[i][j][0].courseTitle + '\t' +
                      auto_solutions[i][j][0].courseDays + '\t' + auto_solutions[i][j][0].courseTime + '\t' +
                      auto_solutions[i][j][1].lastName)
            print('')

    return


def main():
    days, times, courses, instructors = get_schedule_criteria()
    scheduled_courses = get_course_schedule(days, times, courses)
    instructor_combinations = get_valid_instructor_combinations(instructors)
    auto_solutions = get_auto_solutions(instructor_combinations, scheduled_courses)
    show_auto_solutions(auto_solutions)
    return


if __name__ == '__main__':
    main()
