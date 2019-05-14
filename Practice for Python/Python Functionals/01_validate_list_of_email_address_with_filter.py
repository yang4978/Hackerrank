#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import string
import re
def fun(s):
    # if('@' in s):
    #     username,rubbish,temp = s.partition('@')
    #     if('.' in temp):
    #         websitename,rubbish,extension = temp.partition('.')
    #         username=list(set(username))
    #         if(len(username)==0):
    #             return False;
    #         for i in string.digits+string.ascii_letters+'_'+'-':
    #             if i in username:
    #                 username.remove(i)
    #         if(username == []):
    #             websitename = list(set(websitename))
    #             if(len(websitename)==0):
    #                 return False;
    #             for i in string.digits+string.ascii_letters:
    #                 if i in websitename:
    #                     websitename.remove(i)
    #             if(websitename == []):
    #                 if(len(extension)<=3):
    #                     return True
    # return False
    return re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',s)
    # return True if s is a valid email, else return False

def filter_mail(emails):
