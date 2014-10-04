from enum import Enum

LN	= 2	# length of nose
d	= 3	# diameter at base of nose
dF	= 4	# diameter at front of transition
dR	= 5	# diameter at rear of transition
LT	= 6	# length of transition
XP	= 7	# distance from tip of nose to front of transition
CR	= 8	# fin root chord
CT	= 9	# fin tip chord
S	= 1	# fin semispan
LF	= 2	# length of fin mid-chord line
R	= 3	# radius of body at aft end
XR	= 4	# distance between fin root leading edge and fin tip leading edge parallel to body
XB	= 5	# distance from nose tip to fin root chord leading edge
N	= 6	# number of fins

#The nose cone enum class
class noseConeTypes(Enum):
	cone = 1
	Ogive = 2
	
#Nose Cone 
CNN = 2;
XN = 0;

#NoseConeTypes = ["cone","Ogive"]
#cone = NoseConeTypes[0]
#Ogive = NoseConeType[1]

#Without enum
#def NoseConeTerms (NoseCone):
#    if NoseCone == cone:
#        XN = 0.666 * N
#    elif NoseCone == Ogive:
#        XN = 0.466 * N
#    else :
#        print("Error, Cone not recognised")

#With enum
def noseConeTerms (noseCone):
	if noseCone = noseConeTypes.cone:
		XN = 0.666 * N
	elif noseCone = noseConeTypes.Ogive:
		XN = 0.466 * N 
	else :
		print("Error, Cone was not recognised")
    
#NoseConeTerms("cone") 
noseConeTerms(noseConeTypes.cone)   
