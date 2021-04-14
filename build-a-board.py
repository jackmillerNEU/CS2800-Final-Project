# CS2800 Final Project
# build-a-board.py
#
#



import tkinter as tk

board = [[[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']],
         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']],
         [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]];

def draw_board():
    global board
    row = '';
    for i in range(3):
        for j in range(3):
            print('     |     |     ')
            for k in range(3):
                letter = board[i][j][k]
                if letter == 'BLOCK':
                    letter = 'B'
                row = row + '  ' + letter + '  ';
                if k == 0 or k == 1:
                    row += '|'
            print(row);
            if j != 2:
                print('_____|_____|_____')
            else:
                print('     |     |     ')
            row = ''
        print()

placing_x = 1

def place_x():
    global placing_x
    placing_x = 1
def place_o():
    global placing_x
    placing_x = 0
def place_block():
    global placing_x
    placing_x = 2
def done():
    window.destroy()
    draw_board()
    
    
def ijk_to_pos(i, j, k):
    pos = '';
    if i == 0:
        pos += 'a';
    elif i == 1:
        pos += 'b';
    elif i == 2:
        pos += 'c';
    if j == 0:
        pos += 'i';
    elif j == 1:
        pos += 'j';
    elif j == 2:
        pos += 'k';
    pos += str(k + 1);
#    print(str(i) + ' ' + str(j) + ' ' + str(k));
#    print(pos);
    return pos       


def ai1_pressed():
    i=0;
    j=0;
    k=0;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ai1 = tk.Button(master=frm_top, text=val, bg=color, command=ai1_pressed)
    btn_ai1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def ai2_pressed():
    i=0;
    j=0;
    k=1;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ai2 = tk.Button(master=frm_top, text=val, bg=color, command=ai2_pressed)
    btn_ai2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def ai3_pressed():
    i=0;
    j=0;
    k=2;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ai3 = tk.Button(master=frm_top, text=val, bg=color,  command=ai3_pressed)
    btn_ai3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def aj1_pressed():
    i=0;
    j=1;
    k=0;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ai1 = tk.Button(master=frm_top, text=val, bg=color,  command=aj1_pressed)
    btn_ai1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def aj2_pressed():
    i=0;
    j=1;
    k=1;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_aj2 = tk.Button(master=frm_top, text=val, bg=color,  command=aj2_pressed)
    btn_aj2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def aj3_pressed():
    i=0;
    j=1;
    k=2;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_aj3 = tk.Button(master=frm_top, text=val, bg=color,  command=aj3_pressed)
    btn_aj3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ak1_pressed():
    i=0;
    j=2;
    k=0;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ak1 = tk.Button(master=frm_top, text=val,  bg=color,  command=ak1_pressed)
    btn_ak1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ak2_pressed():
    i=0;
    j=2;
    k=1;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ak2 = tk.Button(master=frm_top, text=val, bg=color,  command=ak2_pressed)
    btn_ak2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ak3_pressed():
    i=0;
    j=2;
    k=2;
    global board
    color = 'gray90';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray90';
    btn_ak3 = tk.Button(master=frm_top, text=val, bg=color,  command=ak3_pressed)
    btn_ak3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
    
# board 2 ************************************************************
    
def bi1_pressed():
    i=1;
    j=0;
    k=0;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bi1 = tk.Button(master=frm_mid, text=val, command=bi1_pressed, bg=color)
    btn_bi1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def bi2_pressed():
    i=1;
    j=0;
    k=1;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bi2 = tk.Button(master=frm_mid, text=val, command=bi2_pressed, bg=color)
    btn_bi2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def bi3_pressed():
    i=1;
    j=0;
    k=2;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bi3 = tk.Button(master=frm_mid, text=val, bg=color,  command=bi3_pressed,)
    btn_bi3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bj1_pressed():
    i=1;
    j=1;
    k=0;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bi1 = tk.Button(master=frm_mid, text=val, bg=color,  command=bj1_pressed)
    btn_bi1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bj2_pressed():
    i=1;
    j=1;
    k=1;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bj2 = tk.Button(master=frm_mid, text=val, bg=color,  command=bj2_pressed)
    btn_bj2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bj3_pressed():
    i=1;
    j=1;
    k=2;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bj3 = tk.Button(master=frm_mid, text=val, bg=color,  command=bj3_pressed)
    btn_bj3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bk1_pressed():
    i=1;
    j=2;
    k=0;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bk1 = tk.Button(master=frm_mid, text=val, bg=color,  command=bk1_pressed)
    btn_bk1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bk2_pressed():
    i=1;
    j=2;
    k=1;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bk2 = tk.Button(master=frm_mid, text=val, bg=color,  command=bk2_pressed)
    btn_bk2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def bk3_pressed():
    i=1;
    j=2;
    k=2;
    global board
    color = 'lightgray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'lightgray';
    btn_bk3 = tk.Button(master=frm_mid, text=val, bg=color,  command=bk3_pressed)
    btn_bk3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

# board 3 ************************************************************

def ci1_pressed():
    i=2;
    j=0;
    k=0;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ci1 = tk.Button(master=frm_bot, text=val, bg=color,  command=ci1_pressed)
    btn_ci1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def ci2_pressed():
    i=2;
    j=0;
    k=1;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    ctn_ai2 = tk.Button(master=frm_bot, text=val, bg=color,  command=ci2_pressed)
    ctn_ai2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
def ci3_pressed():
    i=2;
    j=0;
    k=2;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ci3 = tk.Button(master=frm_bot, text=val, bg=color,  command=ci3_pressed)
    btn_ci3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def cj1_pressed():
    i=2;
    j=1;
    k=0;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ci1 = tk.Button(master=frm_bot, text=val, bg=color,  command=cj1_pressed)
    btn_ci1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def cj2_pressed():
    i=2;
    j=1;
    k=1;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_cj2 = tk.Button(master=frm_bot, text=val, bg=color,  command=cj2_pressed)
    btn_cj2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def cj3_pressed():
    i=2;
    j=1;
    k=2;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_cj3 = tk.Button(master=frm_bot, text=val, bg=color,  command=cj3_pressed)
    btn_cj3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ck1_pressed():
    i=2;
    j=2;
    k=0;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ck1 = tk.Button(master=frm_bot, text=val, bg=color,  command=ck1_pressed)
    btn_ck1.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ck2_pressed():
    i=2;
    j=2;
    k=1;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ck2 = tk.Button(master=frm_bot, text=val, bg=color,  command=ck2_pressed)
    btn_ck2.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val

def ck3_pressed():
    i=2;
    j=2;
    k=2;
    global board
    color = 'gray';
    if board[i][j][k] == ' ':    
        if placing_x == 1:
            val = 'x'
        elif placing_x == 0:
            val = 'o'
        elif placing_x == 2:
            val = 'BLOCK'
            color = 'red';
    else:
        val = ' '
        color = 'gray';
    btn_ck3 = tk.Button(master=frm_bot, bg=color, text=val, command=ck3_pressed)
    btn_ck3.grid(sticky="nsew", row=j, column=k)
    board[i][j][k] = val
    

window = tk.Tk()
window.title('Board Setup')

frm_buttons = tk.Frame(master=window)
frm_buttons.pack(ipadx=5, ipady=5)

btn_x = tk.Button(master=frm_buttons, text="x", foreground="white", bg="black", command=place_x)
btn_x.pack(side=tk.LEFT, padx = 10, ipadx = 10)

btn_o = tk.Button(master=frm_buttons, text="o", bg="white", command=place_o)
btn_o.pack(side=tk.LEFT, padx = 10, ipadx = 10)

btn_block = tk.Button(master=frm_buttons, text="block", bg="red", command=place_block)
btn_block.pack(side=tk.LEFT, padx = 10, ipadx = 10)

btn_done = tk.Button(master=frm_buttons, text="Done", bg="white", command=done)
btn_done.pack(side=tk.RIGHT, padx = 10, ipadx = 10)

frm_top = tk.Frame(master=window, bg="red", width=150)
frm_top.columnconfigure([0,1,2], weight=1, minsize=50)
frm_top.rowconfigure([0,1,2], weight=1, minsize=50)
frm_top.pack(fill=tk.BOTH)

btn_ai1 = tk.Button(master=frm_top, text="", bg ="gray90", command=ai1_pressed)
btn_ai1.grid(sticky="nsew", row=0, column=0)
btn_ai2 = tk.Button(master=frm_top, text="", bg ="gray90", command=ai2_pressed)
btn_ai2.grid(sticky="nsew", row=0, column=1)
btn_ai3 = tk.Button(master=frm_top, text="", bg ="gray90", command=ai3_pressed)
btn_ai3.grid(sticky="nsew", row=0, column=2)
btn_aj1 = tk.Button(master=frm_top, text="", bg ="gray90", command=aj1_pressed)
btn_aj1.grid(sticky="nsew", row=1, column=0)
btn_aj2 = tk.Button(master=frm_top, text="", bg ="gray90", command=aj2_pressed)
btn_aj2.grid(sticky="nsew", row=1, column=1)
btn_aj3 = tk.Button(master=frm_top, text="", bg ="gray90", command=aj3_pressed)
btn_aj3.grid(sticky="nsew", row=1, column=2)
btn_ak1 = tk.Button(master=frm_top, text="", bg ="gray90", command=ak1_pressed)
btn_ak1.grid(sticky="nsew", row=2, column=0)
btn_ak2 = tk.Button(master=frm_top, text="", bg ="gray90", command=ak2_pressed)
btn_ak2.grid(sticky="nsew", row=2, column=1)
btn_ak3 = tk.Button(master=frm_top, text="", bg ="gray90", command=ak3_pressed)
btn_ak3.grid(sticky="nsew", row=2, column=2)

frm_mid = tk.Frame(master=window, bg="yellow", width=150)
frm_mid.columnconfigure([0,1,2], weight=1, minsize=50)
frm_mid.rowconfigure([0,1,2], weight=1, minsize=50)
frm_mid.pack(fill=tk.BOTH)

btn_bi1 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bi1_pressed)
btn_bi1.grid(sticky="nsew", row=0, column=0)
btn_bi2 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bi2_pressed)
btn_bi2.grid(sticky="nsew", row=0, column=1)
btn_bi3 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bi3_pressed)
btn_bi3.grid(sticky="nsew", row=0, column=2)
btn_bj1 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bj1_pressed)
btn_bj1.grid(sticky="nsew", row=1, column=0)
btn_bj2 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bj2_pressed)
btn_bj2.grid(sticky="nsew", row=1, column=1)
btn_bj3 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bj3_pressed)
btn_bj3.grid(sticky="nsew", row=1, column=2)
btn_bk1 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bk1_pressed)
btn_bk1.grid(sticky="nsew", row=2, column=0)
btn_bk2 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bk2_pressed)
btn_bk2.grid(sticky="nsew", row=2, column=1)
btn_bk3 = tk.Button(master=frm_mid, text="", bg ="lightgray", command=bk3_pressed)
btn_bk3.grid(sticky="nsew", row=2, column=2)

