from Models.Person import Person

class Teacher(Person):
    def __init__(self, fname, lname, bdate, phone, email, degree, subject):
        super().__init__(fname, lname, bdate, phone, email)
        self.degree = degree
        self.subject = subject

    def __str__(self):
        return f"""
                {super().__init__(self)}
                Degree: {self.degree}
                Subject: {self.subject}
                """