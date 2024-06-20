import os, random, time

#---------------- Balance
Wallet = 500
Bet = 0
Balance_disp = []

#---------------- Game
Number = 0
Status = "Ready"


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
        
        

def roll_dice():
    global Number
    Number = random.randint(0,99)
    return Number

def Condition_WL(W):
    global Status
    if (Number <= W):
        Status = "Loser"
    else:
        Status = "Winner"
    return Status
        
def Boot():
    global Status
    Number = 0
    Bet = 0
    os.system("cls||clear")
    Balance(Wallet, Bet)
    Game(Status, Number)
    Main()
    
def Main():
    global Wallet
    global Number
    global Bet
    global Status
    i = 0
    os.system("cls||clear")
    Balance(Wallet, Bet)
    Game(Status, Number)    
    Bet = Place_Bet()
    Wallet -= Bet
    while i<=10:
        os.system("cls||clear")
        Balance(Wallet, Bet)
        Number = roll_dice()
        Status = "Rolling"
        Game(Status, Number)
        time.sleep(0.7)
        i+=1;
    os.system("cls||clear")
    Status = Condition_WL(46)
    if Status == "Winner":
        Wallet += 2*Bet
        Balance(Wallet, Bet)
        Game(Status, Number)
    else:
        Balance(Wallet, Bet)
        Game(Status, Number)       
    time.sleep(5)
    os.system("cls||clear")
    Status = "Ready"
    Balance(Wallet, Bet)
    Game(Status, Number)
    Bet = 0;
    Main()
    

Boot()


