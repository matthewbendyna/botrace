# botrace
A simulated bot race on a 1 km track that let's you race 1-10 robots. Random speed and endurance values for each bot.

Full Description: races a number of bots with varying attributes across a virtual 1km track.
Each bot will have two attributes: speed and endurance
You will specify the number of bots you would like to race and either manually enter their attributes or type random to give a random attribute.
Random will give you a random selection, differing for each attribute.
Selecting a random speed will result in a random selection between 1m/s and 5m/s.
Selecting a random endurance level will result in a random selection between 10m and 50m
The speed determines how fast your bot will cover meters while in motion.
The endurance determines how many meters a bot can run before it must take a five second break to rest, adding diversity that makes speed not necessarily as important.
A robot with low speed and high endurance might win against a robot with high speed and low endurance.
A second for a robot will be 1/100th or .01 seconds for a human so that the race doesn't take over 1000 seconds for a slow bot. Reduced time factor makes a faster race and faster simulated results.
Now, enough explanation, let us set up a bot race...
