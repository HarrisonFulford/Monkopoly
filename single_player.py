from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random
from pieces import pieceslist
from boardplaces import *
from chest import *
from dice import *
from Labels import *

def newmovefunc():
    dice1 = random.randint(8, 8)
    dice2 = random.randint(0,0)
    #two random dice
    for item in activedicelist:
        item.place_forget()
        #erases the list of the active dice from the screen (removes them)
    activedicelist.clear()
    #clears list of active dice
    for z in dicelist:
        if z.dicenum == dice1:
            #finds the dice images that are equal to the two things the person rolled
            z.dicelb.place(x=340, y=560)
            #places that labels
            activedicelist.append(z.dicelb)
            #adds it to the dice list so it can be remove next roll
        if z.dicenum == dice2:
            #same for second dice
            z.dicelb2.place(x=380, y=560)
            #places
            activedicelist.append(z.dicelb2)
            #adds to list
    inp = dice1 + dice2
    #the total amount the piece is moving is inp
    for x in pieceslist:
        if x.turn == 'yes':
            #finds who's turn it is from list of players
            if dice1 == dice2:
                #if the dice are the same
                global doubleslb
                doubleslb = Label(gui, text='DOUBLES!', height =1, width=10, bg='#D5E8D4', fg='green', font=('Cooper Std Black', 30))
                doubleslb.place(x=444, y =132)
                #places the doubles label on screen
            if dice1 != dice2:
                #if they are not the same
                doubleslb.config(text='')
                #clears text from doubles label so it cannot be seen
                if x.piecenumber == 2:
                    #if the piece is number from makes it 0 to reset order of pieces back to 0 (all pieces have had one turn_
                    x.piecenumber = 0
                newx = x.piecenumber - 1 #1
                #looks at the piece that just went and sets it turn to no below
                pieceslist[newx].turn = 'no'
                pieceslist[x.piecenumber].turn = 'yes'
                #sets the next piece's turn to yes

            x.boardnumber += inp
            #sets the pieces board number to its current board number plus the amount they rolled
            if x.boardnumber >= 40:
                x.boardnumber -= 40
                #if they have made one complete cycle set the boardnumber back to 0
                x.money += 200
                #add 200 to their money
                x.moneylabel.config(text=x.money)
                #configure the money label to reflect new amount

            for item in boardplaceslist:
                #for the list of board places
                if item.number == x.boardnumber:
                    #if the piece is on that board place
                    x.placex = item.cordx
                    x.placey = item.cordy
                    #sets piece coordinates to that boardplace's held coordinates
                    for y in pieceslist:
                        #for every piece
                        if y.boardnumber == x.boardnumber and x.boardnumber != 0 and x.name != y.name:
                            #if another piece is already on that boardplace displace the coordinates by 30 so both can be seen
                            if x.boardnumber <=10:
                                x.placey = y.placey - 30
                            if x.boardnumber >=11 and x.boardnumber <=20:
                                x.placex = y.placex + 30
                            if x.boardnumber >=21 and x.boardnumber <30:
                                x.placey = y.placey + 30
                            if x.boardnumber >=31:
                                x.placex = y.placex - 30
                            #display coordinates to prevent piece overlap
                    x.label.place(x = x.placex, y = x.placey)
                    #place the piece label and redraw on board to new place

                    if item.propertytype == 'chest':
                        #if that boardplace is a chest type
                        m = random.randint(0,12)
                        #chooses random number for random card
                        def chestbuttondestroy():
                            #executes command when the chest card button is clicked
                            chestbutton.destroy()
                            #destroys the button on screen
                            rollbut['state'] = NORMAL
                            #make the roll state normal which means the next player can roll.
                            x.money += chestlist[m].moneycom
                            #adds money or removes money if money is involved in card
                            x.moneylabel.config(text=x.money)
                            #changes that piece's money label
                            if chestlist[m].movecom != 'no':
                                # if there is movement
                                if x.boardnumber > chestlist[m].movecom:
                                    x.money += 200
                                    x.moneylabel.config(text=x.money)
                                    #if the piece is about to make one full rotation around the board and pass go add 200 to money
                                x.boardnumber = chestlist[m].movecom
                                #set the place on the board to the card's movement

                            if chestlist[m].movecom == '-3':
                                newxb = int(x.boardnumber) - 3
                                x.boardnumber = newxb
                                #go back three spaces
                                if x.boardnumber == 33:
                                    print('33') #if they land on the chance and go back three to the community chess just print 33 because that is not finished
                            for item in boardplaceslist:
                                if item.number == x.boardnumber:
                                    x.placex = item.cordx
                                    x.placey = item.cordy
                                    for y in pieceslist:
                                        if y.boardnumber == x.boardnumber and x.boardnumber != 0 and x.name != y.name:
                                            if x.boardnumber <=10:
                                                x.placey = y.placey - 30
                                            if x.boardnumber >=11 and x.boardnumber <=20:
                                                x.placex = y.placex + 30
                                            if x.boardnumber >=21 and x.boardnumber <30:
                                                x.placey = y.placey + 30
                                            if x.boardnumber >=31:
                                                x.placex = y.placex - 30
                                    x.label.place(x = x.placex, y = x.placey)
                                    #does the same place explained above
                        #m = random.randint(0,39)
                        if x.boardnumber == 2 or x.boardnumber == 17 or x.boardnumber == 33:
                            chestbutton = Button(gui, bg = 'brown', highlightbackground='brown', text=chestlist[m].lbtext, height=12, width=30, command=chestbuttondestroy)
                            chestbutton.place(x=300, y=270)
                            rollbut['state'] = DISABLED
                        #if it is a monkey bin makes the card brown

                        if x.boardnumber == 7 or x.boardnumber == 22 or x.boardnumber == 36:
                            chestbutton = Button(gui, bg = 'yellow', highlightbackground='yellow', text=chestlist[m].lbtext, height=12, width=30, command=chestbuttondestroy)
                            chestbutton.place(x=300, y=270)
                            rollbut['state'] = DISABLED
                        #if it is a health care hazard make it yellow
                    if item.propertytype == 'property':
                        #if a property
                        def passfunc():
                            propgui.destroy()
                            rollbut['state'] = NORMAL
                            #dont buy move on
                        def buyfunc():
                            rollbut['state'] = NORMAL
                            x.asset += item.cost
                            x.money -= item.cost
                            x.moneylabel.config(text=x.money)
                            propgui.destroy()
                            item.owner = x.piecenumber
                            #remove the money from account and close window
                            if x.boardnumber > 10 and x.boardnumber < 20:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx+110, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 30:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx-94, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 20 and x.boardnumber < 30:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy+106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 0 and x.boardnumber < 10:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy-106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side
                        if item.owner == 'no':
                            #if there is no owner to the property
                            rollbut['state'] = DISABLED
                            #disable the role button
                            propgui = tk.Toplevel()
                            propgui.geometry('800x608')
                            #make window
                            costlb = Label(propgui, text='$'+str(item.cost), height =1, width=10, font=('Cooper Std Black', 48))
                            costlb.place(x=508, y =1)
                            #add cost
                            newlb = tk.Label(propgui, image=item.label)
                            newlb.place(x=1, y=1)
                            buybutton = Button(propgui, text='buy', bg='green', highlightbackground='green',height=10, width=26, command=buyfunc)
                            buybutton.place(x=528, y=74)
                            #buy
                            passbutton = Button(propgui, text='pass', bg='red', highlightbackground='red',height=10, width=26, command=passfunc)
                            passbutton.place(x=528, y=304)
                            #pass
                            propgui.mainloop()
                        else:
                            if item.mortgaged == False:
                                print('this item is mortgaged')
                                g = item.owner - 1
                                pieceslist[g].money += item.rent0
                                x.money -= item.rent0
                                if x.money < 0:
                                    debt = 0 - x.money
                                    x.money = 0
                                    x.label.place(x=9999, y=9999)
                                    print('this player is in debt by ',debt)
                                    if x.asset < debt:
                                        print('they do not have enough to pay they are out')
                                #print(pieceslist[g].money)
                                #print(pieceslist[g].piecenumber)
                                x.moneylabel.config(text=x.money)
                                pieceslist[g].moneylabel.config(text=pieceslist[g].money)


                    if item.number == 4:
                        x.money -= 200
                        x.moneylabel.config(text=x.money)
                        #tax 200
                    if item.number == 38:
                        x.money -= 100
                        x.moneylabel.config(text=x.money)
                        #tax 100
                    if item.number == 30:
                        x.boardnumber = 10
                        x.label.place(x=60, y=660)
                        doubleslb.config(text='JAIL')
                        #jail
                    if item.propertytype == 'bus':
                        def passfunc():
                            busgui.destroy()
                            rollbut['state'] = NORMAL
                            #dont buy move on
                        def buyfunc():
                            x.busnumber += 1
                            rollbut['state'] = NORMAL
                            x.money -= item.cost
                            x.moneylabel.config(text=x.money)
                            busgui.destroy()
                            item.owner = x.piecenumber
                            #remove the money from account and close window
                            if x.boardnumber > 10 and x.boardnumber < 20:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx+110, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 30:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx-94, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 20 and x.boardnumber < 30:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy+106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 0 and x.boardnumber < 10:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy-106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side

                        if item.owner == 'no':
                            #if there is no owner to the property
                            rollbut['state'] = DISABLED
                            #disable the role button
                            busgui = tk.Toplevel()
                            busgui.geometry('800x608')
                            #make window
                            costlb = Label(busgui, text='$'+str(item.cost), height =1, width=10, font=('Cooper Std Black', 48))
                            costlb.place(x=508, y =1)
                            #add cost
                            newlb = tk.Label(busgui, image=item.label)
                            newlb.place(x=1, y=1)
                            buybutton = Button(busgui, text='buy', bg='green', highlightbackground='green',height=10, width=26, command=buyfunc)
                            buybutton.place(x=528, y=74)
                            #buy
                            passbutton = Button(busgui, text='pass', bg='red', highlightbackground='red',height=10, width=26, command=passfunc)
                            passbutton.place(x=528, y=304)
                            #pass
                            busgui.mainloop()
                        else:
                            g = item.owner - 1
                            if pieceslist[g].busnumber == 1:
                                minnum = item.rent0
                            if pieceslist[g].busnumber == 2:
                                minnum = item.rent1
                            if pieceslist[g].busnumber == 4:
                                minnum = item.rent3
                            if pieceslist[g].busnumber == 4:
                                minnum = item.rent3
                            pieceslist[g].money += minnum
                            x.money -= minnum
                            #print(pieceslist[g].money)
                            #print(pieceslist[g].piecenumber)
                            x.moneylabel.config(text=x.money)
                            pieceslist[g].moneylabel.config(text=pieceslist[g].money)
                    if item.propertytype == 'company':
                        def passfunc():
                            busgui.destroy()
                            rollbut['state'] = NORMAL
                            #dont buy move on
                        def buyfunc():
                            x.compnumber += 1
                            rollbut['state'] = NORMAL
                            x.money -= item.cost
                            x.moneylabel.config(text=x.money)
                            busgui.destroy()
                            item.owner = x.piecenumber
                            #remove the money from account and close window
                            if x.boardnumber > 10 and x.boardnumber < 20:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx+110, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 30:
                                for line in x.vertcolour:
                                    line.place(x=item.cordx-94, y=item.cordy-16)
                                    x.vertcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 20 and x.boardnumber < 30:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy+106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side
                            elif x.boardnumber > 0 and x.boardnumber < 10:
                                for line in x.horcolour:
                                    line.place(x=item.cordx-16, y=item.cordy-106)
                                    x.horcolour.remove(line)
                                    #add the line to the right side

                        if item.owner == 'no':
                            #if there is no owner to the property
                            rollbut['state'] = DISABLED
                            #disable the role button
                            busgui = tk.Toplevel()
                            busgui.geometry('800x608')
                            #make window
                            costlb = Label(busgui, text='$'+str(item.cost), height =1, width=10, font=('Cooper Std Black', 48))
                            costlb.place(x=508, y =1)
                            #add cost
                            newlb = tk.Label(busgui, image=item.label)
                            newlb.place(x=1, y=1)
                            buybutton = Button(busgui, text='buy', bg='green', highlightbackground='green',height=10, width=26, command=buyfunc)
                            buybutton.place(x=528, y=74)
                            #buy
                            passbutton = Button(busgui, text='pass', bg='red', highlightbackground='red',height=10, width=26, command=passfunc)
                            passbutton.place(x=528, y=304)
                            #pass
                            busgui.mainloop()
                        else:
                            g = item.owner - 1
                            if pieceslist[g].compnumber == 1:
                                if item.number == 12:
                                    minnum = inp * 5
                                if item.number == 28:
                                    minnum = inp * 10
                            if pieceslist[g].compnumber == 2:
                                minnum = inp * 10
                            pieceslist[g].money += minnum
                            x.money -= minnum
                            #print(pieceslist[g].money)
                            #print(pieceslist[g].piecenumber)
                            x.moneylabel.config(text=x.money)
                            pieceslist[g].moneylabel.config(text=pieceslist[g].money)
            break
