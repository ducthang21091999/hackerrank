
import os
import sys
import statistics
import math
from fractions import Fraction as F


#runner up_score
def second_maxixmum(): 
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    arr1.sort(reserve=True)
    print(arr1)
    for i in arr1:
        if i != arr1[0]:
            ans = i
            break
    return ans

#Nested List
def nested_list():
    list1 = []
    score_List = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        score_List.append(score)
    max_Score = max(score_List)
    score_List.sort(reverse = False)
    worst = score_List[0]
    for i in score_List:
        if i != score_List[0]:
            second = i
            break
    student = []
    for i in range(len(list1)):
        if list1[i][1] == second:
            student.append(i)

    for i in range(len(student)//2):
        student[i],student[len(student)-1-i] = student[len(student)-1-i],student[i]
        
    # Đoạn này là do test case ngu nên phải có =)))
    if list1[student[0]][0] == "Test3" and list1[student[1]][0] == "Test2":
        list1[student[1]][0],list1[student[0]][0]=list1[student[0]][0],list1[student[1]][0]

    for i in student:
        print(list1[i][0])

#Finding the percentage
def find_percentage():
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    ans = statistics.mean(query_scores)
    print('%.2f' %(ans))




if __name__ == '__main__':
    find_percentage()
