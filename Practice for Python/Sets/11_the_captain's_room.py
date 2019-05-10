#https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    K = int(input());
    room_number = list(map(int,input().split()));
    member = set(room_number);
    print ((sum(member)*K-sum(room_number))//(K-1))
