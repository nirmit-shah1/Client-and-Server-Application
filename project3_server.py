#name :- Nirmit Rajeshbhai shah
#Mavid:- 1001772180
#email:- nirmitrajeshbha.shah@mavs.uta.edu
from tkinter import * #Got refrences of the b line from (https://pythonprogramming.net/python-3-tkinter-basics-tutorial/)
from socket import * #Got refrences of the bline from (https://www.geeksforgeeks.org/socket-programming-python/)  I have modified in my way to get access of all the methods
import threading     # Got th refences from https://realpython.com/intro-to-python-threading/
import os # Got th refences from https://pythonprogramming.net/python-3-os-module/
import shutil # Got th refences from https://www.geeksforgeeks.org/python-shutil-copy-method/
from random import randint # slightly modified https://www.geeksforgeeks.org/python-randint-function/
from distutils.dir_util import copy_tree
directory="server_main_directory" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
mega_counter=0
value=""
userdictionary={}
bigger={}
server_connect_button="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label1="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label2="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label3="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label4="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label5="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_label6="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_connect_button1="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
server_screen="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
path="" # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
socket_object = socket(AF_INET, SOCK_STREAM) # Got the refrence from https://www.geeksforgeeks.org/socket-programming-python/ 
user1_log_details=["Data"]
user2_log_details=["Data"]
user3_log_details=["Data"]
user1_tracker={}
user2_tracker={}
user3_tracker={}
counterA=0
counterB=0
counterC=0
continousloggA=""
continousloggB=""
continousloggC=""
continouslogg=""
finalsequence=""
finalcondition=0
list_to_be_attached = {"A":None,"B":None ,"C":None}
final_list_to_be_attached_A=[]
final_list_to_be_attached_B=[]
final_list_to_be_attached_C=[]
final_list_to_be_attached=""
def operationperformance(username21,operationtoperform):
    global user1
    global user2
    global user3
    global counterA
    global counterB
    global counterC
    global user1_tracker
    global user2_tracker
    global user3_tracker
    global continouslogg
    global continousloggA
    global continousloggB
    global continousloggC
    global list_to_be_attached
    global final_list_to_be_attached_A
    global final_list_to_be_attached_B
    global final_list_to_be_attached_C
    global bigger
    print("frff",username21)
    if(username21=="A"):
        continousloggA=""
        for i in operationtoperform:
            final_list_to_be_attached_A.append(i)
        
        print("IN ON E A")
        for i in range(1,len(user1_log_details)):
            if i not in final_list_to_be_attached_A:
                continousloggA=continousloggA+"\n"+user1_log_details[i]
    elif (username21== "B"):
        continousloggB=""
        for i in operationtoperform:
            final_list_to_be_attached_B.append(i)
        print("IN ON E B")
        for i in range(1,len(user2_log_details)):
            if i not in final_list_to_be_attached_B:
                continousloggB=continousloggB+"\n"+user2_log_details[i]
        print("IN ON E B")
    elif (username21== "C"):
        continousloggC=""
        for i in operationtoperform:
            final_list_to_be_attached_C.append(i)
        print("IN ON E C")
        for i in range(1,len(user3_log_details)):
            if i not in final_list_to_be_attached_C:
                continousloggC=continousloggC+"\n"+user3_log_details[i]
        print("IN ON E C")
    if(username21=="A"):
        print("fjqf")
        for i in operationtoperform[::-1]:
            print("",user1_log_details[i])
            actiontobeperformed=user1_log_details[i]
            print("actiontobeperformed:= ",actiontobeperformed )
            actioninformation=actiontobeperformed.split(" ")
            print("actioninformation:= ",actioninformation )
            if actioninformation[2]=="created":
                print("In the created")
                source=actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="synchronized":
                print("In the created")
                source="local_"+actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="renamed":
                oldfoldername=actioninformation[5];
                print(oldfoldername)
                newfoldername=actioninformation[3];
                print(newfoldername)
                data=[]
                new_info2=username21
                path4="./server_main_directory/"+new_info2
                print(path4)
                for root,dirs,files in os.walk(path4):
                    data.append(dirs)
                    print("hello")
                    for elements in dirs:
                        if(elements == newfoldername):
                            print("exist")                                
                        elif(elements == oldfoldername):
                            print("done")
                            os.rename(os.path.join(root,elements),os.path.join(root,newfoldername))
            if actioninformation[2]=="delete":
                abc=actioninformation[4]
                st = repr(abc)
                print("STDSSDSDSDSDSDDDadd",st)
                st=st.replace('\\','/')
                st=st.replace("'","")
                print(bigger)
                demo=bigger[actioninformation[3]]
                print("DEMO:===",demo)
                xyz=demo.split(',')
                print("xyz",xyz)
                os.mkdir(st)
                count=0
                print("STTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",st)
                print(len(xyz))
                if(len(xyz) >=2):
                    trial=st+"//"+xyz[0]
                    print("TRIAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
                    os.mkdir(trial)
                    bigger[actioninformation[3]]=""
                    count=count+1
            if actioninformation[2]=="moved":
                destination_path=actioninformation[3]
                destination_path = repr(destination_path)
                destination_path=destination_path.replace('\\','/')
                destination_path=destination_path.replace("'","")
                demo=destination_path.split("/")
                print(demo)
                abc=len(demo)
                source=demo[abc-1]
                print("source:- ",source)
                destination=demo[abc-3];
                print("Destination:-",destination)
                data=[]
                new_info3=actioninformation[1]
                path5="./server_main_directory"
                print(path5)
                count=0
                count1=0
                source_path=""
                destination_path=""
                check_element=""
                check_path=""
                isdir=0
                count3=2
                if source == destination:
                    count3=0
                for root,dirs,files in os.walk(path5):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                            source_path=os.path.join(root,elements)
                            check_element=elements
                            print("check_element:=",check_element)
                            count+=1
                        if(elements == destination):
                            destination_path=os.path.join(root,elements)
                            print("destination_path",destination_path)
                            check_path=str(os.path.join(root,elements))+"/"+check_element
                            print("check_path",check_path)
                            count1+=1
                            padt=os.listdir(destination_path)
                            for elem in padt:
                                if elem == check_element: 
                                    isdir=1
                print(isdir)
                print(count)
                print(count1)
                if( isdir==0 and count1>=1 and count>=1 and count3==2):
                    print(source_path)
                    print(destination_path)
                    dest = shutil.move(source_path, destination_path)
    if(username21=="B"):
        print("B")
        for i in operationtoperform[::-1]:
            print("",user2_log_details[i])
            actiontobeperformed=user2_log_details[i]
            print("actiontobeperformed:= ",actiontobeperformed )
            actioninformation=actiontobeperformed.split(" ")
            print("actioninformation:= ",actioninformation )
            if actioninformation[2]=="created":
                print("In the created")
                source=actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="synchronized":
                print("In the created")
                source="local_"+actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="renamed":
                oldfoldername=actioninformation[5];
                print(oldfoldername)
                newfoldername=actioninformation[3];
                print(newfoldername)
                data=[]
                new_info2=username21
                path4="./server_main_directory/"+new_info2
                print(path4)
                for root,dirs,files in os.walk(path4):
                    data.append(dirs)
                    print("hello")
                    for elements in dirs:
                        if(elements == newfoldername):
                            print("exist")                                
                        elif(elements == oldfoldername):
                            print("done")
                            os.rename(os.path.join(root,elements),os.path.join(root,newfoldername))
            if actioninformation[2]=="delete":
                abc=actioninformation[4]
                st = repr(abc)
                print("STDSSDSDSDSDSDDDadd",st)
                st=st.replace('\\','/')
                st=st.replace("'","")
                print(bigger)
                demo=bigger[actioninformation[3]]
                print("DEMO:===",demo)
                xyz=demo.split(',')
                print("xyz",xyz)
                os.mkdir(st)
                count=0
                print("STTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",st)
                print(len(xyz))
                if(len(xyz) >=2):
                    trial=st+"//"+xyz[0]
                    print("TRIAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
                    os.mkdir(trial)
                    bigger[actioninformation[3]]=""
            if actioninformation[2]=="moved":
                destination_path=actioninformation[3]
                destination_path = repr(destination_path)
                destination_path=destination_path.replace('\\','/')
                destination_path=destination_path.replace("'","")
                demo=destination_path.split("/")
                print(demo)
                abc=len(demo)
                source=demo[abc-1]
                print("source:- ",source)
                destination=demo[abc-3];
                print("Destination:-",destination)
                data=[]
                new_info3=actioninformation[1]
                path5="./server_main_directory"
                print(path5)
                count=0
                count1=0
                source_path=""
                destination_path=""
                check_element=""
                check_path=""
                isdir=0
                count3=2
                if source == destination:
                    count3=0
                for root,dirs,files in os.walk(path5):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                            source_path=os.path.join(root,elements)
                            check_element=elements
                            print("check_element:=",check_element)
                            count+=1
                        if(elements == destination):
                            destination_path=os.path.join(root,elements)
                            print("destination_path",destination_path)
                            check_path=str(os.path.join(root,elements))+"/"+check_element
                            print("check_path",check_path)
                            count1+=1
                            padt=os.listdir(destination_path)
                            for elem in padt:
                                if elem == check_element: 
                                    isdir=1
                print(isdir)
                print(count)
                print(count1)
                if( isdir==0 and count1>=1 and count>=1 and count3==2):
                    print(source_path)
                    print(destination_path)
                    dest = shutil.move(source_path, destination_path)
    if(username21=="C"):
        print("C")
        for i in operationtoperform[::-1]:
            print("",user3_log_details[i])
            actiontobeperformed=user3_log_details[i]
            print("actiontobeperformed:= ",actiontobeperformed )
            actioninformation=actiontobeperformed.split(" ")
            print("actioninformation:= ",actioninformation )
            if actioninformation[2]=="created":
                print("In the created")
                source=actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="synchronized":
                print("In the created")
                source="local_"+actioninformation[3]
                print("source:- ",source)
                data=[]
                new_info4=username21
                path6="server_main_directory/"+new_info4
                print(path6)
                count=0
                for root,dirs,files in os.walk(path6):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                               source_path=os.path.join(root,elements)
                               shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                               count+=1
            if actioninformation[2]=="renamed":
                oldfoldername=actioninformation[5];
                print(oldfoldername)
                newfoldername=actioninformation[3];
                print(newfoldername)
                data=[]
                new_info2=username21
                path4="./server_main_directory/"+new_info2
                print(path4)
                for root,dirs,files in os.walk(path4):
                    data.append(dirs)
                    print("hello")
                    for elements in dirs:
                        if(elements == newfoldername):
                            print("exist")                                
                        elif(elements == oldfoldername):
                            print("done")
                            os.rename(os.path.join(root,elements),os.path.join(root,newfoldername))
            if actioninformation[2]=="delete":
                abc=actioninformation[4]
                st = repr(abc)
                print("STDSSDSDSDSDSDDDadd",st)
                st=st.replace('\\','/')
                st=st.replace("'","")
                print(bigger)
                demo=bigger[actioninformation[3]]
                print("DEMO:===",demo)
                xyz=demo.split(',')
                print("xyz",xyz)
                os.mkdir(st)
                count=0
                print("STTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",st)
                print(len(xyz))
                if(len(xyz) >=2):
                    trial=st+"//"+xyz[0]
                    print("TRIAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
                    os.mkdir(trial)
                    bigger[actioninformation[3]]=""

            if actioninformation[2]=="moved":
                destination_path=actioninformation[3]
                destination_path = repr(destination_path)
                destination_path=destination_path.replace('\\','/')
                destination_path=destination_path.replace("'","")
                demo=destination_path.split("/")
                print(demo)
                abc=len(demo)
                source=demo[abc-1]
                print("source:- ",source)
                destination=demo[abc-3];
                print("Destination:-",destination)
                data=[]
                new_info3=actioninformation[1]
                path5="./server_main_directory"
                print(path5)
                count=0
                count1=0
                source_path=""
                destination_path=""
                check_element=""
                check_path=""
                isdir=0
                count3=2
                if source == destination:
                    count3=0
                for root,dirs,files in os.walk(path5):
                    data.append(dirs)
                    for elements in dirs:
                        if(elements == source):
                            source_path=os.path.join(root,elements)
                            check_element=elements
                            print("check_element:=",check_element)
                            count+=1
                        if(elements == destination):
                            destination_path=os.path.join(root,elements)
                            print("destination_path",destination_path)
                            check_path=str(os.path.join(root,elements))+"/"+check_element
                            print("check_path",check_path)
                            count1+=1
                            padt=os.listdir(destination_path)
                            for elem in padt:
                                if elem == check_element: 
                                    isdir=1
                print(isdir)
                print(count)
                print(count1)
                if( isdir==0 and count1>=1 and count>=1 and count3==2):
                    print(source_path)
                    print(destination_path)
                    dest = shutil.move(source_path, destination_path)
    return
def undo(username21,logno):
    print("hello")
    global user1
    global user2
    global user3
    global counterA
    global counterB
    global counterC
    global user1_tracker
    global user2_tracker
    global user3_tracker
    global continouslogg
    global continousloggA
    global continousloggB
    global continousloggC
    operationtoperform=[]
    global finalsequence
    print("Username",username21)
    print("logno",logno)
    checklogno=str(logno)
    if(username21=="A"):
        print("IN A")
        print("userA Details", user1_tracker)
        for key in user1_tracker:
            checker=str(user1_tracker[key])
            print("checker", checker);
            if checklogno in checker:
                stringtocheck=checklogno
                result=checker.find(stringtocheck)
                print("Result",result)
                handler=-1
                if(result>0):
                    print("INSIDE IF")
                    if checker[result-1]== "1":
                        handler=1
                    elif checker[result-1]== "2":
                        handler=1
                    elif checker[result-1]== "3":
                        handler=1
                    elif checker[result-1]== "4":
                        handler=1
                    elif checker[result-1]== "5":
                        handler=1
                    elif checker[result-1]== "6":
                        handler=1
                    elif checker[result-1]== "7":
                        handler=1
                    elif checker[result-1]== "8":
                        handler=1
                    elif checker[result-1]== "9":
                            handler=1
                    elif checker[result-1]== ",":
                            handler=0
                    elif len(checker)>1 and result <len(checker):
                        if checker[result+1]== stringtocheck:
                            handler=1
                    else:
                        if len(checker)>1:
                            if checker[result+1]== stringtocheck:
                                handler=1
                if(result==0):
                   print("INSIDE ELSE")
                   handler=0
                   print("Handler",handler)
                if(handler ==0):
                    print("Handler",handler)
                    print("checker",checker)
                    finalsequence=checker
                    print("Final Sequence:= ",finalsequence)
                    performsequence=finalsequence.split(",")
                    print("Perform Sequence:= ",performsequence)
                    endsequence= [int(i) for i in performsequence] 
                    print("End Sequence:= ",endsequence)
                    for data in endsequence:
                        if(data>=logno):
                            operationtoperform.append(data)
                    print("operation to perform:= ",operationtoperform)
                    operationperformance(username21,operationtoperform)
    
    if(username21 == "B"):
        print("IN B")
        for key in user2_tracker:
            checker=str(user2_tracker[key])
            print("checker", checker);
            if checklogno in checker:
                stringtocheck=checklogno
                result=checker.find(stringtocheck)
                print("Result",result)
                handler=-1
                if(result>0):
                    print("INSIDE IF")
                    if checker[result-1]== "1":
                        handler=1
                    elif checker[result-1]== "2":
                        handler=1
                    elif checker[result-1]== "3":
                        handler=1
                    elif checker[result-1]== "4":
                        handler=1
                    elif checker[result-1]== "5":
                        handler=1
                    elif checker[result-1]== "6":
                        handler=1
                    elif checker[result-1]== "7":
                        handler=1
                    elif checker[result-1]== "8":
                        handler=1
                    elif checker[result-1]== "9":
                            handler=1
                    elif checker[result-1]== ",":
                            handler=0
                    elif len(checker)>1 and result <len(checker):
                        if checker[result+1]== stringtocheck:
                            handler=1
                    else:
                        if len(checker)>1:
                            if checker[result+1]== stringtocheck:
                                handler=1
                if(result==0):
                   print("INSIDE ELSE")
                   handler=0
                   print("Handler",handler)
                if(handler ==0):
                    print("Handler",handler)
                    print("checker",checker)
                    finalsequence=checker
                    print("Final Sequence:= ",finalsequence)
                    performsequence=finalsequence.split(",")
                    print("Perform Sequence:= ",performsequence)
                    endsequence= [int(i) for i in performsequence] 
                    print("End Sequence:= ",endsequence)
                    for data in endsequence:
                        if(data>=logno):
                            operationtoperform.append(data)
                    print("operation to perform:= ",operationtoperform)
                    operationperformance(username21,operationtoperform)

    if(username21 == "C"):
        print("IN C")
        for key in user3_tracker:
            checker=str(user3_tracker[key])
            print("checker", checker);
            if checklogno in checker:
                stringtocheck=checklogno
                result=checker.find(stringtocheck)
                print("Result",result)
                handler=-1
                if(result>0):
                    print("INSIDE IF")
                    if checker[result-1]== "1":
                        handler=1
                    elif checker[result-1]== "2":
                        handler=1
                    elif checker[result-1]== "3":
                        handler=1
                    elif checker[result-1]== "4":
                        handler=1
                    elif checker[result-1]== "5":
                        handler=1
                    elif checker[result-1]== "6":
                        handler=1
                    elif checker[result-1]== "7":
                        handler=1
                    elif checker[result-1]== "8":
                        handler=1
                    elif checker[result-1]== "9":
                            handler=1
                    elif checker[result-1]== ",":
                            handler=0
                    elif len(checker)>1 and result <len(checker):
                        if checker[result+1]== stringtocheck:
                            handler=1
                    else:
                        if len(checker)>1:
                            if checker[result+1]== stringtocheck:
                                handler=1
                if(result==0):
                   print("INSIDE ELSE")
                   handler=0
                   print("Handler",handler)
                if(handler ==0):
                    print("Handler",handler)
                    print("checker",checker)
                    finalsequence=checker
                    print("Final Sequence:= ",finalsequence)
                    performsequence=finalsequence.split(",")
                    print("Perform Sequence:= ",performsequence)
                    endsequence= [int(i) for i in performsequence] 
                    print("End Sequence:= ",endsequence)
                    for data in endsequence:
                        if(data>=logno):
                            operationtoperform.append(data)
                    print("operation to perform:= ",operationtoperform)
                    operationperformance(username21,operationtoperform)
    return
def checker_demo(username1):
    global continouslogg
    global userdirectory 
    global continousloggA
    global continousloggB
    global continousloggC
    data=[]
    data1=[]
    username=username1
    new_info=[]
    new_info.append(userdictionary.get(username))
    source_path="./server_main_directory/server/"
    path5="./server_main_directory/server/"
    check_element=""
    check_path=""
    for user in new_info:
        path="./server_main_directory/"+user+"/"
    for root,dirs,files in os.walk(path):
        print(dirs)
        for demo in dirs:
            if "local" in demo:
                data.append(demo)
        print("DATA VARIABLE:-",data)
        for elements in data:
            print("Elemnets:-",elements)
            y=elements.replace("local_","")
            source_path="./server_main_directory/server/"
            for root,dirs,files in os.walk(source_path):
                for elements in dirs:
                    if elements == y :
                        source_path=os.path.join(root,elements)    
            print("Source Path",source_path)
            check_element=elements
            path_extra="./server_main_directory/"+user+"/local_"+y+"/"
            print("Path Extra",path_extra)
            shutil.rmtree(path_extra)
            dest=shutil.copytree(source_path, path_extra)
            print("dggs")
    return 
    
def server_button(self):# it is for creating the thread on the servers side for handaling the reqst
    th=threading.Thread(target=server_connect) # got the references from https://pymotw.com/3/threading/
    th.start() # got the references from https://pymotw.com/3/threading/
def server_button1(self):
    global server_screen # access the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    directory="server_main_directory"  # Modified the variable name naccording to my preferences https://www.w3schools.com/python/python_variables.asp#:~:text=Creating%20Variables,assign%20a%20value%20to%20it.
    shutil.rmtree(directory) #got the refence from  https://docs.python.org/3/library/shutil.html
    server_screen.destroy() #got the refence from https://www.tutorialspoint.com/destroy-method-in-tkinter-python#:~:text=The%20destroy()%20method%20in,()%20method%20achieves%20all%20this.
#==================================Defining the window for the server==============================  
def server_window():
    global server_connect_button # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global  server_label1 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_label2 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_label3 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_label4 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_label5 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_label6 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_connect_button1 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    global server_screen # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
    server_screen=Tk() # Got the Refrences of the Tk() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    server_screen.title('Server Window') # Got the Refrences of the title() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    server_screen.geometry("900x500+100+200") # Got the Refrences of the geometry() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
    server_label1=Label(server_screen, text="First Click below Button to start server", fg='Red', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label1.place(x=150, y=50)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_connect_button=Button(server_screen, text="Start the Server", fg='white',bg='green')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_connect_button.place(x=150, y=100,height=40, width=180)# Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
    server_connect_button.bind('<Button-1>',server_button) # bind the button with the function in order to start the server
    server_connect_button1=Button(server_screen, text="Close the Server", fg='white',bg='red')# Got the refrence of Button method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_connect_button1.bind('<Button-1>',server_button1) # bind the button with the function in order to close the server
    server_label2=Label(server_screen, text="", fg='Blue', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label2.place(x=150, y=160)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_label3=Label(server_screen, text="USERNAME OF ALL THE CONNECTED USER", fg='red', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label3.place(x=150, y=200)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_label4=Label(server_screen, text="", fg='blue', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label4.place(x=150, y=250)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_label5=Label(server_screen, text="Ongoing Activity on Server", fg='red', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label5.place(x=150, y=450)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    server_label6=Label(server_screen, text="", fg='blue', font=("Verdana", 20)) # Got the refrence of Label method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)     
    server_label6.place(x=150, y=500)  # Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) 
    
    server_screen.mainloop() # Got the Refrences of the mainloop() method from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)

def logg_handaling(operation):
    global user1
    global user2
    global user3
    global counterA
    global counterB
    global counterC
    global user1_tracker
    global user2_tracker
    global user3_tracker
    global continouslogg
    global continousloggA
    global continousloggB
    global continousloggC
    # A created demo234
    # A rename demo234 to nix1234
    # A moved demo1/demo234 to demo2/demo234
    # A syncronized local_demo
    # A deleted demo234
    data=operation.split(" ")
    if data[0]=="A":
        counterA=counterA+1
        print("Username:= ",data[0])
        log_info=str(counterA)+"."+" "+operation
        user1_log_details.append(log_info)     
        continousloggA=continousloggA+"\n"+log_info
        print("Log Details of A := ", user1_log_details)
        if (data[1] == "created"  or data[1] == "synchronized"):
            user1_tracker[data[2]]=counterA
        if data[1] == "renamed":
            user1_tracker[data[4]]=user1_tracker.pop(data[2])
            x=str(user1_tracker.get(data[4]))+","+str(counterA)
            user1_tracker[data[4]]=x
        if data[1] == "moved":
            trial=data[2].split("/")
            val=len(trial)-1
            data=repr(trial[val])
            data=data.replace('\\','/')
            data=data.replace("'","")
            other=data.split("//")
            finder=other[1]
            x=str(user1_tracker.get(finder))+","+str(counterA)
            user1_tracker[finder]=x
        if data[1] == "delete":
            print("delete")
            print(data[2])
            x=str(user1_tracker.get(data[2]))+","+str(counterA)
            user1_tracker[data[2]]=x
        
        return continousloggA
            
    elif data[0] == "B":
        counterB=counterB+1
        print("Username:= ",data[0])
        log_info=str(counterB)+"."+" "+operation
        user2_log_details.append(log_info)     
        continousloggB=continousloggB+"\n"+log_info
        print("Log Details of B := ", user2_log_details)
        if (data[1] == "created"  or data[1] == "synchronized"):
            user2_tracker[data[2]]=counterB
        if data[1] == "renamed":
            user2_tracker[data[4]]=user2_tracker.pop(data[2])
            x=str(user2_tracker.get(data[4]))+","+str(counterB)
            user2_tracker[data[4]]=x
        if data[1] == "moved":
            trial=data[2].split("/")
            val=len(trial)-1
            data=repr(trial[val])
            data=data.replace('\\','/')
            data=data.replace("'","")
            other=data.split("//")
            finder=other[1]
            x=str(user2_tracker.get(finder))+","+str(counterB)
            user2_tracker[finder]=x
        if data[1] == "delete":
            print("delete")
            print(data[2])
            x=str(user2_tracker.get(data[2]))+","+str(counterB)
            user2_tracker[data[2]]=x
        return continousloggB
    elif data[0] == "C":  
        counterC=counterC+1
        print("Username:= ",data[0])
        log_info=str(counterC)+"."+" "+operation
        user3_log_details.append(log_info)     
        continousloggC=continousloggC+"\n"+log_info
        print("Log Details of C := ", user3_log_details)
        if (data[1] == "created"  or data[1] == "synchronized"):
            user3_tracker[data[2]]=counterC
        if data[1] == "renamed":
            user3_tracker[data[4]]=user3_tracker.pop(data[2])
            x=str(user3_tracker.get(data[4]))+","+str(counterC)
            user3_tracker[data[4]]=x
        if data[1] == "moved":
            trial=data[2].split("/")
            val=len(trial)-1
            data=repr(trial[val])
            data=data.replace('\\','/')
            data=data.replace("'","")
            other=data.split("//")
            finder=other[1]
            x=str(user3_tracker.get(finder))+","+str(counterC)
            user3_tracker[finder]=x
        if data[1] == "delete":
            print("delete")
            print(data[2])
            x=str(user3_tracker.get(data[2]))+","+str(counterC)
            user3_tracker[data[2]]=x
        return continousloggC
 
def server_connect(): #this function will be called on 0pressing the start button
    try: #to handle the exception all the things are written in try block
        global server_connect_button # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global socket_object # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global server_label2 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global server_label3 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global server_label4 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global server_label5 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global server_connect_button1 # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global path # accessing the global variable https://www.geeksforgeeks.org/global-keyword-in-python/
        global mega_counter
        global value
        global userdictionary
        global final_list_to_be_attached
        global bigger
        label="" # creating variable https://www.geeksforgeeks.org/global-keyword-in-python/
        port=1234 #just use the same name as specified in the following website https://www.geeksforgeeks.org/socket-programming-python/ 
        socket_object.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # got the refence from https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
        socket_object.bind(('127.0.1.3', port))   # Got the refrence of the bind method from https://www.geeksforgeeks.org/socket-programming-python/ 
        socket_object.listen(30)    # Got the refrence of the listen method from https://www.geeksforgeeks.org/socket-programming-python/     
        server_label2.configure(text="Server is Online") #using the configure method the text method was changed
        server_connect_button.place_forget() #got the refrence from https://www.geeksforgeeks.org/place_forget-method-using-tkinter-in-python/   
        server_connect_button1.place(x=150, y=100,height=40, width=180)# Got the refrence of place method and its parameters from the (https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python) and height and width refrence from https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
        f1=directory+"/"+"server"
        f2=f1+"/"+"server_folder1"
        f3=f1+"/"+"server_folder2"
        f4=f1+"/"+"server_folder3"
        f22=f2+"/subfolder_of_1"
        f33=f3+"/subfolder_of_2"
        f44=f4+"/subfolder_of_3"
        #=================================CREATE DIRECTORY FOR  ALL USERS==========================
        os.mkdir(directory) #got the refrence from https://www.tutorialspoint.com/python/os_mkdir.htm
        os.mkdir(f1)
        os.mkdir(f2)
        os.mkdir(f3)
        os.mkdir(f4)
        os.mkdir(f22)
        os.mkdir(f33)
        os.mkdir(f44)
        
        #================================CREATE FILE TO STORE THE USERNAMES===========================
        path=directory+"/"+"username.txt" #created a path variable from where the username file has to be open
        f = open(path, "w") #open the file in the write mode
        f.close() #closed the file
        #================================NOW PERFORM THE FUNCTIONS FOR THE USER========================        
        while True: #loop for the active operation of the server
            print("heldelo") 
            c, addr = socket_object.accept() #got the refrence from https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
            print("bye")
            username="" # create a variable to store the username current
            username=c.recv(1024).decode("utf-8")  #got the refrencaaarom https://www.youtube.com/watch?v=u4kr7EFxAKk&ab_channel=Telusko
            print("username1:= ",username) 
            finaldirusername=username.split(";") #done the divison of the string on the basis of the ; which has been passed in the string and stoere in the list
            print("username:=",finaldirusername) 
            print("username2:= ",username)
            if username.find(';') == -1 : #whenever this condition is satisfied than only the new user will be build
                if username == "" :
                    print("Starting if username1:= ",username)
                    output = 'Please Enter the value before submitting'
                    c.sendall(output.encode('utf-8'))  
                else:
                    print("Starting else username1:= ",username)
                    file=open(path,"r")
                    demo=file.readline().split(';')
                    print(demo)
                    file.close()
                    if username in demo:
                        print("not Starting if username1:= ",username)
                        info1=username+" has been deny connection with the server because of username collistion\n"
                        server_label6['text'] += info1
                        output = 'Please enter another username'+";"+username
                        c.sendall(output.encode('utf-8'))  #got the refrence from https://docs.python.org/3/library/socket.html
                        c.close()
                    else:
                        print(" not Starting else username1:= ",username)#this else block will create the usee and store its name in the usrername.txt file
                        file1=open(path,"a")
                        name=";"+username
                        file1.write(name)
                        file1.close()
                        if(mega_counter ==0):
                            value="A"
                            userdictionary[username]=value
                            mega_counter+=1
                        elif mega_counter==1:
                            value="B"
                            userdictionary[username]=value
                            mega_counter+=1
                        elif mega_counter==2:
                            value="C"
                            userdictionary[username]=value
                        info=username+"\n"
                        server_label4['text'] += info
                        info1=username+" has been conected to the system\n"
                        server_label6['text'] += info1
                        output = 'Successfull'+";"+username
                        path1=directory+"/"+value
                        os.mkdir(path1)
                        c.sendall(output.encode('utf-8')) #got the reference from https://docs.python.org/3/library/socket.html
                        c.close()
            else:
                #==================CREATE THE DIRECTORY BY ATTACHING THE RANDOM NUMBER ON THE BACK OF THE DIRECTORY NAME IN ORDER TO GENERATE NEW DIRECTORY WITH NEW NAME SO RANDINT WAS USED
                if finaldirusername[0]=="directory":
                    
                    new_info=userdictionary.get(finaldirusername[1])
                    checker_demo(finaldirusername[1])
                    print(new_info)
                    
                    localuser=finaldirusername[1]
                    localuser2=localuser+str(randint(0,800))
                    path2=directory+"/"+new_info+"/"+localuser2
                    print(path2)
                    os.mkdir(path2)
                    msg=new_info+" "+"created"+" "+localuser2
                    logg_handaling(msg)
                    info1=localuser2+" directory has been created of the "+localuser+"\n"
                    server_label6['text'] += info1
                    print ('Got connection from', addr )  #got the reference from https://docs.python.org/3/library/socket.html
                    c.close();
                    
                #=======DISPLAY ALL THE DIRECTORY THE REPLACE HAS TO BE USED IN ORDER TO EXTRACT THE INFO FROM THE NESTED LIST     
                if finaldirusername[0]=="list":
                   checker_demo(finaldirusername[1])
                   new_info1=userdictionary.get(finaldirusername[1])
                   listuser=finaldirusername[1] 
                   print(new_info1)
                   path3=directory+"/"+new_info1+"/"
                   data=""
                   for root, dirs, files in os.walk(path3): #MODIFIED IN MY WAY https://www.tutorialspoint.com/python/os_walk.htm
                       mine=str(dirs)
                       mine1=mine.replace('[',"")
                       #    print("my",mine1)
                       mine2=mine1.replace(']',"")
                       #print("my", mine2)
                       mine3=mine2.replace("'"," ")
                       mine3.replace('\'',' ')
                       #print(mine3)
                       mine2=mine3+"    "
                       data+=mine2
                   info1=listuser+"has requested to list all the directories in its home directory"+"\n"
                   server_label6['text'] += info1
                   msg=new_info1+" "+"listed"
                   continouslogg=logg_handaling(msg)
                   output = 'lists;'+data+';'+continouslogg
                   c.sendall(output.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                   print ('Got connection from', addr )
            
                   c.close()
                  #=======DISPLAY ALL THE DIRECTORY THE REPLACE HAS TO BE USED IN ORDER TO EXTRACT THE INFO FROM THE NESTED LIST     
                if finaldirusername[0]=="slist":
                   checker_demo(finaldirusername[1])
                   new_info1s=userdictionary.get(finaldirusername[1])
                   listuser=finaldirusername[1] 
                   print(new_info1s)
                   path4s=f1
                   data=""
                   for root, dirs, files in os.walk(path4s): #MODIFIED IN MY WAY https://www.tutorialspoint.com/python/os_walk.htm
                       mine=str(dirs)
                       mine1=mine.replace('[',"")
                       #    print("my",mine1)
                       mine2=mine1.replace(']',"")
                       #print("my", mine2)
                       mine3=mine2.replace("'"," ")
                       mine3.replace('\'',' ')
                       #print(mine3)
                       mine2=mine3+" "
                       data+=mine2
                   info1=listuser+"has requested to list all the directories in its home directory"+"\n"
                   server_label6['text'] += info1
                   
                   msg=new_info1s+" "+"server listed"
                   continouslogg=logg_handaling(msg)
                   output = 'slists;'+data+';'+continouslogg+';'+final_list_to_be_attached
                   c.sendall(output.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                   c.close()
                   print ('Got connection from', addr )
                #=============== FIRST CHECKED WHEATHERT THE FILE WHICH THE USER HAS REQUESTED EXIST OR NOT IF IT EXIST THAN ONLY THE FILE WILL BE RENAMED
                if finaldirusername[0]=="rename":
                    checker_demo(finaldirusername[3])
                    oldfoldername=finaldirusername[1];
                    print(oldfoldername)
                    newfoldername=finaldirusername[2];
                    print(newfoldername)
                    data=[]
                    localuser=finaldirusername[3];
                    print(localuser)
                    new_info2=userdictionary.get(localuser)
                    path4="./server_main_directory/"+new_info2
                    print(path4)
                    for root,dirs,files in os.walk(path4):
                        data.append(dirs)
                        print("hello")
                        for elements in dirs:
                            if(elements == newfoldername):
                                print("exist")
                                output1 = "frename"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                                info1="Fail to rename the directory requested by "+localuser+"\n"
                                server_label6['text'] += info1
                                msg=new_info2+" "+"fail rename"
                                logg_handaling(msg)
                                c.sendall(output1.encode('utf-8'))
                            elif(elements == oldfoldername):
                                print("done")
                                os.rename(os.path.join(root,elements),os.path.join(root,newfoldername))
                                
                                info1="Successfull to rename the directory requested by "+localuser+"\n"
                                server_label6['text'] += info1
                                msg=new_info2+" "+"renamed"+" "+oldfoldername+" to "+newfoldername
                                continouslogg=logg_handaling(msg)
                                output2 = "srename"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                                c.sendall(output2.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                    c.close()
                if finaldirusername[0]=="log":
                    checker_demo(finaldirusername[2])
                    localuser=finaldirusername[2];
                    print("localuser:-",localuser)
                    
                    new_info3=userdictionary.get(localuser)
                    print("NEW INFO 3",new_info3)
                    print("finaldirusername[1]",finaldirusername[1])
                    undo(new_info3,int(finaldirusername[1]))
                    #undo(new_info3,finaldirusername[1])
                    output2 = "log"+";"+localuser
                    print("username",username)
                    print("OUTPUT 2:= ",output2)
                    c.sendall(output2.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                    c.close()
                                
                    
                    
                # CHECKED WHEATHER THE SOURCE AND DESTINATION FILE EXIST OR NOT THEN ONLY THE MOVE OPERATION HAS TO BE PERFORMED
                if finaldirusername[0]=="move":
                    checker_demo(finaldirusername[3])
                    source=finaldirusername[1];
                    print("source:- ",source)
                    destination=finaldirusername[2];
                    print("Destination:-",destination)
                    data=[]
                    localuser=finaldirusername[3];
                    print(localuser)
                    new_info3=userdictionary.get(localuser)
                    path5="./server_main_directory/"+new_info3
                    print(path5)
                    count=0
                    count1=0
                    source_path=""
                    destination_path=""
                    check_element=""
                    check_path=""
                    isdir=0
                    count3=2
                    if source == destination:
                        count3=0
                    for root,dirs,files in os.walk(path5):
                        data.append(dirs)
                        for elements in dirs:
                            if(elements == source):
                                source_path=os.path.join(root,elements)
                                check_element=elements
                                print("check_element:=",check_element)
                                count+=1
                            if(elements == destination):
                                destination_path=os.path.join(root,elements)
                                print("destination_path",destination_path)
                                check_path=str(os.path.join(root,elements))+"/"+check_element
                                print("check_path",check_path)
                                count1+=1
                                padt=os.listdir(destination_path)
                                for elem in padt:
                                    if elem == check_element: 
                                        isdir=1
                    print(isdir)
                    print(count)
                    print(count1)
                    if( isdir==0 and count1>=1 and count>=1 and count3==2):
                        print(source_path)
                        print(destination_path)
                        dest = shutil.move(source_path, destination_path)
                        
                        info1="Successfull to move the directory requested by "+localuser+"\n"
                        server_label6['text'] += info1
                        msg=new_info3+" moved "+source_path+" to "+destination_path
                        print(msg)
                        continouslogg=logg_handaling(msg)
                        output4 = "smove"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                        c.sendall(output4.encode('utf-8'))
                    else:
                        print("fail")
                        
                        info1="Fail to move the directory requested by "+localuser+"\n"
                        server_label6['text'] += info1
                        msg=new_info3+" fail moved "+source+" to "+destination
                        continouslogg=logg_handaling(msg)
                        output4 = "fmove"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                        c.sendall(output4.encode('utf-8'))
                    c.close()
                ###############SERVER
                if finaldirusername[0]=="smove":
                    checker_demo(finaldirusername[2])
                    new_info3=userdictionary.get(finaldirusername[2])
                    localuser=userdictionary.get(finaldirusername[2])
                    path5="./server_main_directory/server/"
                    data=[]
                    source=finaldirusername[1]
                    print(path5)
                    count=1
                    count1=0
                    username=finaldirusername[2]
                    destination=new_info3
                    source_path="./server_main_directory/server/"
                    destination_path="./server_main_directory/"+new_info3+"/"
                    check_element=""
                    check_path=""
                    isdir=0
                    count3=2
                    for root,dirs,files in os.walk(path5):
                        data.append(dirs)
                        print("MYDATA",data)
                        for elements in dirs:
                            print(len(dirs))
                            if(elements == source):
                                source_path=os.path.join(root,elements)
                                print("MY SOURCE PATH",source_path)
                                #dest = copy_tree(source_path, destination_path)
                                check_element=elements
                                print("check_element:=",check_element)
                                count+=1
                               
                    if( isdir==0  and count>=1 and count3==2):
                        path_extra="./server_main_directory/"+new_info3+"/local_"+source+"/"
                        os.mkdir(path_extra)
                        dest = copy_tree(source_path, path_extra)
                        
                        info1="Successfull to sync the directory requested by "+localuser+"\n" 
                        server_label6['text'] += info1
                        msg=new_info3+" synchronized "+source
                        continouslogg=logg_handaling(msg)
                        output4 = "ssmove"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                        c.sendall(output4.encode('utf-8'))
                        
                        c.close()
                    else:
                        print("fail")
                        
                        info1="Fail to sync the directory requested by "+localuser+"\n"
                        server_label6['text'] += info1
                        msg=new_info3+" fail synchronized "+source
                        continouslogg=logg_handaling(msg)
                        output4 = "ffmove"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                        c.sendall(output4.encode('utf-8'))
                        c.close()
                    c.close()
                ###############SYNC
                
                if finaldirusername[0]=="delete":
                    checker_demo(finaldirusername[2])
                    source=finaldirusername[1];
                    print("source:- ",source)
                    data=[]
                    data1=[]
                    localuser=finaldirusername[2];
                    print(localuser)
                    new_info4=userdictionary.get(localuser)
                    path6="server_main_directory/"+new_info4
                    print(path6)
                    count=0
                    apt=""
                    username=finaldirusername[2];
                    for root,dirs,files in os.walk(path6):
                        data.append(dirs)
                        for elements in dirs:
                            if(elements == source):
                                source_path=os.path.join(root,elements)
                                for root,dirs,files in os.walk(source_path):
                                    data1.append(dirs)
                                    for elements in dirs:
                                        apt=apt+elements+","
                                bigger[source]=apt
                                shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                                count+=1
                                msg=new_info4+" delete "+source+" "+source_path
                                continouslogg=logg_handaling(msg)
                                
                                
                                        
                                    
                                print("Mydata:= ",continouslogg)
                                output5 = "sdelete"+";"+username+";"+continouslogg+';'+final_list_to_be_attached
                                c.sendall(output5.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                    if(count ==0):
                       print("fail")
                       
                       info1="Successfull to delete the directory requested by "+localuser+"\n"
                       server_label6['text'] += info1
                       msg=new_info4+" fail delete "+source+" "+source_path
                       continouslogg=logg_handaling(msg)
                       output5 = "fdelete"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                       c.sendall(output5.encode('utf-8'))
                    c.close()
                #server
                if finaldirusername[0]=="sdelete":
                    checker_demo(finaldirusername[2])
                    source=finaldirusername[1];
                    print("source:- ",source)
                    data=[]
                    localuser=finaldirusername[2];
                    print(localuser)
                    new_info4=userdictionary.get(localuser)
                    path6="server_main_directory/"+new_info4
                    print(path6)
                    username=finaldirusername[2];
                    count=0
                    for root,dirs,files in os.walk(path6):
                        data.append(dirs)
                        for elements in dirs:
                            if(elements == source):
                                source_path=os.path.join(root,elements)
                                shutil.rmtree(source_path) #got the reference from https://docs.python.org/3/library/shutil.html
                                
                                count+=1
                                msg=new_info4+" delete "+source_path
                                continouslogg=logg_handaling(msg)
                                print("Mydata:= ",continouslogg)
                                output5 = "sdelete"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                                c.sendall(output5.encode('utf-8'))  #got the reference from https://docs.python.org/3/library/socket.html
                    if(count ==0):
                       print("fail")
                       
                       info1="Successfull to delete the directory requested by "+localuser+"\n"
                       server_label6['text'] += info1
                       msg=new_info4+" fail delete "+source
                       continouslogg=logg_handaling(msg)
                       print("Mydata:= ",continouslogg)
                       output5 = "fdelete"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                       c.sendall(output5.encode('utf-8'))
                    c.close()         
                    
                if finaldirusername[0]=="close":
                    username=finaldirusername[1];
                    data=str(server_label4.cget("text"))
                    list_data=data.split("\n")
                    data_final=""
                    for element in list_data:
                        print("adcafaf",element)
                        if element!=username:
                            data_final=data_final+element+"\n"
                    server_label4['text'] = data_final
                    fin = open("server_main_directory/username.txt", "rt") #  got the reference of method from https://pythonexamples.org/python-replace-string-in-file/
                    fout = open("server_main_directory/username.txt", "w")#  got the reference of method from https://pythonexamples.org/python-replace-string-in-file/
                    for line in fin:	
                        data=line.split(";")
                        for elements in data:
                            if elements != username:
                                sample=elements+";"
                                fout.write(sample)    #  got the reference of method from https://pythonexamples.org/python-replace-string-in-file/                      
                    fin.close() #  got the reference of method from https://pythonexamples.org/python-replace-string-in-file/
                    fout.close() #  got the reference of method from https://pythonexamples.org/python-replace-string-in-file/
                    output6 = "sclose"+";"+username+';'+continouslogg+';'+final_list_to_be_attached
                    info1="Successfull to disconnect "+username+"\n"
                    server_label6['text'] += info
                    c.sendall(output6.encode('utf-8'))
                    c.close()
            c.close()
    except socket.timeout:
        print("Connection dropped")        
    finally:
        print("hello")
    

  
    
server_window()


#===============================ALL THE REFRENCES ARE LISTED BELOW===========================
# 1. https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
# 2. https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# 3. https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20unit%20of%20width%20option,is%20set%20to%20be%2010.
# 4. https://www.geeksforgeeks.org/socket-programming-python/ 
