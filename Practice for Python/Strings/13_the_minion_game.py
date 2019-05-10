#https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = ['A','E','I','O','U'];
    sum_vowels = 0;
    sum_consonants = 0;

    for i in range(len(string)):
        if(string[i] in vowels):
            sum_vowels += len(string)-i;
        else:
            sum_consonants += len(string)-i;
                   
    if(sum_consonants>sum_vowels):
        print("Stuart",sum_consonants)
    elif(sum_consonants<sum_vowels):
        print("Kevin",sum_vowels)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