def managefunc():
    propimagelist = []
    coordslist = [0, 0]
    buttonpluscoordlist = [75, 175]
    buttonmincoordlist = [33, 175]
    buttonpluslist = []
    buttonminlst = []
    coordsycounter = 0
    managegui.deiconify()
    for x in pieceslist:
        if x.turn == 'no':
            for item in boardplaceslist:
                #print(item.owner, x.piecenumber)
                if item.owner == x.piecenumber:
                    #print('func2')
                    propimagelist.append(item.smallerlabel)
                    break
            break
    def mortgagefunc():
        if item.mortgaged == False:
            item.mortgaged = True
            print(item.number)
            x.money += item.rent0 * 7
            x.moneylabel.config(text=x.money)
            mortgagebutton.config(text='unmortgage')
            print('i mortgaged')
        elif item.mortgaged == True:
            item.mortgaged = False
            x.money -= item.rent0 * 8
            x.moneylabel.config(text=x.money)
            print('i unmortgaged')
            mortgagebutton.config(text='mortgage')


    def minfunc():
        print('min')
        if item.housenumber == 0:
            pass
        else:
            print('second min')
            item.housenumber -= 1
            if item.number < 10:
                if item.housenumber == 0:
                    print('removed all houses')
                else:
                    for q in range(1, item.housenumber):
                        for treelb in treelist:
                            treelb.place(x=item.cordx, y=item.cordy+40)

    def plusfunc():
        for item in boardplaceslist:
            if item.smallerlabel == im:
                item.housenumber += 1
                if item.number > 0 and item.number < 10:
                    print(item.number)
                    if item.housenumber == 5:
                        print('hotel')
                    else:
                        o = 90
                        for q in range(0, item.housenumber):
                            for treelb in treelist:
                                treelb.place(x=item.cordx+o, y=item.cordy-75)
                                treelist.remove(treelb)
                                o + 20
                                break
                if item.number > 10 and item.number < 20:
                    if item.housenumber == 5:
                        print('hotel')
                    else:
                        o = 90
                        for q in range(0, item.housenumber):
                            for treelb in treelist:
                                treelb.place(x=item.cordx+75, y=item.cordy-o)
                                treelist.remove(treelb)
                                o += 20
                if item.number > 20 and item.number < 30:
                    if item.housenumber == 5:
                        print('hotel')
                    else:
                        o = 90
                        for q in range(0, item.housenumber):
                            for treelb in treelist:
                                treelb.place(x=item.cordx-o, y=item.cordy-75)
                                treelist.remove(treelb)
                                o += 20
                if item.number > 30:
                    if item.housenumber == 5:
                        print('hotel')
                    else:
                        o = 90
                        for q in range(0, item.housenumber):
                            for treelb in treelist:
                                treelb.place(x=item.cordx+75, y=item.cordy+o)
                                treelist.remove(treelb)
                                o += 20



    for im in propimagelist:
        print('ok')
        im.place(x=coordslist[0], y=coordslist[1])
        minbutton = Button(managegui, height=1, width=1, text='-1', command=minfunc)
        minbutton.place(x=buttonmincoordlist[0], y=buttonmincoordlist[1])
        plusbutton = Button(managegui, height=1, width=1, text='+1', command=plusfunc)
        plusbutton.place(x=buttonpluscoordlist[0], y=buttonpluscoordlist[1])
        if item.mortgaged == True:
            text = 'unmortgage'
        else: text = 'mortgage'
        mortgagebutton = Button(managegui, height=1, width=6, text=text, command=mortgagefunc)
        mortgagebutton.place(x=buttonmincoordlist[0], y=buttonmincoordlist[1]+22)
        coordslist[0] += 155
        buttonmincoordlist[0] += 155
        buttonpluscoordlist[0] += 155
        coordsycounter += 1
        if coordsycounter == 5 or coordsycounter == 10:
            coordslist[1] += 210
            coordslist[0] = 1
            buttonmincoordlist[1] += 210
            buttonpluscoordlist[1] += 210
            buttonmincoordlist[0] = 33
            buttonpluscoordlist[0] = 65
    managegui.mainloop()
playerturngui = Tk()
playerturngui.geometry('350x200+300+300')
playerturngui.title('Player Turn')
#players turn gui with controls
rollbut = Button(playerturngui, height=5, width=5, text='roll', command=newmovefunc)
rollbut.place(x = '1', y = '1')

managepropbutton = Button(playerturngui, height=5, width=5, text='manage', command=managefunc)
managepropbutton.place(x='100', y='1')
#he roll button

#lb.place(x='100', y='1')
def destroyfunc():
    gui.destroy()
    playerturngui.destroy()
    #if they close the board tkinter window closes all tkinter windows

gui.resizable(False, False)
playerturngui.resizable(False, False)
#does not allow either window to be resized
def nah():
    pass
    #does not allow the player control gui to be closed
playerturngui.wm_protocol("WM_DELETE_WINDOW", nah) #command in nah which does nothing when they try to close player control window
gui.wm_protocol("WM_DELETE_WINDOW", destroyfunc) #if they close board window execute above command to close all windows
playerturngui.mainloop() #mainloop
gui.mainloop()
