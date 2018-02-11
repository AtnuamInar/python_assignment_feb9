class student():
    def __init__(self):
        self.fname=""
        self.lname=""

    def getstring(self):
        self.fname=input('Enter yur first name')
        self.lname=input('Enter your last name')

    def printstring(self):
        print(self.fname)
        print(self.lname)

    def generateemail(self):
         self.email="".join([self.fname,'.',self.lname,"@deerwalk.edu.np"])
        
        

std=student()
std.getstring()

std.generateemail()
print(std.email)


        

 
