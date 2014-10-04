
import math


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

#cnf 
raizcuadrada = math.sqrt(1 + ((2 * LF) / (CR + CT))**2)

cnf =  (1 + (R/(S + R) ) ) * (

	((4 * N) * (S/d)*(S/d)) /

	(1 + raizcuadrada))

print cnf




#XF

Xf = XB + ((XR / 3) * ((CR+(2*CT)) / (CR+CT) ) + (1/6) * (
	(CR+CT) - ((CR*CT) / (CR+CT))
	)


	)

print Xf







