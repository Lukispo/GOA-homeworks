middle_exam = int(input("please enter your middle exam score: "))
final_exam = int(input('please enter your final exam score: '))
project = int(input('please enter your project score: '))
average_score = (middle_exam + final_exam + project) / 3


if average_score >= 70:
    print("Score: ",average_score,  "Status: Passed")

elif average_score < 70:
    print("Score: ",average_score, "Status: Failed")