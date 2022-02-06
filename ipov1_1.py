from tkinter import *
from PIL import Image
import sqlite3
import tksheet

root =Tk()
root.title('IPO MANAGEMENT SYSTEM V1.2')
#root.iconbitmap('/home/muglu/Personal/DataBase/project/IPO Test/ipo.ico')
root.config(bg="#516395")
root.geometry("700x540")
#Databases




#Create a databse or connect to one
conn= sqlite3.connect('IPO_DB.db')

#create cursor

c= conn.cursor()

#Create Table
'''
c.execute(""" CREATE TABLE ipo_database(
        issuer_company text,
        exchange text,
        open_date numeric,
        close_date numeric,
        lot_size integer,
        issue_price integer, 
        issue_size integer
        )""")
'''

global issuer_company_editor
global exchange_editor
global open_date_editor
global close_date_editor
global lot_size
global issue_price_editor
global issue_size_editor


def submit():
        #Create a databse or connect to one
        conn= sqlite3.connect('IPO_DB.db')

        #create cursor

        c= conn.cursor()
        
        # Insert Into Table
        c.execute("INSERT INTO ipo_database VALUES(:issuer_company, :exchange, :open_date, :close_date, :lot_size, :issue_price, :issue_size)",
        {
                'issuer_company': issuer_company.get(),
                'exchange': exchange.get(),
                'open_date': open_date.get(),
                'close_date': close_date.get(),
                'lot_size': lot_size.get(),
                'issue_price':issue_price.get(),
                'issue_size' :issue_size.get()
       })

        #Commit Changes
        conn.commit()



        #Close Connection
        conn.close()




        #clear text Boxes
        issuer_company.delete(0,END)
        exchange.delete(0,END)
        open_date.delete(0,END)
        close_date.delete(0,END)
        lot_size.delete(0,END)
        issue_price.delete(0,END)
        issue_size.delete(0,END)
        
