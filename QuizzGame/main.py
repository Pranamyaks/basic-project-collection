print("Welcome!! to quizz..Game..")
quizz=[
    {
        'question':"What is the capital city of india?",
        'options':['A.Delhi','B.Chennai','C.Lucknow','D.Kerala'],
        'answer':'A'

    },
    {
        'question':"What is the capital city of Karnataka?",
        'options':['A.Delhi','B.Chennai','C.Lucknow','D.Bengaluru'],
        'answer':'D'

    },
    {
        'question':"Which language is used in AI",
        'options':['A.HTML','B.CSS','C.Python','D.C++'],
        'answer':'C'
    },
    {
        'question':'2+2=?',
        'options':['A.5','B.6','C.3','D.4'],
        'answer':'D'
    }
]
score=0
for q in quizz:
    print("\n",q['question'])
    for option in q['options']:
        print(option)
    user_answer=input("Enter your option:A/B/C/D:").upper()
    if user_answer==q['answer']:
        print("Correct Answer")
        score+=1
    else:
        print("wrong Answer!!..correct answer is",q['answer'])
print("your total score is", score,"/",len(quizz))
print(f"Total percentage is {score/len(quizz)*100}%")    
                
