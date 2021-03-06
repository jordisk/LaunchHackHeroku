#Create Component Class
class Component:
	def __init__(self, Mass, Distance, Name):
		self.weight = Mass * 9.8 #9.8 is the gravity
		self.distance = Distance
		#Remove Name after debugging
		self.name = Name
	def cgValue(self):
		print (self.name + " cgValue: " + str((self.distance * self.weight)))
		return self.distance * self.weight

def getCentreOfGravity(Nose, Recovery, Body, Engine, Fins):
	#Combine weights
	weight = Nose.weight + Recovery.weight + Body.weight + Engine.weight + Fins.weight
	#Work out the centre of gravity
	cg = (Nose.cgValue() + Recovery.cgValue() + Body.cgValue() + Engine.cgValue() + Fins.cgValue()) / weight
	print ("Weight of Rocket: " + str(weight))	
	return cg

#Test Values
Nose = Component(3.69,49.2, "Nose")
print ("Nose Weight: " + str(Nose.weight))

Recovery = Component(0.6,39.15, "Recovery")
print ("Recovery Weight: " + str(Recovery.weight))

Body = Component(7.06,22.85, "Body")
print ("Body Weight: " + str(Body.weight))

Engine = Component(21.1,7.0,"Engine")
print ("Engine Weight: " + str(Engine.weight))

Fins = Component(184,3.0,"Fins")
print ("Fins Weight: " + str(Body.weight))

print getCentreOfGravity(Nose,Recovery,Body,Engine,Fins)


