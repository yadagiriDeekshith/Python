class StudentDetails:
    def __init__(self,marks):
        self.marks=marks
    def HighestScore(self):
        max_score=max(self.marks.values(), key=lambda student: student.get("maths"))
        Higest_marks=[student for student,scores in self.marks.items() if scores["maths"] == max_score["maths"]]
        return Higest_marks
marks={
    "Siva":{"science":68,"maths":70},
    "venkat":{"science":88,"maths":80},
    "Anu":{"science":62,"maths":82},
    "Raju":{"science":64,"maths":71},
    "Venkat":{"science":64,"maths":82}
    }
student_marks=StudentDetails(marks)
Higest_marks=student_marks.HighestScore()
result=",".join(Higest_marks)
print(result)
