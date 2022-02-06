print("Hello! Welcome to KBC")
ans=input("Are you ready to play(yes/no)")
a="NOTE: Write answers! Do not copy the options"
score=0
total_question=3
correct_ans=["Seven","Delhi","Software Engineering"]
question_list=["How many continents are there?","What is the capital of Indian?","NG me kaun sa course padhaya jata hai?"]
option_list=[["Four","Nine","Seven","Eight"],["Chandigarh","Bhopal","Chennai","Delhi"],["Software Engineering","Counselling","Tourism","Agriculture"]]
if ans=="yes":
    print(a)
    print(question_list[0])
    print(option_list[0])
    ans=input("The answer is:")
    if ans==correct_ans[0]:
        score=score+1
        print("CORRECT")
    else:
        print("INCORRECT")
    print(a)
    print(question_list[1])
    print(option_list[1])
    ans=input("The answer is:")
    if ans==correct_ans[1]:
        score=score+1
        print("CORRECT")
    else:
        print("INCORRECT")
    print(a)
    print(question_list[2])
    print(option_list[2])
    ans=input("The answer is:")
    if ans==correct_ans[2]:
        score=score+1
        print("CORRECT")
    else:
        print("INCORRECT")
i=score*10
if i==20:
    print("oops, your score is",i,"/30 better luck next time")
elif i==20:
    print("WOW! you scored",i,"/30 you are quite smart")
else:
    print("Congratulations! it's a perfect",i,"/30 you are intelligent")


#KBC