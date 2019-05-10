#https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0;

	# Add your code here
    def computeDifference(self):
        # max_temp = 0;
        # for i in range(len(self.__elements)):
        #     for j in range(i+1,len(self.__elements)):
        #         if(abs(self.__elements[i]-self.__elements[j])>max_temp):
        #             max_temp = abs(self.__elements[i]-self.__elements[j]);
        # self.maximumDifference = max_temp;
        self.maximumDifference = abs(max(self.__elements)-min(self.__elements))


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
