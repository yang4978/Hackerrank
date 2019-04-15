#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):

    """acsii_num = list(map(ord,s));

    for i in range(len(acsii_num)):
        if(65<=acsii_num[i]<=90):
            acsii_num[i] += 32;
        elif(97<=acsii_num[i]<=122):
            acsii_num[i] -= 32;

    s_swap = ''.join(list((map(chr,acsii_num))));

    return s_swap"""
    return s.swapcase()

if __name__ == '__main__':
