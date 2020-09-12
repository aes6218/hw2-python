# Author: August Sanderson aes6218@psu.edu

def getGradePoint(grade):
  if grade=="A" or grade=="A+":
    p = 4.0
  elif grade=="A-":
    p = 3.67
  elif grade=="B+":
    p = 3.33
  elif grade=="B":
    p = 3.0
  elif grade=="B-":
    p = 2.67
  elif grade=="C+":
    p = 2.33
  elif grade=="C":
    p = 2.0
  elif grade=="D":
    p = 1.0
  else:
    p = 0.0
  return p

def run():
  grade = input("Enter your course 1 letter grade: ")
  g1 = getGradePoint(grade)
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {g1}")
  grade = input("Enter your course 2 letter grade: ")
  g2 = getGradePoint(grade)
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {g2}")
  grade = input("Enter your course 3 letter grade: ")
  g3 = getGradePoint(grade)
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {g3}")

  print(f"Your GPA is: {(g1*credit1 + g2*credit2 + g3*credit3)/(credit1+credit2+credit3)}")

if __name__ == "__main__":
  run()