def show_data():
    
    show= Tk()
    show.title('Records')
    show.geometry("1080x1440")
    show.config(bg="#516395")
     #Create a databse or connect to one
    conn= sqlite3.connect('IPO_DB.db')

            #create cursor

    c= conn.cursor()

            #Query the database
    c.execute("SELECT *, oid FROM ipo_database")
    records = c.fetchall()
            #print(records)

            #Results through LOOP
    # print_records= ''
    # for record in records:
    #     print_records += str(record)+"\n "
            
    # query_label = Label(show, text=print_records)
    # query_label.grid(row=5, column=0, columnspan=2)



    space_label= Label(show, text="")
    space_label.grid(row=0, column=0)
    space_label.config(bg="#516395")

    space_label2= Label(show, text="")
    space_label2.grid(row=0, column=1)
    space_label2.config(bg="#516395")

    #head_name_label= Label(show, text="Your data in Records")
    #head_name_label.grid(row=0, column=3, columnspan=1, rowspan=2 )
    #head_name_label.config(font =("Courier", 25))


    space_label0= Label(show, text="")
    space_label0.grid(row=1, column=0)
    space_label0.config(bg="#516395")

    space_label1= Label(show, text="")
    space_label1.grid(row=2, column=0)
    space_label1.config(bg="#516395")

    space_label4= Label(show, text="")
    space_label4.grid(row=3, column=0)
    space_label4.config(bg="#516395")

    print_records1= ''
    for record in records:
         print_records1 += str(record[7])+"\n "


    sl_no= Label(show, text="Serial Number")
    sl_no.grid(row=3, column=1,padx=4)
    sl_no.config(bg="#516395",font=('FreeSerif',18))

    space_label6= Label(show, text="")
    space_label6.grid(row=4, column=0,padx=4)
    space_label6.config(bg="#516395")

    space_label7= Label(show, text="")
    space_label7.grid(row=5, column=0)
    space_label7.config(bg="#516395")
            
    sl_no = Label(show, text=print_records1)
    sl_no.grid(row=5, column=1,padx=4)
    sl_no.config(bg="#516395")

    print_records2= ''
    for record in records:
         print_records2 += str(record[0])+"\n "

    issuer_company_label = Label(show,text="Issuer company")
    issuer_company_label.grid(row=3, column=2,padx=4)
    issuer_company_label.config(bg="#516395",font=("FreeSerif", 18))


    issuer_company_label1 = Label(show, text=print_records2)
    issuer_company_label1.grid(row=5, column=2,padx=4)
    issuer_company_label1.config(bg="#516395")


    print_records3= ''
    for record in records:
         print_records3 += str(record[1])+"\n "

    exchange_label = Label(show,text="Exchange")
    exchange_label.grid(row=3, column=3,padx=4)
    exchange_label.config(bg="#516395",font=("FreeSerif", 18))



    exchange_label1 = Label(show, text=print_records3)
    exchange_label1.grid(row=5, column=3,padx=4)
    exchange_label1.config(bg="#516395")


    print_records4= ''
    for record in records:
         print_records4 += str(record[2])+"\n "

    open_date_label = Label(show,text="Opening Date")
    open_date_label.grid(row=3, column=4,padx=4)
    open_date_label.config(bg="#516395",font=("FreeSerif", 18))


    open_date_label1 = Label(show, text=print_records4)
    open_date_label1.grid(row=5, column=4,padx=4)
    open_date_label1.config(bg="#516395")


    print_records5= ''
    for record in records:
         print_records5 += str(record[3])+"\n "

    close_date_label = Label(show,text="Closing Date")
    close_date_label.grid(row=3, column=5,padx=4)
    close_date_label.config(bg="#516395",font=("FreeSerif", 18))



    close_date_label1 = Label(show, text=print_records5)
    close_date_label1.grid(row=5, column=5,padx=4)
    close_date_label1.config(bg="#516395")


    print_records6= ''
    for record in records:
         print_records6 += str(record[4])+"\n "

    lot_size_label = Label(show,text="Lot Size")
    lot_size_label.grid(row=3, column=6,padx=4)
    lot_size_label.config(bg="#516395",font=("FreeSerif", 18))

    lot_size_label1 = Label(show, text=print_records6)
    lot_size_label1.grid(row=5, column=6,padx=4)
    lot_size_label1.config(bg="#516395")


    print_records7= ''
    for record in records:
         print_records7 += str(record[5])+"\n "

    issue_price_label = Label(show,text="Issue Price (In Crore)")
    issue_price_label.grid(row=3, column=7,padx=4)
    issue_price_label.config(bg="#516395",font=("FreeSerif", 18))


    issue_price_label1 = Label(show, text=print_records7)
    issue_price_label1.grid(row=5, column=7,padx=4)
    issue_price_label1.config(bg="#516395")


    print_records8= ''
    for record in records:
         print_records8 += str(record[6])+"\n "

    issue_size_label = Label(show,text="Issue Size (In Crore)")
    issue_size_label.grid(row=3, column=8,padx=4)
    issue_size_label.config(bg="#516395",font=("FreeSerif", 18))

    issue_size_label1 = Label(show, text=print_records8)
    issue_size_label1.grid(row=5, column=8,padx=4)
    issue_size_label1.config(bg="#516395")


    #commit changes
    conn.commit()
    #close Connection
    conn.close()


    show.mainloop()

def delete():
      #Create a databse or connect to one
        conn= sqlite3.connect('IPO_DB.db')

        #create cursor

        c= conn.cursor()

        #Delete from records

        c.execute("DELETE from ipo_database WHERE oid="+ delete_box.get())

        delete_box.delete(0, END)





        #commit changes
        conn.commit()
        #close Connection
        conn.close()


#Create a function to update a record

