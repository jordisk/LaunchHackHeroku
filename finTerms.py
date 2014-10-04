
import math


LN	= 2.0	# length of nose
d	= 3.0	# diameter at base of nose
dF	= 4.0	# diameter at front of transition
dR	= 5.0	# diameter at rear of transition
LT	= 6.0	# length of transition
XP	= 7.0	# distance from tip of nose to front of transition
CR	= 8.0	# fin root chord
CT	= 9.0	# fin tip chord
S	= 1.0	# fin semispan
LF	= 2.0	# length of fin mid-chord line
R	= 3.0	# radius of body at aft end
XR	= 4.0	# distance between fin root leading edge and fin tip leading edge parallel to body
XB	= 5.0	# distance from nose tip to fin root chord leading edge
N	= 6.0	# number of fins

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





