#https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   idNum - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName = firstName;
        self.lastName = lastName;
        self.idNum = idNum;
        self.scores = scores;
    
    def printPerson(self):
        print("Name: %s,"%self.lastName,self.firstName);
        print("ID:",self.idNum)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum_scores = sum(self.scores);
        aver = sum_scores/len(self.scores);
        if(90<=aver<=100):
            return 'O';
        elif(80<=aver<90):
            return 'E';
        elif(70<=aver<80):
            return 'A';
        elif(55<=aver<70):
            return 'P';
        elif(40<=aver<55):
            return 'D';
        else:
            return 'T';


line = input().split()
