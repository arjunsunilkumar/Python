import pickle
import datetime
from datetime import date
import time
import os
def add_book(): 											#Function for adding a book
	os.system('clear') 										#Clear screen
	print "LIBRARY MANAGEMENT SYSTEM\n\n"
	f=open("library.txt","r") 									#opening the file to pull the nested dictionary
	lib={"name":{},"type":{},"author":{},"issuedto":{},"issuedfor":{},"issuedon":{},"addedon":{}} 	#declaring the structure of the dictionart
	try:												#checking if there is a dictionary to pull from the file
		lib=pickle.load(f)
	except EOFError: 										#If there is nothing in the file to load.... this section is executed
		f.close()
		f=open("library.txt","w")
		pickle.dump(lib,f)									#Adding a dictionary(This is generally for when the library management is being run for the first time")
	f.close()
	bno=input("Enter the Book ID for the book you are adding:- ")
	bname=raw_input("Enter the name of the book you are adding to the library:- ")	
	btype=raw_input("Enter the type of the book you are adding to the library:- ")
	bauth=raw_input("Enter the author of the book you are adding to the library:- ")
	bissto=""											#initialising the value of who the book is issued as an empty string
	bissfor=0											
	bisson=datetime.date(1000,01,01)
	baddon=datetime.date.today()
	lib["name"][bno]=bname
	lib["type"][bno]=btype
	lib["author"][bno]=bauth
	lib["issuedto"][bno]=bissto
	lib["issuedfor"][bno]=bissfor
	lib["issuedon"][bno]=bisson
	lib["addedon"][bno]=baddon
	f=open("library.txt","w")
	pickle.dump(lib,f)
	os.system('clear')
	print "LIBRARY MANAGEMENT SYSTEM\n\n"
	print "Book was added to the library "
	time.sleep(1)
	f.close()
def issue_book():
	os.system('clear')
  	print "LIBRARY MANAGEMENT SYSTEM\n\n"
  	f=open("library.txt","r")
    	lib={}
   	t=1
    	try:
        	lib=pickle.load(f)
    	except EOFError:
        	os.system('clear')
        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
        	print "ERROR: LIBRARY IS EMPTY!"
		t=0
		time.sleep(2)		
	f.close()
	if(t==1):
		bissto=raw_input("Enter the name of the individual you are issuing the book to ")
		bno=input("Enter the book ID of the book you are issuing ")
		for i,n in lib["name"].items():
			if i==bno:
				bisson=datetime.date.today()
				bissfor=input("For how many days is the book being issued:- ")
               			while(bissfor==0):
                   			print "Number of days has to be greater than 0"
                    			bissfor=input("For how many days is the book being issued:- ")
				lib["issuedto"][bno]=bissto
				lib["issuedfor"][bno]=bissfor
                		lib["issuedon"][bno]=bisson
				f=open("library.txt","w")
				pickle.dump(lib,f)
				f.close()
				os.system('clear')
        	        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
				print "Book has been issued successfully!!"
				print "For the information of ",bissto,", upon failure of returning the book back to the library on time, you will be subjected to late fees of Rs.10 per day "
				time.sleep(5)
				break
		else:
			print"\n\n\nBook ID INVALID"
			time.sleep(2)
		f=open("library.txt","w")
		pickle.dump(lib,f)
		f.close()
def return_book():
	os.system('clear')
	print "LIBRARY MANAGEMENT SYSTEM\n\n"
	f=open("library.txt","r")
    	lib={}
	t=1
        try:
                lib=pickle.load(f)
        except EOFError: 
                os.system('clear')
                print "LIBRARY MANAGEMENT SYSTEM\n\n"
                print "ERROR: LIBRARY IS EMPTY!"    
                t=0
		time.sleep(2)
        f.close()
        if(t==1):
        	bno=input("Enter the book ID of the book being returned:- ")
            	latefees=0		
	        for i,n in lib["name"].items():
                	if i==bno:
				bissfor=lib["issuedfor"][bno]
        			if bissfor==0:
					os.system('clear')
                			print "LIBRARY MANAGEMENT SYSTEM\n\n"
					print "Book is already in the library!"
					time.sleep(2)
				else:
					bisson=lib["issuedon"][bno]        
					timbor=(datetime.date.today()-bisson).days
					if bissfor<timbor:
                				latefees=(timbor-bissfor)*10
                			bisson=datetime.date(1000,01,01)
                			bissfor=0
                			bissto=lib["issuedto"][bno]
                			lib["issuedto"][bno]=""
                			lib["issuedfor"][bno]=bissfor
                			lib["issuedon"][bno]=bisson
                			f=open("library.txt","w")
                			pickle.dump(lib,f)
                			f.close()
                			os.system('clear')
                			print "LIBRARY MANAGEMENT SYSTEM\n\n"
                			print "Book has been returned successfully!!"
                			if latefees!=0:
							print "For the information of ",bissto, ", due to your failure in returning the book back to the library on time you have incurred late fees(",latefess,") you are hereby required to pay the amount within 3 days to avoid further inconvenience"
                			time.sleep(2)
                		break
	        else:
	                print"\n\n\nBook ID INVALID"
	                time.sleep(2)
		f=open("library.txt","w")
                pickle.dump(lib,f)
                f.close()
