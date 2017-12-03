# chatbotNodejs
Aim : Web app using Nodejs for creating chatbot that can identify intent of asking weather by user and tell weather for asked location. 

## design model
The server is powered by Nodejs and uses expressjs framework.The user input is passed on to python worker using socket.The python script uses opensource adapt intent api for identfying whether user is asking for weather information.The appropriate response is set.

## expected working
The user chats and bot generates appropriate response. User asks for weather for location and bot replies with the same.

## current working
The user messages as received via socket to python code for appropriate parsing and revert response.


## completed modules and parts
1 Hosting html page using Nodejs and connecting with Python socketclient to transfer user message for appropriate parsing. 2 Module for identifying intent. 

## yet to be done
Intergrating intent module and then using openweather api for fetching weather.


