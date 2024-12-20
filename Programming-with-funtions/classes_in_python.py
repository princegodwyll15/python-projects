class Instructor:
    def __init__(self, f_name, l_name) -> None:
        self.instructor_fname = f_name
        self.instructor_lname = l_name

    def display(self, age):
        print(f"{self.instructor_fname} is {age} years old")
    
    def course_of_instructor(self):
        course_dict = {
            "001": "ICT",
            "002": "RME",
            "003": "Business",
            "004": "General Arts",
            "005": "Visual Arts"       
        }

        course_id = input('Please what is the course ID: ')
        if course_id in course_dict:
            course = course_dict[course_id]
            print(f"The course id you inputed is been taught by: {self.instructor_fname} {self.instructor_lname}")
            print(f"And the course is {course}")

Instructor_1 = Instructor("Prince", "Godwyll")
Instructor_1.display(2)
Instructor_1.course_of_instructor()


Instructor_2 = Instructor("Prince", "Godwyll")
Instructor_2.display(2)
Instructor_2.course_of_instructor()

