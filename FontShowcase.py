from tkinter import * 
import tkinter.font as tkFont


root = Tk()
root.title("FontShowcase")

listnum = 0

def fontname( key = 0 ):
    global listnum
    listnum += key

    if listnum >= len( tkFont.families() ):
        listnum = 0

    text = tkFont.families()[ listnum ]
    return text

def conftext(key):
    text = fontname(key)
    fontna.configure( text = text )
    fontexam.configure( font = ( str( text ) , 20 ) )
    fontexam2.configure( font = ( str( text ) , 20 ) )
    fontexam3.configure( font = ( str( text ) , 20 ) )
    return




fontna    = Label( root , text = str( fontname() ) , font = ( 20 )  )
fontexam  = Label( root , text = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" , font = ( fontname() , 20 ) )
fontexam2 = Label( root , text = "a b c d e f g h i j k l m n o p q r s t u v w x y z" , font = ( fontname() , 20 ) )
fontexam3 = Label( root , text = "1 2 3 4 5 6 7 8 9" , font = ( fontname() , 20 ) )

nextbut     = Button( root , text = "Next" , command = lambda:conftext( 1 ) )
previousbut = Button( root , text = "Previous" , command = lambda:conftext( -1 ) )

fontna.grid( row = 0 , column = 2 )
fontexam.grid( row = 1 , column = 2 )
fontexam2.grid( row = 2 , column = 2 )
fontexam3.grid( row = 3 , column = 2 )

nextbut.grid( row = 2 , column = 4 )
previousbut.grid( row = 2 , column = 0) 



     
root.mainloop()