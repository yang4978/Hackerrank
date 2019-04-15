#https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    print (any([i.isalnum() for i in s]))
    print (any([i.isalpha() for i in s]))
    print (any([i.isdigit() for i in s]))
    print (any([i.islower() for i in s]))
    print (any([i.isupper() for i in s]))

    """flag_alpha = 0;
    flag_digit = 0;
    flag_upper = 0;
    flag_lower = 0;
    for i in s:
        if(i.isalpha()):
            flag_alpha = 1;
        if(i.isdigit()):
            flag_digit = 1;
        if(i.islower()):
            flag_lower = 1;
        if(i.isupper()):
            flag_upper = 1;
    flag_alnum = flag_alpha+flag_digit;
    if(flag_alnum):
        print("True");
    else:
        print("False");
    if(flag_alpha):
        print("True");
    else:
        print("False");
    if(flag_digit):
        print("True");
    else:
        print("False");
    if(flag_lower):
        print("True");
    else:
        print("False");
    if(flag_upper):
        print("True");
    else:
        print("False"); """