def edit():
    editor =Tk()
    editor.title('Update your Records')
    #root.iconbitmap('/home/muglu/Personal/DataBase/project/IPO Test/ipo.ico')
    editor.config(bg="#6dd5ed")
    editor.geometry("700x540")

    #Create a databse or connect to one
    conn= sqlite3.connect('IPO_DB.db')

    #create cursor

    c= conn.cursor()

    record_id= delete_box.get()

    # Create global Variables for the text boxes
    global issuer_company_editor
    global exchange_editor
    global open_date_editor
    global close_date_editor
    global lot_size_editor
    global issue_price_editor
    global issue_size_editor

    #Query to copy database from records to edit
    c.execute("SELECT * FROM ipo_database WHERE oid = " + record_id)
    
    records =  c.fetchall()

    issuer_company_editor = Entry(editor,width=30)
    issuer_company_editor.grid(row=1, column=1, padx=20, pady=(10,0))

    exchange_editor = Entry(editor,width=30)
    exchange_editor.grid(row=2, column=1, pady=(10,0))

    open_date_editor = Entry(editor,width=30)
    open_date_editor.grid(row=3, column=1, pady=(10,0))

    close_date_editor = Entry(editor,width=30)
    close_date_editor.grid(row=4, column=1, pady=(10,0))

    lot_size_editor = Entry(editor,width=30)
    lot_size_editor.grid(row=5, column=1, pady=(10,0))


    issue_price_editor  = Entry(editor,width=30)
    issue_price_editor.grid(row=6, column=1, pady=(10,0))

    issue_size_editor  = Entry(editor,width=30)
    issue_size_editor.grid(row=7, column=1, pady=(10,0))
    
    #Create Label Boxes

    head_name_label= Label(editor, text="Update your data in Records")
    head_name_label.grid(row=0, column=0, columnspan=3, pady=18, padx=18,ipadx=130)
    head_name_label.config(bg="#6dd5ed")

    issuer_company_label = Label(editor,text="Enter Issuer company")
    issuer_company_label.grid(row = 1, column=0, pady=(10,0))
    issuer_company_label.config(bg="#6dd5ed")

    exchange_label = Label(editor,text="Exchange")
    exchange_label.grid(row = 2, column=0, pady=(10,0))
    exchange_label.config(bg="#6dd5ed")

    open_date_label = Label(editor,text="Enter Open Date")
    open_date_label.grid(row = 3, column=0, pady=(10,0))
    open_date_label.config(bg="#6dd5ed")

    close_date_label = Label(editor,text="Enter Close Date")
    close_date_label.grid(row = 4, column=0, pady=(10,0))
    close_date_label.config(bg="#6dd5ed")

    lot_size_label = Label(editor,text="Enter Lot Size")
    lot_size_label.grid(row= 5, column=0, pady=(10,0))
    lot_size_label.config(bg="#6dd5ed")

    issue_price_label = Label(editor,text="Enter Issue Price (In Crore)")
    issue_price_label.grid(row = 6, column=0, pady=(10,0))
    issue_price_label.config(bg="#6dd5ed")

    issue_size_label = Label(editor,text="Enter Issue Size (In Crore)")
    issue_size_label.grid(row = 7, column=0, pady=(10,0))
    issue_size_label.config(bg="#6dd5ed")

    space_label0= Label(editor, text="")
    space_label0.grid(row=8, column=0)
    space_label0.config(bg="#6dd5ed")

    space_label1= Label(editor, text="")
    space_label1.grid(row=9, column=0)
    space_label1.config(bg="#6dd5ed")

    for record in records:

        issuer_company_editor.insert(0, record[0])

        exchange_editor.insert(0, record[1])

        open_date_editor.insert(0, record[2])

        close_date_editor.insert(0, record[3])

        lot_size_editor.insert(0, record[4])

        issue_price_editor.insert(0, record[5])

        issue_size_editor.insert(0, record[6])

    update_btn= Button(editor, text="Update Record", command=update)
    update_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=136)


 #clear text Boxes
   # issuer_company_editor.delete(0,END)
    #exchange_editor.delete(0,END)
   # open_date_editor.delete(0,END)
   # close_date_editor.delete(0,END)
   # lot_size_editor.delete(0,END)
   # issue_price_editor.delete(0,END)

