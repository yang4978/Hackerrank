#https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1,number+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))
        
    """num = number.bit_length()+1;
    for i in range (1,number+1):
        print('{:d}'.format(i).rjust(num-1,' '),end='')
        print('{:o}'.format(i).rjust(num,' '),end='')
        print('{:X}'.format(i).rjust(num,' '),end='')
        print('{0:b}'.format(i).rjust(num,' '))"""



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
