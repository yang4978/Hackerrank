#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_score = 0

    for i in student_marks[query_name]:
        sum_score += i; 
    
    aver = sum_score/3;

    print("%.2f" %aver);