def update():
    #Create a databse or connect to one
        conn= sqlite3.connect('IPO_DB.db')

        #create cursor

        c= conn.cursor()

       
        record_id = delete_box.get()
        c.execute("""UPDATE ipo_database SET
                issuer_company = :company,
                exchange = :exch,
                open_date = :odate,
                close_date = :cdate,
                lot_size = :l_size,
                issue_price = :iprice,
                issue_size = :isize
            WHERE oid = :oid""",
            {
            'company': issuer_company_editor.get(),
            'exch': exchange_editor.get(),
            'odate' : open_date_editor.get(),
            'cdate' : close_date_editor.get(),
            'l_size' :lot_size_editor.get(),
            'iprice' : issue_price_editor.get(), 
            'isize' : issue_size_editor.get(),

            'oid' : record_id
            })

    #commit changes
        conn.commit()
        #close Connection
        conn.close()
         #clear text Boxes
        issuer_company_editor.delete(0,END)
        exchange_editor.delete(0,END)
        open_date_editor.delete(0,END)
        close_date_editor.delete(0,END)
        lot_size_editor.delete(0,END)
        issue_price_editor.delete(0,END)
        issue_size_editor.delete(0,END)


#Input Boxes
issuer_company = Entry(root,width=30)
issuer_company.grid(row=1, column=1, padx=20, pady=(10,0))

exchange = Entry(root,width=30)
exchange.grid(row=2, column=1, pady=(10,0))

open_date = Entry(root,width=30)
open_date.grid(row=3, column=1, pady=(10,0))

close_date = Entry(root,width=30)
close_date.grid(row=4, column=1, pady=(10,0))

lot_size = Entry(root,width=30)
lot_size.grid(row=5, column=1, pady=(10,0))


issue_price  = Entry(root,width=30)
issue_price.grid(row=6, column=1, pady=(10,0))

issue_size= Entry(root, width=30)
issue_size.grid(row=7, column=1, pady=(10,0))

space_label2= Label(root, text="")
space_label2.grid(row=8, column=1)

space_label3= Label(root, text="")
space_label3.grid(row=9, column=1)


delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, pady=(10,0))

#Create Text Box Labels
head_name_label= Label(root, text="New IPO released in 2021 Database System")
head_name_label.grid(row=0, column=0, columnspan=3, pady=18, padx=18,ipadx=130)
head_name_label.config(bg="#516395", font="Arial")

issuer_company_label = Label(root,text="Enter Issuer company")
issuer_company_label.grid(row = 1, column=0, pady=(10,0))
issuer_company_label.config(bg="#516395")


exchange_label = Label(root,text="Exchange")
exchange_label.grid(row = 2, column=0, pady=(10,0))
exchange_label.config(bg="#516395")

open_date_label = Label(root,text="Enter Open Date")
open_date_label.grid(row = 3, column=0, pady=(10,0))
open_date_label.config(bg="#516395")

close_date_label = Label(root,text="Enter Close Date")
close_date_label.grid(row = 4, column=0, pady=(10,0))
close_date_label.config(bg="#516395")

lot_size_label = Label(root,text="Enter Lot Size")
lot_size_label.grid(row= 5, column=0, pady=(10,0))
lot_size_label.config(bg="#516395")

issue_price_label = Label(root,text="Enter Issue Price (In Crore)")
issue_price_label.grid(row = 6, column=0, pady=(10,0))
issue_price_label.config(bg="#516395")

issue_size_label = Label(root,text="Enter Issue Size (In Crore)")
issue_size_label.grid(row = 7, column=0, pady=(10,0))
issue_size_label.config(bg="#516395")

space_label0= Label(root, text="")
space_label0.grid(row=8, column=0)
space_label0.config(bg="#516395")

space_label1= Label(root, text="")
space_label1.grid(row=9, column=0)
space_label1.config(bg="#516395")

delete_box_label= Label(root, text="Delete ID")
delete_box_label.grid(row=10, column=0, pady=(10,0))
delete_box_label.config(bg="#516395")


#Create Submit Button

submit_btn= Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10,ipadx=100)

#Create Show Records Button

show_btn= Button(root, text="Show Records", command=show_data)
show_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a delete Button


# space_label1= Label(root, text="")
# space_label1.grid(row=10, column=0)

# space_label1= Label(root, text="")
# space_label1.grid(row=11, column=0)

del_btn= Button(root, text="Delete Records", command=delete)
del_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

#Create a edit button

edit_btn= Button(root, text="Edit Records", command=edit)
edit_btn.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=136)


#Commit Changes
conn.commit()



#Close Connection
conn.close()





root.mainloop()