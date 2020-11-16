# Kaun Banega Crorepati/Who wants to be a millionare
# Introduction
This is a replica of famous entertainment show kaun Banega Crorepati(Who wants to be a millionare)
There are two parts of this game, first part is called as the fastest finger first where multiple players get the same question and the players have to select the options in the correct order. To acheive this  I used server socket programming where one machine can be used as a host/server machine and others are client machines
The question is sent from the server to client, the client's time is recoreded and then sent to the host machine, the host machine then selects the player with the shortest time
The winner gets to play the main game
# External Libraries used-
1. PIL
2. ImageTK
3. pyhton-mysql connector
# Steps
1. Create database named 'kbc' without quotes
2. Copy and paste txt files inside mysql to create necessary tables and populate them.
3. Run firstregister.py on client machine, register your details, after submission you will taken to rules screen, wait here.
4. Run multiclientserver.py on server machine, after running this program immediately click on start on client machine as server will only accept response for 25 seconds only
5. Select the options in correct sequence, the winner will be displayed on the host machine on the python console
7. Run gamerules.py on winners machine or any machine to play the main game
