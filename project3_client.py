#name :- Nirmit Rajeshbhai shah
#Mavid:- 1001772180
#email:- nirmitrajeshbha.shah@mavs.uta.edu
from tkinter import * #Got refrences of the below line from (https://pythonprogramming.net/python-3-tkinter-basics-tutorial/)
from socket import *  #Got refrences of the bline from (https://www.geeksforgeeks.org/socket-programming-python/)  I have modified in my way to get access of all the methods
from random import *  # slightly modified https://www.geeksforgeeks.org/python-randint-function/
import threading      # Got th refences from https://realpython.com/intro-to-python-threading/
import tkinter.scrolledtext as scroll
client_username_textbox="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label1=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label2=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_connect_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
socket_object=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_create_directory_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
username=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_create_directory_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_directory_list_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_rename_old=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_rename_textbox_old=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_rename_new=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_rename_textbox_new=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_directory_rename_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_rename_answer=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_move_old=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_move_textbox_old=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_move_new=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_move_textbox_new=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_directory_move_button=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_move_answer=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_directory_list_button=""
client_label_delete=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_textbox_delete=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_button_delete=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_username_label_delete_answer=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
title=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_screen=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
client_button_close=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
master_screen=""  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_username_label2=""
server_label_move=""
server_textbox_move=""
server_button_move=""
server_label_move_answer=""
server_label_delete=""  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
server_textbox_delete=""  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
server_button_delete=""  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
client_label_log=""
client_textbox_log=""
client_button_log=""
logarea=""
#==================================Defining The methods for the connection====================

