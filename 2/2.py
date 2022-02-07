f=open("2-input.txt","r")
print("Actual file")
print("")
for i in f.readlines():
        print(i.strip())
f.close()
f=open("2-input.txt","r")
o=open("2-output.txt","w")
for c in f.readlines():
    if(len(c.split(" "))>5 and c[0].isupper()):
        o.write(c)
f.close()
o.close()
print("")
print("Output--------------------------------")
print("")
o=open("2-output.txt","r")
for c in o.readlines():
    print(c.strip())
o.close()




