wincount = 0
winamt = 0
i = 0


qsnans1 = ["What is the capital of Nepal?", ["Kathmandu", "Pokhara", "Chitwan", "Butwal"], "A",0]
qsnans2 = ["What is the capital of India?", ["Kathmandu", "Delhi", "Chitwan", "Butwal"], "B",1]
qsnans3 = ["What is the capital of China?", ["Beijing", "Delhi", "Chitwan", "Butwal"], "A",0]
qsnans4 = ["What is the capital of Pakistan?", ["Islamabad", "Pokhara", "Chitwan", "Butwal"], "A",0]
qsnans5 = ["What is the capital of Bangaladesh?", ["Kathmandu", "Dhaka", "Chitwan", "Butwal"], "B",1]
qsnans6 = ["What is the capital of Bhutan?", ["Beijing", "Thimpu", "Chitwan", "Butwal"], "B",1]
qsnans=[qsnans1,qsnans2,qsnans3,qsnans4,qsnans5,qsnans6]


for i in range(len(qsnans)):
        print("Question for",1000*(i+1))
        print(qsnans[i][0])
        print("A:",qsnans[i][1][0],"\t B:",qsnans[i][1][1],"\t C:",qsnans[i][1][2],"\t D:",qsnans[i][1][3])
        ans = input("Enter your choice: ").upper()
        if(ans == "A" or ans == "B" or ans == "C" or ans == "D"):
            if(ans == qsnans[i][2]):
                print("Correct!")
                winamt = winamt + 1000*(i+1)
                wincount = wincount + 1
            else:
                print("Incorrect")
                print("The answer is:",qsnans[i][1][qsnans[i][3]])
                break
        else:
            print("Invalid Choice. You Lost.")
            break


print("You won: Rs.",winamt)
print("You got",wincount,"correct answers.")
