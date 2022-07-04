from random import *



# one prison, 100 presoners, 100 box. each box contain random number upto 100 with no repeat.
# presoner can enter into the prison only once.
# every presoner can open upto 50 box long as as they can't find her number inside the box.
# presoner can't comunicate with eachother.
# if presoner find his number then he wins.

# idea from : https://www.youtube.com/watch?v=iSNsgj1OCLA

box = []
box_num_temp = []
temp = []
ava = []

# make 100 box with random 100 number but not repeated
def genarateBox(num_of_presoner):
    for i in range(num_of_presoner):
        box_num_temp.append(i)

    for i in range(num_of_presoner):
        n = box_num_temp[randrange(len(box_num_temp))]
        box_num_temp.remove(n)
        if n in box:
            print("n contains")
        else:
            box.append(n)
            # print("n is not contained")


# enter one presoner at a time and see if he can find his number with 50 chance.

def findyournumber(chance):
    for i in range(len(box)):
        # enter presoner
        num = openbox(i)
        for j in range(chance):
            num = openbox(num)
            if num == i:
                temp.append(i)
                # print("found", num, i)
                break

            

    print( "Number of people found there number", len(temp))

    if len(temp) >= len(box):
        ava.append(1)

    

def openbox(index):
    return box[index]

def main():
    print("Hello World!")
   

    for i in range(100):
        genarateBox(1000)
        findyournumber(500)
        box.clear()
        box_num_temp.clear()
        temp.clear()


    print("total times 100 people success", len(ava))


if __name__ == "__main__":
    main()