def server_client_connect():
    global logarea
    global client_username_label_rename_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_rename_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_rename_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/ 
    global client_rename_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_directory_rename_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_textbox  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_directory_list_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label1  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_connect_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label  # accessing the global v ariable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_rename_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_create_directory_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global socket_object  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_username_label2
    global client_username_label_move_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_move_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global   client_username_label_move_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global   client_move_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global    client_directory_move_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global    client_username_label_move_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_button_close  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_label_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_textbox_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_button_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global master_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_directory_list_button
    global  server_label_move
    global  server_textbox_move
    global  server_button_move
    global server_label_move_answer
    global client_label_log
    global client_textbox_log
    global client_button_log
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 #define the port in the variable
    socket_object.connect(('127.0.1.3', port))# got the refence from https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
    data=client_username_textbox.get() #get the name from the textbox
    decision="pass" #checking condition
    sum_data="" # to stoe the result of  the find
    arr=["1","2","3","4","5","6","7","8","9","0",".","/",";","{","}","/","*","-","+","!","@",'#',"$","&","(",")","-","_","=","`","~","?","<",">",".",":",";","[","]","|"] #an list of all the number,special char and symbols
    for a in arr: #parsing through the list
        sum_data=data.find(a) # checking if any char exist or not
        if sum_data >=0: # if there is noo special symbol then the value will be -1 and never in the loop
            decision="fail"
            break;
    if decision== "pass": #if there is no symbols then only it will go into this loop
        socket_object.send(bytes(data + "", "utf-8"))#https://stackoverflow.com/questions/34653875/python-how-to-send-data-over-tcp/34655152
        info=socket_object.recv(1024) # got the refence from https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
        info1=info.decode("utf-8")   # got the refence from https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
        print(info1) 
        received_info=info1.split(";") #split the message received from the server
        username=received_info[1] # at the second location there will be username
        text1=received_info[0] # at first location message will be there
        client_username_label1.configure(text=text1 ) #modifying the value of the label
        client_screen.title(username) #change the title of the window
        if(received_info[0]=="Successfull"): 
            print("djadl")
            client_create_directory_button.place(x=100, y=150,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_directory_list_button.place(x=100, y=200,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            server_directory_list_button.place(x=360, y=200,height=40, width=250) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_username_label_rename_old.place(x=100, y=250)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
            client_rename_textbox_old.place(x=230, y=250,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_username_label_rename_new.place(x=422, y=250)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
            client_rename_textbox_new.place(x=542, y=250,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_directory_rename_button.place(x=760, y=250,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_username_label_move_old.place(x=100, y=355)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
            client_move_textbox_old.place(x=230, y=355,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_username_label_move_new.place(x=422, y=355)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
            client_move_textbox_new.place(x=542, y=355,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_directory_move_button.place(x=760, y=355,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_label_delete.place(x=100, y=455)# Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
            server_label_move.place(x=610, y=455)
            client_textbox_delete.place(x=240, y=455,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_button_delete.place(x=430, y=455,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            
            client_label_log.place(x=520, y=100,height=40, width=80)
            client_textbox_log.place(x=605, y=100,height=40, width=70)
            client_button_log.place(x=615, y=200,height=40, width=100) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            server_textbox_move.place(x=750, y=455,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            server_button_move.place(x=930, y=455,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            logarea.place(x=944, y=200,height=240, width=470)
            client_button_close.place(x=130, y=100,height=40, width=180) # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
            client_connect_button.place_forget()#got the refrence from https://www.geeksforgeeks.org/place_forget-method-using-tkinter-in-python/   
            client_username_label.place_forget()#got the refrence from https://www.geeksforgeeks.org/place_forget-method-using-tkinter-in-python/   
            client_username_textbox.place_forget()#got the refrence from https://www.geeksforgeeks.org/place_forget-method-using-tkinter-in-python/   
    else:
        client_username_label1.configure(text="Invalid Format" )
        
def create_directory_connect(self):
    global logarea
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global  client_username_label1  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/ 
    dem1=client_username_label1.cget("text")  
    print(client_screen.title())
    dem2=str(client_screen.title())
    print("CURRENT TITLE:= ", dem2)
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234# Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port)) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    
    finaldata="directory;"+dem2
    print(finaldata)
    socket_object.send(bytes(finaldata+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
def create_directory_list(self):
    global logarea
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port))  # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    finaldata="list;"+username
    print(finaldata)
    socket_object.send(bytes(finaldata+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    info=socket_object.recv(1024)
    info1=info.decode("utf-8")
    print(info1)
    received_info=info1.split(";")
    if(received_info[0]=="lists"):
        text3=received_info[1]
        client_username_label2.configure(text=text3 )
        print(received_info[2])
        log_details=str(received_info[2])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
#==========================================SERVER FILES
def server_directory_list(self):
    global logarea
    global server_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port))  # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    finaldata="slist;"+username
    print(finaldata)
    socket_object.send(bytes(finaldata+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    info=socket_object.recv(1024)
    info1=info.decode("utf-8")
    print(info1)
    received_info=info1.split(";")
    if(received_info[0]=="slists"):
        text3=received_info[1]
        server_username_label2.configure(text=text3 )
        log_details=str(received_info[2])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
def directory_rename(self):
    global logarea
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_rename_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_rename_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port)) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    old_value=client_rename_textbox_old.get() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    new_value=client_rename_textbox_new.get() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    send_data="rename"+";"+old_value+";"+new_value+";"+username #all the send_data variable is the way the operation request has been sent to the server and also attaching the username with it so the server know which user has send the request
    socket_object.send(bytes(send_data+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    
    info=socket_object.recv(1024) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    print("info",info) 
    info1=info.decode("utf-8") #done the changes in my way https://www.tutorialspoint.com/python/string_decode.htm 
    print(info1)
    received_info=info1.split(";")
    username=received_info[4]
    if(received_info[0]=="frename"): 
        print("fail rename")
        client_username_label_rename_answer.configure(text="Same name folder exist")
        client_username_label_rename_answer.place(x=100, y=300)
        log_details=str(received_info[5])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
    elif received_info[0]=="srename":
        client_username_label_rename_answer.configure(text="Sucessfully Directory Renamed")
        client_username_label_rename_answer.place(x=100, y=300)
        log_details=str(received_info[5])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
def directory_move(self):
    global logarea
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_move_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_move_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port))  # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    old_value=client_move_textbox_old.get() #getting the old value
    new_value=client_move_textbox_new.get() #getting the new value
    send_data="move"+";"+old_value+";"+new_value+";"+username #as described above
    socket_object.send(bytes(send_data+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    info=socket_object.recv(1024) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    print("info",info)
    info1=info.decode("utf-8") #done the changes in my way https://www.tutorialspoint.com/python/string_decode.htm  
    print(info1)
    received_info=info1.split(";")# ALL THE INFO VARIABLE WILL RECIEVE THE MESSAGE FROM THE SERVER AND WILL SPLIT IT ON THE BASIS OF THE ; AND IT HAS BEEN SENT IN A PARTICULAR STRUCTURED WAY
    username=received_info[4]
    if(received_info[0]=="fmove"):
        print("fail move")
        client_username_label_move_answer.configure(text="Some problem occured")
        client_username_label_move_answer.place(x=100, y=400)
        log_details=str(received_info[5])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
    elif received_info[0]=="smove":
         client_username_label_move_answer.configure(text="Sucessfully Directory moved")
         client_username_label_move_answer.place(x=100, y=400)
         log_details=str(received_info[5])
         print(log_details)
         logarea.delete("1.0","end")
         logarea.insert(INSERT,log_details)
def server_directory_move(self):
    global logarea
    global  server_label_move
    global  server_textbox_move
    global  server_button_move
    global server_label_move_answer
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port))  # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    old_value=server_textbox_move.get() #getting the old value
    send_data="smove"+";"+old_value+";"+username #as described above
    socket_object.send(bytes(send_data+ "","utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    info=socket_object.recv(1024) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    print("info",info)
    info1=info.decode("utf-8") #done the changes in my way https://www.tutorialspoint.com/python/string_decode.htm  
    print(info1)
    received_info=info1.split(";")# ALL THE INFO VARIABLE WILL RECIEVE THE MESSAGE FROM THE SERVER AND WILL SPLIT IT ON THE BASIS OF THE ; AND IT HAS BEEN SENT IN A PARTICULAR STRUCTURED WAY
    username=received_info[1]
    if(received_info[0]=="ffmove"):
        print("fail move")
        server_label_move_answer.configure(text="Some problem occured")
        server_label_move_answer.place(x=570, y=500)
        log_details=str(received_info[2])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
    elif received_info[0]=="ssmove":
         server_label_move_answer.configure(text="Sucessfully Directory Downloaded")
         server_label_move_answer.place(x=570, y=500)
         log_details=str(received_info[2])
         print(log_details)
         logarea.delete("1.0","end")
         logarea.insert(INSERT,log_details)
    
def directory_delete(self):
    global logarea
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_textbox_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_delete_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port)) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    delete_value=client_textbox_delete.get() 
    send_data="delete"+";"+delete_value+";"+username
    socket_object.send(bytes(send_data,"utf-8"))
    info=socket_object.recv(1024)
    print("info",info)
    info1=info.decode("utf-8")
    print(info1)
    received_info=info1.split(";")
    username=received_info[1]
    if(received_info[0]=="fdelete"):
        print("fail move")
        client_username_label_delete_answer.configure(text="Some problem occured")
        client_username_label_delete_answer.place(x=100, y=500)
        log_details=str(received_info[2])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
    elif received_info[0]=="sdelete":
        client_username_label_delete_answer.configure(text="Sucessfully Directory Discynchronized ")
        client_username_label_delete_answer.place(x=100, y=500)
        log_details=str(received_info[2])
        print(log_details)
        logarea.delete("1.0","end")
        logarea.insert(INSERT,log_details)
def log_operation(self):
    global client_textbox_log
    global username
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port)) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    log_value=str(client_textbox_log.get())
    send_data="log"+";"+log_value+";"+username
    print("send data", send_data)
    socket_object.send(bytes(send_data,"utf-8"))
    info=socket_object.recv(1024)
    info1=info.decode("utf-8") #done the changes in my way https://www.tutorialspoint.com/python/string_decode.htm 
    print(info1)
    received_info=info1.split(";")
    username=received_info[1]
    print("Done", username)
    
def window_close(self):
    global logarea
    global client_button_close  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global master_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    socket_object = socket() # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    port=1234 # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    socket_object.connect(('127.0.1.3', port)) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    send_data="close"+";"+username 
    socket_object.send(bytes(send_data,"utf-8")) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    info=socket_object.recv(1024) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
    print("info",info)
    info1=info.decode("utf-8")
    print(info1)
    
    # print("info",info)
    # info1=info.decode("utf-8")
    # print(info1)
    received_info=info1.split(";")
    username=received_info[1] #all the received info in seprate function consits the information send from the server in the list form
    client_screen.destroy()  #got the refence from https://www.tutorialspoint.com/destroy-method-in-tkinter-python#:~:text=The%20destroy()%20method%20in,()%20method%20achieves%20all%20this.
   # master_screen.destroy()  #got the refence from https://www.tutorialspoint.com/destroy-method-in-tkinter-python#:~:text=The%20destroy()%20method%20in,()%20method%20achieves%20all%20this.
    
    # if(received_info[0]=="sclose"):
    #     print("done")
    
    
    
    
    
#==================================Defining the Window for the Client=====================
    
#class client_window(Thread):    
def client_window():
    global client_username_label_rename_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_rename_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/ 
    global client_username_label_rename_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_rename_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_directory_rename_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global socket_object  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_textbox  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label1  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_connect_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label   # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_create_directory_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label2  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_username_label2
    global client_directory_list_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_rename_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_move_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_move_textbox_old  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_move_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_move_textbox_new  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_directory_move_button  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_move_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global username  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_label_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_textbox_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_button_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_username_label_delete_answer  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_button_close  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global master_screen  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_directory_list_button
    global  server_label_move
    global  server_textbox_move
    global  server_button_move
    global server_label_move_answer
    global server_label_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_textbox_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_button_delete  # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global client_label_log
    global client_textbox_log
    global client_button_log
    global logarea
    print("hello")
    client_screen=Tk() # Got the Refrences of the Tk() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    client_screen.title("client") # Got the Refrences of the title() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    client_screen.geometry("900x500+100+200") # Got the Refrences of the geometry() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    client_username_label=Label(client_screen, text="Enter the Username", fg='blue', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label.place(x=60, y=50)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_textbox=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_textbox.place(x=380, y=50,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
    client_connect_button=Button(client_screen, text="Connect to the Server", fg='red')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_connect_button.place(x=150, y=100,height=40, width=180)# Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
    client_connect_button.bind('<Button-1>',client_server)
    client_username_label1=Label(client_screen, text="", fg='Green', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label1.place(x=450, y=100)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_create_directory_button=Button(client_screen, text="Create Directory", fg='black')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_create_directory_button.bind("<Button-1>",create_directory_connect)
    client_directory_list_button=Button(client_screen, text="List Directories", fg='black')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_directory_list_button.bind("<Button-1>",create_directory_list)
    server_directory_list_button=Button(client_screen, text="List Server Directories", fg='black')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_directory_list_button.bind("<Button-1>",server_directory_list) 
    client_username_label2=Label(client_screen, text="", fg='Green', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label2.place(x=100, y=580)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_username_label2=Label(client_screen, text="", fg='Green', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_username_label2.place(x=100, y=650)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label_rename_old=Label(client_screen, text="Present name", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)  
    client_rename_textbox_old=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_rename_textbox_new=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label_rename_new=Label(client_screen, text="New name", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_directory_rename_button=Button(client_screen, text="Rename Directory", fg='black')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_directory_rename_button.bind("<Button-1>",directory_rename)
    client_username_label_rename_answer=Label(client_screen, text="", fg='red', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label_move_old=Label(client_screen, text="Folder name", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)  
    client_move_textbox_old=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_move_textbox_new=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_username_label_move_new=Label(client_screen, text="Destination folder", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_directory_move_button=Button(client_screen, text="move Directory", fg='black')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_directory_move_button.bind("<Button-1>",directory_move)
    client_username_label_move_answer=Label(client_screen, text="", fg='red', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    
    client_label_delete=Label(client_screen, text="Folder name", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_textbox_delete=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_delete=Button(client_screen, text="Disyncronize", fg='red')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_delete.bind('<Button-1>',directory_delete) #bind the directory delete btuuin with method
    client_username_label_delete_answer=Label(client_screen, text="", fg='red', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_close=Button(client_screen, text="Close Window", fg='red')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_close.bind('<Button-1>',window_close)  #bind the window close button
    server_label_move=Label(client_screen, text="Folder name", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_textbox_move=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_button_move=Button(client_screen, text="Syncronize Server Directory", fg='green')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_label_move_answer=Label(client_screen, text="", fg='red', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_button_move.bind('<Button-1>',server_directory_move) #bind the directory delete btuuin with method    
    
    client_label_log=Label(client_screen, text="Log no.", fg='blue', font=("Verdana", 10)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)  
    client_textbox_log=Entry(client_screen, bg='white',fg='black', bd=2) # Got the refrence of Entry method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_log=Button(client_screen, text="Undo", fg='red')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    client_button_log.bind('<Button-1>',log_operation)  #bind the window close button
    
    logarea=scroll.ScrolledText(client_screen,font = ("Times New Roman",9)) 
     
  
# Making the text read only 
    #logarea.configure(state ='disabled') 

  
    
    client_screen.mainloop() # Got the Refrences of the mainloop() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)

    

def client_button(self):
    th=threading.Thread(target=client_window) # got the references from https://pymotw.com/3/threading/
    th.start() # got the references from https://pymotw.com/3/threading/
def client_server(self):
    th=threading.Thread(target=server_client_connect) # got the references from https://pymotw.com/3/threading/
    th.start() # got the references from https://pymotw.com/3/threading/
#==================================Defining the Main window of the Application================================
count=randint(1, 40)
demo='Client Window '+str(count)
def master_window():
    global master_screen 
    master_screen=Tk()
    # Got the Refrences of the Tk() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    master_screen.title(demo) # Got the Refrences of the title() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    master_screen.geometry("900x500+100+200") # Got the Refrences of the geometry() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    master_username_label=Label(master_screen, text="Maximum 3 client", fg='red', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    master_username_label.place(x=60, y=50)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    master_client_connect_button=Button(master_screen, text="Open client window", fg='Blue')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    master_client_connect_button.place(x=380, y=50,width=180,height=35)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
    master_client_connect_button.bind('<Button-1>',client_button)
    master_screen.mainloop() # Got the Refrences of the mainloop() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    
       
master_window() #calling the method
    

#===============================ALL THE REFRENCES ARE LISTED BELOW===========================
# 1. https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
# 2. https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# 3. https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.