class Instructor:
    def __init__(self) -> None:
        pass
    def course_of_instructor(self):
        COUSRSE_NAME_INDEX = 0
        NAME_OF_INSTRUCTOR_INDEX = 1
        instructor_data = {
            #key, subject index, name of instructor-index
            "001": ["ICT", "Prince Godwyll"],
            "002": ["RME", "Kelvin Essiaw"],
            "003": ["Business", "Ebenezer Essiaw"],
            "004": ["General Arts", "Guyreth Obeng"],
            "005": ["Visual Arts" , "Bridget Nyarko"]      
        }

        course_id = input('Please what is the course ID: ')
        if course_id in instructor_data:
            instructor_info = instructor_data[course_id]
            course_of_instructor = instructor_info[0]
            name_of_instructor = instructor_info[1]
            print(f"The name of the instructor assocaited with {course_id} is: {name_of_instructor.upper()}")
            print(f"The name of the course been thought by {name_of_instructor.upper()} is: {course_of_instructor.upper()}")


Instructor_1 = Instructor()
Instructor_1.course_of_instructor()
print()


Instructor_2 = Instructor()
Instructor_2.course_of_instructor()

