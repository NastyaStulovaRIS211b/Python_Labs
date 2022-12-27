class Employees:

    def __init__(self,n,a,num,s):
    	self.Name=n
    	self.Age=a
    	self.Office=num
    	self.Salary=s
    def Inf(self):
        return f'{self.Name} {self.Age} work in in the {self.Office} cabinet'



def GetName(self):
	 return {self.Name}



def GetSalary(self):
	 return self.Salary



h1=Employees("Alex Denvers",24,104,2500)
h2=Employees('Lena Luthor',58,805,7000)
h3=Employees('Kara Zorel',37,222,8760)
h4=Employees('Will Turner',45,995,5400)
h5=Employees('Laya Burnell',28,112,1000)


print('map')
a=[h1,h2,h3,h4,h5]
b = []
for i in range(5):
	b.append((GetName(a[i])))
print(b)


s1=GetSalary(a[0])
s2=GetSalary(a[1])
s3=GetSalary(a[2])
s4=GetSalary(a[3])
s5=GetSalary(a[4])

print('reduce')
s=s1+s2+s3+s4+s5
print(s)