#authored by kchadha 03/20/2014
#simple Python Bot meant for logging purposes. 


import socket
import sys
import datetime
import time


server = "ircserver.ece.arizona.edu"       #settings
channel = "#acl"
botnick = "bot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :hoila!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")        #join the chan

print "connected to %s" %channel;

def ping(): # This is our first function! It will respond to server Pings.
  irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!) 

def privmsg(nick,destination,message,st):
  print text;	
  print "%s %s -> %s  %s" %(st,nick,destination,message); 

def topic(nick,destination,message,st):
  print "%s TOPIC changed %s -> %s to -> %s" %(st,nick,destination,message); 

while 1:    #puts it in a loop
   ts = time.time()
   st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

   text=irc.recv(2040)  #receive the text
   text = text.strip('\n\r')
   nick = text.split('!')[ 0 ].replace(':',' ') #The nick of the user issueing the command is taken from the hostname
   message = ':'.join(text.split (':')[2:]) #Split the command from the message
   destination = ''.join (text.split(':')[:2]).split (' ')[-2] #Destination is taken from the data
   if text.find("PING :") != -1: # if the server pings us then we've got to respond!
      ping();

   if text.find('PRIVMSG') != -1: #IF PRIVMSG only then display
      privmsg(nick,destination,message,st);	

   if text.find('TOPIC') != -1: #IF PRIVMSG only then display
      topic(nick,destination,message,st);	
      
