#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)];

    #answer
    n = size
    for i in range(n):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))

    for i in range(n-1):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))

    # my own code
    """total = 4*size - 3;
    for i in range(size):
        temp ='';
        for j in range(i+1):
            temp += alphabet[size-j-1]+'-';
        for j in range(i-1,-1,-1):
            temp += alphabet[size-j-1]+'-';
        temp = temp[0:len(temp)-1];
        print (temp.center(total,'-'))
    
    for i in range(size-2,-1,-1):
        temp ='';
        for j in range(i+1):
            temp += alphabet[size-j-1]+'-';
        for j in range(i-1,-1,-1):
            temp += alphabet[size-j-1]+'-';
        temp = temp[0:len(temp)-1];
        print (temp.center(total,'-'))"""

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
