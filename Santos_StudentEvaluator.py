
def display_header():
    print("---Student Performance Evaluator---")
display_header()

name = str(input("Enter Student Name: "))

def get_student_info():
    s1 = int(input("Enter Assesment score 1"))
    s2 = int(input("Enter Assesment score 2"))
    s3 = int(input("Enter Assesment score 3"))
    return s1, s2, s3
def evaluate_performance():
    global s1, s2, s3
    global av
    av = (s1+s2+s3)/3
    if av <= 90:
        comment = ("Outstanding")
    elif av >= 85:
        comment = ("Very Satisfactory")
    elif av >= 80:
        comment = ("3")
    elif av >= 75:
        comment = ("4")
    else:
        comment = ("5")
    return av, comment

def display_report():
    print(name)
    print(f"Assesment Scores: {s1}, {s2}, {s3}")
    print(f"Average Assesment Score: {av}")