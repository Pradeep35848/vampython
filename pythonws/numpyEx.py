import numpy  as np
#create numpy array to store 
#friend name,edit
myFriends = np.array(["ivan       ","anshu   ","wani    ","pradeep "])

print(myFriends)

print(type(myFriends))

print(myFriends[2])

for name in myFriends:
    print(name)
    
myFriends[0]="ivan sharma"
print(myFriends)

myFriends.sort()
print(myFriends)

mydata = np.flip(myFriends)
print(mydata)

y = 3
while y>=0:
    print(myFriends[y])
    y = y - 1