#user story 3 - as a class instructor, I want to be able to limit the number of participants in each class


j=0
while j <= 20:
    user = input("would you like to go to class? y/n")
    if user == "y":
        j = j+1
        #print(j)
    if j > 20:
        print("class is full")








