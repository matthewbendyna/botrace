#!python3
#botrace.py
#by Matthew Bendyna, aka Author Rykon Volta
#this program will race a number of bots that are given two attributes, speed and
#endurance, and then the bots will run a 1 km(1000m) race at their top speeds
#speed will be a random value between 1m/s and 5m/s, while endurance
#will be a random value between 10m and 50m. A bot with high speed may lose
#to a bot with slightly lower speed if the high speed bot has a low endurance
#and the lower speed bot has a higher endurance.
#endurance describes how long the bot can run without taking a break.
#When the endurance bar reaches 0, the bot takes a five second break before
#continuing with the endurance bar replenished
#This is a zero player game with 

import pyinputplus as pyip, threading, time, random, sys

global stats
stats={
    "Bot": "Total Time"
    }

class Bot:
    def __init__(self, name, speed, endurance):
        self.name=name
        self.speed=speed
        self.endurance=endurance

def run(botname, botspeed, botendurance):
    global stats
    starttime=time.time()
    track=1000
    distance=0
    complete=False
    endurance=botendurance
    while complete==False:
        time.sleep(.01)
        distance+=botspeed
        endurance-=botspeed
        if distance>=1000:
            endtime=time.time()
            break
        if endurance<=0:
            time.sleep(.05)
            endurance=botendurance
    totaltime=round((endtime-starttime)*100, 2)
    stats[botname]=totaltime
    return

def main():
    global stats
    threads=[]
    bn=input("\nHow many bots will be racing this round? Maximum of 10 bots allowed: ")
    try:
        bn=int(bn)
    except:
        print("\nInput must be an integer value...")
        main()
    if bn>10:
        print("\nToo many bots. Maximum of 10 bots allowed on the track.")
        main()
    if bn<1:
        print("\nNot enough bots. Must have at least one bot on the track.")
        main()
    bot1=Bot("Bot 1", random.randint(1,5),random.randint(10,50))
    b1=threading.Thread(target=run, args=[bot1.name, bot1.speed, bot1.endurance])
    threads.append(b1)
    b1.start()
    if bn>=2:
        bot2=Bot("Bot 2", random.randint(1,5),random.randint(10,50))
        b2=threading.Thread(target=run, args=[bot2.name, bot2.speed, bot2.endurance])
        threads.append(b2)
        b2.start()
    if bn>=3:
        bot3=Bot("Bot 3", random.randint(1,5),random.randint(10,50))
        b3=threading.Thread(target=run, args=[bot3.name, bot3.speed, bot3.endurance])
        threads.append(b3)
        b3.start()
    if bn>=4:
        bot4=Bot("Bot 4", random.randint(1,5),random.randint(10,50))
        b4=threading.Thread(target=run, args=[bot4.name, bot4.speed, bot4.endurance])
        threads.append(b4)
        b4.start()
    if bn>=5:
        bot5=Bot("Bot 5", random.randint(1,5),random.randint(10,50))
        b5=threading.Thread(target=run, args=[bot5.name, bot5.speed, bot5.endurance])
        threads.append(b5)
        b5.start()
    if bn>=6:
        bot6=Bot("Bot 6", random.randint(1,5),random.randint(10,50))
        b6=threading.Thread(target=run, args=[bot6.name, bot6.speed, bot6.endurance])
        threads.append(b6)
        b6.start()
    if bn>=7:
        bot7=Bot("Bot 7", random.randint(1,5),random.randint(10,50))
        b7=threading.Thread(target=run, args=[bot7.name, bot7.speed, bot7.endurance])
        threads.append(b7)
        b7.start()
    if bn>=8:
        bot8=Bot("Bot 8", random.randint(1,5),random.randint(10,50))
        b8=threading.Thread(target=run, args=[bot8.name, bot8.speed, bot8.endurance])
        threads.append(b8)
        b8.start()
    if bn>=9:
        bot9=Bot("Bot 9", random.randint(1,5),random.randint(10,50))
        b9=threading.Thread(target=run, args=[bot9.name, bot9.speed, bot9.endurance])
        threads.append(b9)
        b9.start()
    if bn>=10:
        bot10=Bot("Bot 10", random.randint(1,5),random.randint(10,50))
        b10=threading.Thread(target=run, args=[bot10.name, bot10.speed, bot10.endurance])
        threads.append(b10)
        b10.start()
    for thread in threads:
        thread.join()
    print("Race Complete!!!")
    print("Stats:".center(25, "-"))
    for key, value in stats.items():
        if key=="Bot":
            print(key+'      '+value+' in Seconds')
            print("-"*30)
            continue
        elif int(value)<1000:
            if len(str(value))==6:
                sec="  seconds"
            elif len(str(value))==5:
                sec="   seconds"
            elif len(str(value))==4:
                sec="    seconds"
            else:
                raise Exception("Unkown digit length at line 129")
        else:
            if len(str(value))==7:
                sec=" seconds"
            elif len(str(value))==6:
                sec="  seconds"
            elif len(str(value))==5:
                sec="   seconds"
            else:
                raise Exception("Unkown digit length at line 138")
        if key=="Bot 10":
            print(key+": "+str(value)+sec)
        else:
            print(key+":  "+str(value)+sec)
    retry=pyip.inputYesNo(prompt="Would you like to run another bot race? (y/n) ")
    if retry=='yes':
        main()
    else:
        print("Thank you for playing Bot Race! Hope to see you again soon! :)")
        time.sleep(5)
        sys.exit()
        
print("Botrace")
print("\nDescription: races a number of bots with varying attributes across a virtual 1km track.")
print("Each bot will have two attributes: speed and endurance")
print("You will specify the number of bots you would like to race and either manually enter their attributes or type random to give a random attribute.")
print("Random will give you a random selection, differing for each attribute.")
print("Selecting a random speed will result in a random selection between 1m/s and 5m/s.")
print("Selecting a random endurance level will result in a random selection between 10m and 50m")
print("The speed determines how fast your bot will cover meters while in motion.")
print("The endurance determines how many meters a bot can run before it must take a five second break to rest, adding diversity that makes speed not necessarily as important.")
print("A robot with low speed and high endurance might win against a robot with high speed and low endurance.")
print("A second for a robot will be 1/100th or .01 seconds for a human so that the race doesn't take over 1000 seconds for a slow bot. Reduced time factor makes a faster race and faster simulated results.")
print("Now, enough explanation, let us set up a bot race...\n")
main()

