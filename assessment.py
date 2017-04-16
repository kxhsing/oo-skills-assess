"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Abstraction - Object orientation allows abstraction, which means as 
   programmers we can hide all the unnecessary information in our code and only 
   use the relevant parts when needed to increase efficiency. As other people 
   reuse our code, they won't need to see all the extraneous details of for 
   example the info used in a method inside a class. This makes for cleaner code.

   2. Encapsulation - Encapsulation means that data and methods of a class are 
   contained (or encapsulated), which in turn makes it easier to read, use, and 
   debug code because relevant methods and info are in close proximity of another.

   3. Polymorphism - When you create classes, they can inherit from one another 
   (e.g., a child class can inherit from a parent class), which means that the
   different components of code that would have otherwise overlapped can be 
   interchangeable and reused. For example, when a method or attribute is 
   defined in a parent class, when a child class is created, it automatically 
   inherits the method and attribute in the parent class, unless it would like 
   to overwrite it. Polymorphism reduces repetition in the code and makes it 
   easy to recycle code without the extra steps of typing them over and over again.

2. What is a class?
   A class is a type of thing. It can hold attributes and methods, and can be 
   instantiated with individual "copies" (or instances) of itself. Its attributes 
   and methods can also be inherited by other classes to be used/called upon.

3. What is an instance attribute?
   An instance attribute is set directly on an object/instance of a class. Its 
   value will not change if the class attribute value is changed.

4. What is a method?
   A method is a function defined inside a class. A method works like how a 
   function would outside the class.

5. What is an instance in object orientation?
   An instance in object orientation is an individual occurence of a class. It 
   is a copy of a class. For example, "hello" is an instance of the string class.

6. How is a class attribute different than an instance attribute?
   A class attribute is an attribute defined in a class, which will be inherited
   by instances of it and all its child classes and their instances. A change
   in a class attribute would cause a change in that attribute in all its instances. 
   We would use a class attribute when we know that all instances of it will have this 
   attribute, for example, all mammals have vertebrates, so a vertebrate attribute
   can be used in a Mammal class.

   An instance attribute is an attribute set directly on the instance of a class, 
   and is often only applicable to the instance itself, is different from other
   instances of that same class, and might change for just that instance. 
   An example would be the hobbies of a person who is an instance of a Human class. 
   A change in the instance attribute will not apply to the other instances of 
   the same class.

"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
   def __init__(self, first_name, last_name, address):
      self.first_name = first_name
      self.last_name = last_name
      self.address = address
      # self.student_data()

   def __repr__(self):
      return "{%s: %s,\n %s: %s,\n %s: %s}" %(
                                                "first_name", self.first_name, 
                                                "last_name", self.last_name, 
                                                "address", self.address
                                                   )

   def store_info(self):
      student_dict = {
                     "first_name": self.first_name, 
                     "last_name": self.last_name, 
                     "address": self.address
      }
      return student_dict


class Question(object):
   def __init__(self, question, correct_answer):
      self.question = question
      self.correct_answer = correct_answer

   def __repr__(self):
      return "{%s: %s,\n %s: %s}" % ("question", self.question, 
                                    "correct_answer", self.correct_answer)

   def store_question(self, question, correct_answer):
      question_dict = {
                        "question": question,
                        "correct_answer": correct_answer
                        }
      return question_dict

   def ask_and_evaluate(self, question, correct_answer):
      print self.question
      user_answer = raw_input(">> ")
      if user_answer == self.correct_answer:
         return True
      else:
         return False


class Exam(Question):
   def __init__(self, name):
      # super(Exam, self).__init__
      self.name = name
      self.questions = []


   def __repr__(self):
      return "{%s: %s,\n %s: %s}" % ("name", self.name, 
                                    "questions", self.questions)


   def store_exam(self):
      exam_dict = {
                        "name": self.name,
                        "questions": self.questions
                        }

      return exam_dict


   def add_question(self, question, correct_answer):
      new_question = super(Exam, self).store_question(question, correct_answer)
      self.questions.append(new_question)


   def administer(self):
      score = []
      for indiv_question in self.questions:
         self.correct_answer = indiv_question['correct_answer']
         self.question = indiv_question['question']

         question_score = super(Exam, self).ask_and_evaluate(self.question, self.correct_answer)

         if question_score == True:
            score.append(1.0)
         else:
            score.append(0)

      total = 0
      for num in score:
         total += num

      score_average = float(total) / len(score)

      return score_average * 100.0








