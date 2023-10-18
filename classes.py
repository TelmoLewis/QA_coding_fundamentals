#part 1 

#class Student:
 #   def __init__(self, first, last, age):
  #      self.first = first
   #     self.last = last
    #    self.age = age

#student_1 = Student("Paul", "Richardson", 30)
#student_2 = Student("Telmo", "Lewis", 36)


#print(student_2.age)

# part 2

class Student:
    def __init__(self, first, last, age, class_="classroom"):
        self.first = first
        self.last = last
        self.age = age
        self.class_ = class_
        

    def test_score(self, score_1, score_2, score_3):
        x= (score_1 + score_2 +score_3) / 300 * 100
        return f"{self.first} {self.last} - average test score is {x:.2f}%"



student_1 = Student("Telmo", "Lewis", 36)
print(student_1.test_score(20, 40, 50))


