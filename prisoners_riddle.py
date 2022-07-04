from random import *



# one prison, 100 presoners, 100 box. each box contain random number upto 100 with no repeat.
# presoner can enter into the prison only once.
# every presoner can open upto 50 box long as as they can't find her number inside the box.
# presoner can't comunicate with eachother.
# if presoner find his number then he wins.

# idea from : https://www.youtube.com/watch?v=iSNsgj1OCLA

box = []
box_num_temp = []


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

    # for i in range(len(box)):
    #     print(box[i])

# enter one presoner at a time and see if he can find his number with 50 chance.
temp1 = []
def findyournumber(chance):
    for i in range(len(box)):
        # enter presoner
        num = openbox(i)
        for j in range(chance):
            num = openbox(num)
            if num is i:
                temp1.append(i)
                print("found", num, i)
                break
            else:
                continue
            

    print( "Number of people found there number",len(temp1))

def openbox(index):
    return box[index]

def main():
    print("Hello World!")
    genarateBox(100)
    findyournumber(50)


if __name__ == "__main__":
    main()