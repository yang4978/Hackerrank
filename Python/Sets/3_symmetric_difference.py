#https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ =='__main__':
    
    """
    m = int(input());
    set_m = set(map(int,input().split()));
    n = int(input());
    set_n = set(map(int,input().split()));
    a = list((set_m.difference(set_n)).union((set_n.difference(set_m))));
    a.sort()
    for i in a:
        print(i)"""
    m = int(input());
    set_m = set(input().split());
    n = int(input());
    set_n = set(input().split()); 
    print ("\n".join(sorted(list(set_m ^ set_n),key=int)))
    