frm_bot = tk.Frame(master=window, bg="blue", width=150)
frm_bot.columnconfigure([0,1,2], weight=1, minsize=50)
frm_bot.rowconfigure([0,1,2], weight=1, minsize=50)
frm_bot.pack(fill=tk.BOTH)

btn_ci1 = tk.Button(master=frm_bot, text="", bg ="gray", command=ci1_pressed)
btn_ci1.grid(sticky="nsew", row=0, column=0)
btn_ci2 = tk.Button(master=frm_bot, text="", bg ="gray", command=ci2_pressed)
btn_ci2.grid(sticky="nsew", row=0, column=1)
btn_ci3 = tk.Button(master=frm_bot, text="", bg ="gray", command=ci3_pressed)
btn_ci3.grid(sticky="nsew", row=0, column=2)
btn_cj1 = tk.Button(master=frm_bot, text="", bg ="gray", command=cj1_pressed)
btn_cj1.grid(sticky="nsew", row=1, column=0)
btn_cj2 = tk.Button(master=frm_bot, text="", bg ="gray", command=cj2_pressed)
btn_cj2.grid(sticky="nsew", row=1, column=1)
btn_cj3 = tk.Button(master=frm_bot, text="", bg ="gray", command=cj3_pressed)
btn_cj3.grid(sticky="nsew", row=1, column=2)
btn_ck1 = tk.Button(master=frm_bot, text="", bg ="gray", command=ck1_pressed)
btn_ck1.grid(sticky="nsew", row=2, column=0)
btn_ck2 = tk.Button(master=frm_bot, text="", bg ="gray", command=ck2_pressed)
btn_ck2.grid(sticky="nsew", row=2, column=1)
btn_ck3 = tk.Button(master=frm_bot, text="", bg ="gray", command=ck3_pressed)
btn_ck3.grid(sticky="nsew", row=2, column=2)
window.mainloop()

