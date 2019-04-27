#https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    for _ in range(int(input())):
        a,b = input().split()
        try:
            print(int(a)//int(b))
        # except ValueError as e:
        #     print('Error Code:',e)
        # except ZeroDivisionError as e:
        #     print('Error Code:',e)
        except Exception as e:
            print('Error Code:',e)
