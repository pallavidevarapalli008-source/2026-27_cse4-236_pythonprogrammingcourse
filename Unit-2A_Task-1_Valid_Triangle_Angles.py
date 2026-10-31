a = float(input("Enter first angle in degrees:"))
b= float(input("Enter seconmd angle in degrees:"))
c = float(input("Enter third angle in degrees:"))
if a>0 and b>0 and c>0 and a+b+c==180:
    print(f"Valid triangle (angles={a},{b},{c})")
else:
    print(f"Not a valid triangle(angles={a},{b},{c})")