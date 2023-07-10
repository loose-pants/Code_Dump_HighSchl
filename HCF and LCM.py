#LCM and GCD 
def GDC(x,y):
    while y:
        x,y=y,x%y
    return x

def HCF(x,y):
    hcf=x*y/GDC(x,y)
    return hcf

print(GDC(14,21))
print(HCF(8,0))
    
        