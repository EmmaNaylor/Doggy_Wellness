#user story 3 - as a class instructor, I want to be able to limit the number of participants in each class

#this is a template for what it would look like


def class_fullness():
    j=0
    while j <= 20:
        user = input("would you like to attend this class? y/n")
        if user == "y":
            j = j+1
            print(j)
    if j > 20:
        raise Exception("sorry, this class is now full")


if __name__ == "__main__":
    class_fullness()