turns = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9',
        't10', 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18',
        't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27'];


numTurns = 0;

whiteinits = '';
for i in range(3):
    for j in range(3):
        for k in range(3):
            if board[i][j][k] == 'o':
                whiteinits += ijk_to_pos(i, j, k) + ' ';
                numTurns += 1;
                
blackinits = '';
for i in range(3):
    for j in range(3):
        for k in range(3):
            if board[i][j][k] == 'x':
                blackinits += ijk_to_pos(i, j, k) + ' ';
                numTurns += 1;
                

turnsStr = '';
for i in range(27):
    if i >= numTurns:
        turnsStr += turns[i] + ' ';
        
# 
      
blackTurnsStr = '';
for i in range(27):
    if i >= numTurns and i % 2 == 0:
        blackTurnsStr += turns[i] + ' ';
           

f = open("boardMap.qdimacs", "a");
f.truncate(0);
f.write("#version\n");
f.write("1.0\n");

#times
f.write("#times\n");
f.write(turnsStr + "\n");

#blackturns
f.write("#blackturns\n");
f.write(blackTurnsStr + "\n");

#positions
f.write("#positions\n");

pos = '';
for i in range(3):
    for j in range(3):
        for k in range(3):
            if board[i][j][k] != 'BLOCK':
                pos = pos + ijk_to_pos(i,j,k) + ' '

