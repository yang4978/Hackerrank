#https://www.hackerrank.com/challenges/30-nested-logic/problem

d_a,m_a,y_a = map(int,input().split())
d_e,m_e,y_e = map(int,input().split())
fee = ((y_a-y_e)>0)*10000+((y_a-y_e)==0)*max(m_a-m_e,0)*500+((y_a-y_e)==0)*((m_a-m_e)==0)*max(d_a-d_e,0)*15
print(fee)
