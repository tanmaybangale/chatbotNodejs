# chatbotNodejs
Aim : Web app using Nodejs for creating chatbot that can identify intent of asking weather by user and tell weather for asked location. 

## design model
The server is powered by Nodejs and uses expressjs framework.The user input is passed on to python worker using socket.The python script uses opensource adapt intent api for identfying whether user is asking for weather information.The appropriate response is set.

## current progress
Hosting html page using Nodejs. Connecting with Python socketclient. Idenfying intent. Using openweather api for fetching weather is yet to be added.


