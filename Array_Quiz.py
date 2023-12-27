print("........................................Kasle jitchxa Kalo khassi??..............................................")

print("Welcome to the game...\nTapaile 10 prasna ko sahi jawaf diya ma....\n"
      "Tapaile jitnu huncha euta aakarshak 'Khassi'...")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

questionArray = ["What is the capital city of Nepal",                    #1
                 "Who is the Prime Minister of Nepal",                  #2
                 "Which is the biggest Nation",                         #3
                 "Who is the Mayor of Kathmandu Metropolitian City",    #4
                 "What is the natural satelite of earth",               #5
                 "What is the Tallest mountain in world",               #6
                 "What is the area of rectangle",                       #7
                 "Which is the largest ocean",                           #8
                 "Which country won FIFA worldcup 2022",                 #9
                 "Which is the longest river of nepal",                  #10
                 ]
ansArray = [["Lalitpur", "Pokhara", "Kathmandu","birjung"],             #1 #3
            ["Prachanda", "KP oli", "SherBahadur", "Rajesh Hamal"],     #2 #1
            ["Inida", "china",'Russia','Usa'],                          #3 #3
            ['Harka Sampang', 'Gopi Hamal','Balen Shah','Chir Babu'],   #4 #3
            ['Appolo-19', 'Titan', 'Cirus','Moon'],                     #5 #4
            ['Rajkada', 'Everest','Nanga Parbat', 'Manaslu'],           #6 #2
            ['L*B','L*B*H', "1/2 L*B", "L*L"],                          #7 #1
            ['Artic', 'Indian', "Atlantic", "Pacific"],                 #8 #4
            ['Brazil', 'England', 'Argentina','Portugal'],              #9 #3
            ['Mechi', "Koshi", 'Karnali', 'Rapti']                      #10 #3
            ]
listAnswer = [2,0,2,2,3,1,0,3,2,2]
prizeArray = ["KALO KHASSI", "RATO BHALEY", "500 RUPIYA"]
def prizeDistribute(p):
    print("Since you have answered ", p," questions correctly\n You have won", prizeArray[10-p])

Count=1
for i in range(10):
    j=0
    print(i+1,".",questionArray[i],"?")
    while j<=3:
        print(j+1,ansArray[i][j])
        j+=1
    # listAnswer = [2, 0, 2, 2, 3, 1, 0, 3, 2, 2]

    j = listAnswer[i]   #Here the correct answer is fetched into j variable from list of correct answer index
    temp = int(input("Which is correct 1, 2, 3, or 4?\n"))
    # The user inout is stored in temp

    if j == (temp-1):
        if(i==9):
            break
        print("!!! CORRECT ANSWER !!!\nAba Khassi afno ghar lana",9-i,"Questions baaki chhan...")
        Count +=1
    else:
        print("!!! YOUR ANSWER IS INCORRECT !!!\n")
        print("The Right Answer is", ansArray[i][j] )

    input("Press Enter Key to continue Quiz")
    print(
        "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n\n")
if Count >8:
    print("Congratulations you are qualified for a prize")
    prizeDistribute(Count)
else:

    print("Sorry you did not answered at least 8 questions right!\nPlease try again...")












