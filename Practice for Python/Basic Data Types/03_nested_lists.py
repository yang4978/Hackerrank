#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    student = [];
    score_list = [];
    name_list = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score]);
        
        if (score not in score_list):
            score_list.append(score);
        
    score_list.sort();
        
    for i in range(len(student)):
        if(student[i][1]==score_list[1]):
            name_list.append(student[i][0]);
        
    name_list.sort();

    for i in name_list:
        print(i);


