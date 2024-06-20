import os, random, time

#---------------- Balance
Wallet = 500
Bet = 0
Balance_disp = []

#---------------- Game
Number = 0
Status = "Ready"

#---------------- Results
Result=[['.','.'],['.','.'],['.','.'],['.','.'],['.','.']]
Result_Population = 0


# Initialize X by Y display with '.' and '=' Margins at Bottom and Top of Each Display Section
def display_maker(x,y):
    disp_top = [['=' for _ in range(x)] for _ in range(1)]
    disp_screen = [['.' for _ in range(x)] for _ in range(y)]
    disp_bottom = [['=' for _ in range(x)] for _ in range(1)]
    disp = disp_top + disp_screen + disp_bottom
    return disp

# Function to print the current state of the display
def print_display(disp):
    for row in disp:
        for element in row:
            print(element, end='')
        print()

# Function to update a specific position in the display
def update_display(disp,x, y, char):
    char_room = len(char)
    char_list = list(char)
    i = 0;      
    #print(char_room)
    #print(char_list)
    #print(disp[x+1][y])
    if char_room <= 64:
        while i < char_room:
            disp[x+1][y+i] = char[i]
            i += 1
    else:
        return 0

#Display Balance
def Balance(Wallet, Bet):
    #Constructor 64x(6) display Balance
    Balance_disp = display_maker(64,4)
    #Wallet Parameters
    update_display(Balance_disp, 0, 0, "Wallet: ")
    update_display(Balance_disp, 0, len("Wallet: "), str(Wallet));
    #Bet Parameters
    update_display(Balance_disp, 2, 0, "Bet: ")
    update_display(Balance_disp, 2, len("Bet: "), str(Bet));
    print_display(Balance_disp)
    return Balance_disp


#Display Game
def Game(Status, Number):
    #Constructor 64x(18) display Game
    Game_disp = display_maker(64,16)
    #Status Parameters
    i = 2
    j = 4
    k = 16
    while i<= 14:
        update_display(Game_disp, i, 4, Status)
        update_display(Game_disp, i, -9, Status)
        i += 2;
    while j <= 12:
        while k <= 48:
            update_display(Game_disp, j, k, str(Number))   
            k += 6;
        k = 16;
        j += 1;
    print_display(Game_disp)

#Display Results
def Results():
    global Result
    i=0;
    #Constructor 64x(8) disply Results
    Results_disp = display_maker(64,6)
    #Last Results Parameters
    update_display(Results_disp, 5, 25, "Last Results")
    while i<=4:
        update_display(Results_disp, i, 0, str(Result[i][0] + "......" + Result[i][1]))
        i+=1;
    print_display(Results_disp)
    return Results_disp    
    

#Prompt to Place Bet
def Place_Bet():
    global Bet
    global Wallet
    try:
        BetArgument = int(input("Place a Bet: "))
        if BetArgument > Wallet:
            Main()
        else:
            Bet = BetArgument
            return Bet
    except:
        Main()
        
        
#Dice Roller
def roll_dice():
    global Number
    Number = random.randint(0,99)
    return Number

#Condition Checker
def Condition_WL(W):
    global Status
    if (Number <= W):
        Status = "Loser"
    else:
        Status = "Winner"
    return Status
        
    


#First Boot with Zeros (Redundant, but Whatever it's nice for testing sometimes)
def Boot():
    global Status
    Number = 0
    Bet = 0
    os.system("cls||clear")
    #--------------- Initial call Displays
    Balance(Wallet, Bet)
    Game(Status, Number)
    Results()
    Main()
   
#Main 
def Main():
    global Wallet
    global Number
    global Bet
    global Status
    global Result;
    global Result_Population;
    i = 0
    if Result_Population == 5:
        Result_Population = 0
    os.system("cls||clear")
    #--------------- Recall Displays
    Balance(Wallet, Bet)
    Game(Status, Number) 
    Results()
    Bet = Place_Bet()
    Wallet -= Bet
    while i<=10:
        os.system("cls||clear")
        #--------------- Recall Displays
        Balance(Wallet, Bet)
        Number = roll_dice()
        Status = "Rolling"
        Game(Status, Number)
        Results()
        time.sleep(0.7)
        i+=1
    os.system("cls||clear")
    Status = Condition_WL(46)
    if Status == "Winner":
        #--------------- Recall Displays
        Wallet += 2*Bet
        Balance(Wallet, Bet)
        Game(Status, Number)
        Results()
    else:
        #--------------- Recall Displays
        Balance(Wallet, Bet)
        Game(Status, Number)   
        Results()
    time.sleep(5)
    if(len(Result) <= 4):
        Result.append([Status,str(Bet)])
    else:
        Result[Result_Population] = [Status, str(Bet)]
        Result_Population += 1;
    os.system("cls||clear")
    Status = "Ready"
    #--------------- Recall Displays
    Balance(Wallet, Bet)
    Game(Status, Number)
    Results()
    Bet = 0
    Main()
    

Boot()

