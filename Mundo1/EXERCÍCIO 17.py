import math
opt=float(input("CATETO OPOSTO: "))
adj=float(input("ADJACENTE: "))
h=math.hypot(opt,adj)
print("CATETO OPOSTO {}, CATETO ADJASCENTE {}, HIPOTENUSA {:.2f}".format(opt,adj,h))
