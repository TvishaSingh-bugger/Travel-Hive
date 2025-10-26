def askQues(currentUser):
  ques=input("Enter your Question:")
  with open("question.txt","a") as f:
    f.write(f"{currentUser},{ques},\n")
  print("Question Added!")

def ansQues():
  try:
    with open("question.txt","r") as f:
      lines=f.readlines()
    if not lines:
      print("No questions yet!")
      return
    
    n=1
    for line in lines:
      if line.startswith("QuesNo:"):
        continue
      part=line.split(",",1)
      user,ques=part
      print(f"{n}.{ques.strip()}")
      n=n+1
    qno=int(input("Enter question number to answer:"))
    answer=input("Enter your answers:")
    with open("question.txt","a") as f:
      f.write(f"QuesNo:{qno}:{answer}\n")
    print("Answer added successfully!")
  except:
    print("No questions found!")


def viewQuestion():
  try:
    with open("question.txt","r") as f:
      lines=f.readlines()
    if not lines:
      print("No question found!")
      return
    for line in lines:
      print(line,end="")
  except:
    print("No questions found!")