f.write(pos + '\n');

#ai1 ai2 ai3 
#aj1 aj2 aj3 
#ak1 ak2 ak3
#
#bi1 bi2 bi3 
#bj1 bj2 bj3 
#bk1 bk2 bk3
#
#ci1 ci2 ci3 
#cj1 cj2 cj3 
#ck1 ck2 ck3

#blackwins
f.write("#blackwins\n");

#2d wins ******************************************
#horizontal wins
f.write("ai1 ai2 ai3\naj1 aj2 aj3\nak1 ak2 ak3\n" +
        "bi1 bi2 bi3\nbj1 bj2 bj3\nbk1 bk2 bk3\n" +
        "ci1 ci2 ci3\ncj1 cj2 cj3\nck1 ck2 ck3\n");
#vertical wins
f.write("ai1 aj1 ak1\nbi1 bj1 bk1\nci1 cj1 ck1\n" +
        "ai2 aj2 ak2\nbi2 bj2 bk2\nci2 cj2 ck2\n" +
        "ai3 aj3 ak3\nbi3 bj3 bk3\nci3 cj3 ck3\n");
#diagonal wins
f.write("ai1 aj2 ak3\nbi1 bj2 bk3\nci1 cj2 ck3\n" +
        "ai3 aj2 ak1\nbi3 bj2 bk1\nbi3 bj2 bk1\n");
#3d wins ******************************************
#column wins
f.write("ai1 bi1 ci1\nai2 bi2 ci2\nai3 bi3 ci3\n" +
        "aj1 bj1 cj1\naj2 bj2 cj2\naj3 bj3 cj3\n" +
        "ak1 bk1 ck1\nak2 bk2 ck2\nak3 bk3 ck3\n");
# diagonal wins top-bottom
f.write("ai1 bj1 ck1\nai2 bj2 ck2\nai3 bj3 ck3\n" +
        "ak1 bj1 ci1\nak2 bj2 ci2\nak3 bj3 ci3\n");
# diagonal wins left-right
f.write("ai1 bi2 ci3\naj1 bj2 cj3\nak1 bk2 ck3\n" +
        "ai3 bi2 ci1\naj3 bj2 cj1\nak3 bk2 ck1\n");
# diagonal wins corner-corner
f.write("ai1 bj2 ck3\nai3 bj2 ck3\n" + 
        "ak1 bj2 ci3\nak3 bj2 ci1\n");

#blackinitials
f.write("#blackturns\n");
f.write(blackinits + '\n');

#whitewins
f.write("#whitewins\n");

#2d wins ******************************************
#horizontal wins
f.write("ai1 ai2 ai3\naj1 aj2 aj3\nak1 ak2 ak3\n" +
        "bi1 bi2 bi3\nbj1 bj2 bj3\nbk1 bk2 bk3\n" +
        "ci1 ci2 ci3\ncj1 cj2 cj3\nck1 ck2 ck3\n");
#vertical wins
f.write("ai1 aj1 ak1\nbi1 bj1 bk1\nci1 cj1 ck1\n" +
        "ai2 aj2 ak2\nbi2 bj2 bk2\nci2 cj2 ck2\n" +
        "ai3 aj3 ak3\nbi3 bj3 bk3\nci3 cj3 ck3\n");
#diagonal wins
f.write("ai1 aj2 ak3\nbi1 bj2 bk3\nci1 cj2 ck3\n" +
        "ai3 aj2 ak1\nbi3 bj2 bk1\nbi3 bj2 bk1\n");
#3d wins ******************************************
#column wins
f.write("ai1 bi1 ci1\nai2 bi2 ci2\nai3 bi3 ci3\n" +
        "aj1 bj1 cj1\naj2 bj2 cj2\naj3 bj3 cj3\n" +
        "ak1 bk1 ck1\nak2 bk2 ck2\nak3 bk3 ck3\n");
# diagonal wins top-bottom
f.write("ai1 bj1 ck1\nai2 bj2 ck2\nai3 bj3 ck3\n" +
        "ak1 bj1 ci1\nak2 bj2 ci2\nak3 bj3 ci3\n");
# diagonal wins left-right
f.write("ai1 bi2 ci3\naj1 bj2 cj3\nak1 bk2 ck3\n" +
        "ai3 bi2 ci1\naj3 bj2 cj1\nak3 bk2 ck1\n");
# diagonal wins corner-corner
f.write("ai1 bj2 ck3\nai3 bj2 ck3\n" + 
        "ak1 bj2 ci3\nak3 bj2 ci1\n");

#blackinitials
f.write("#whiteturns\n");
f.write(whiteinits);


f.close();