def remove_book():
	os.system('clear')
	print "LIBRARY MANAGEMENT SYSTEM\n\n"
	f=open("library.txt","r")
	lib={}
	t=1
	try:
        	lib=pickle.load(f)
    	except EOFError:
        	os.system('clear')
       		print "LIBRARY MANAGEMENT SYSTEM\n\n"
        	print "ERROR: LIBRARY IS EMPTY!"
        	t=0
		time.sleep(2)
    	if(t==1):
		bno=input("Enter the book ID of the book being removed:- ")
       		for i,n in lib["name"].items():
        		if i==bno:
				del lib["name"][bno]
        	        	del lib["type"][bno]
                		del lib["author"][bno]
                		del lib["issuedto"][bno]
                		del lib["issuedfor"][bno]
                		del lib["issuedon"][bno]
                		del lib["addedon"][bno]
				f=open("library.txt","w")
                		pickle.dump(lib,f)
                		f.close()
				os.system('clear')
        	        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
                		print "Book has been removed successfully!!"
				time.sleep(2)
				break
		else:
                	print"\n\n\nBook ID INVALID"
                	time.sleep(2)
	f=open("library.txt","w")
        pickle.dump(lib,f)
        f.close()
while(1):
	os.system('clear')				#Main Menu code
    	print "LIBRARY MANAGEMENT SYSTEM\n\n"
	print "1.To add a book"
	print "2.To delete a book"
	print "3.To issue a book to someone"
	print "4.To return a book"
	print "5.To search for a book"
	print "6.To check the status of the library"
	print "7.To exit"
	o=input("Enter the choice:-")
	if(o==1):
		add_book()
	elif(o==2):
		remove_book()
	elif(o==3):
		issue_book()
	elif(o==4):
		return_book()
    	elif(o==5):
        	os.system('clear')
        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
        	f=open("library.txt","r")
        	lib={}
        	t=1
        	try:
            		lib=pickle.load(f)
        	except EOFError:
            		os.system('clear')
            		print "LIBRARY MANAGEMENT SYSTEM\n\n"
            		print "ERROR: LIBRARY IS EMPTY!"
            		t=0
            		time.sleep(2)
            		f.close()
        	if(t==1):
            		bno=input("Enter the book ID of the book you want the details of:- ")
            		for i,n in lib["name"].items():
                		if i==bno:
                    			print "Book ID:-",bno
                    			print "Name:-",lib["name"][bno]
                    			print "Type:-",lib["type"][bno]
                    			print "Author:-",lib["author"][bno]
                    			print "Added on:-",lib["addedon"][bno]
                    			if(lib["issuedfor"][bno]!=0):
                        			print "Issued to:-",lib["issuedto"][bno]
                        			print "Issued on:-",lib["issuedon"][bno]
                        			print "Issued for:-",lib["issuedfor"][bno]
                			else:
                				print "Book is in the library"
		time.sleep(3)
	elif(o==6):
        	os.system('clear')
        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
        	f=open("library.txt","r")
        	lib={}
        	t=1
        	try:
        		lib=pickle.load(f)
        	except EOFError:
            		os.system('clear')
            		print "LIBRARY MANAGEMENT SYSTEM\n\n"
            		nb=0
            		ni=0
            		ninlib=0
            		t=0
            		f.close()
        	if(t==1):
            		os.system('clear')
            		print "LIBRARY MANAGEMENT SYSTEM\n\n"
            		nb=len(lib["name"])
			ni=0
                        ninlib=0
            		for i,n in lib["issuedfor"].items():
                		if n!=0:
					ni+=1
        		ninlib=nb-ni
		print "Number of books belonging to the library=",nb
        	print "Number of books issued=",ni
       		print "Number of books in the library=",ninlib
       		time.sleep(3)
	elif(o==7):
		os.system('clear')
        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
		print "Thank You For Using The Library Management System! :)"
		time.sleep(3)
		os.system('clear')
		break
	else:
		os.system('clear')
        	print "LIBRARY MANAGEMENT SYSTEM\n\n"
		print "Option Entered was INVALID!"
		print "Enter a Valid Option!"

