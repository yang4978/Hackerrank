#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    arr = [];
    for _ in range(N):
        arr_temp = input().strip().split();
        if(arr_temp[0]=="insert"):
            arr.insert(int(arr_temp[1]),int(arr_temp[2]));
        elif(arr_temp[0]=="print"):
            print(arr);
        elif(arr_temp[0]=="remove"):
            arr.remove(int(arr_temp[1]));
        elif(arr_temp[0]=="append"):
            arr.append(int(arr_temp[1]));
        elif(arr_temp[0]=="sort"):
            arr.sort();
        elif(arr_temp[0]=="pop"):
            arr.pop();
        elif(arr_temp[0]=="reverse"):
            arr.reverse();
