import json
class Animal:
     def __init__(self,n):
         self.name=n
    

class Predator(Animal):
    def __init__(self,n,s):
        Animal.__init__(self,n)
        self.sound=s
    def what(self):
        return f'{self.name} say {self.sound}'
       
print("-Class function")

print("What does the fox say?")
predator=Predator('fox','ring-ding-ding')
print(predator.what())
print("-Serialization")
json_string = json.dumps(predator, default=lambda obj: obj.__dict__,sort_keys=True,indent=4)
print(json_string)

def ld(d):
    return Predator(d['name'],d['sound'])
print("-Deserialization")

predator=json.loads(json_string, object_hook=ld)
print(predator.what())

