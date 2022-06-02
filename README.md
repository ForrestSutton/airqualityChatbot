#Air Quality ChatBot
this is a simple app that uses Googe cloud functions to scrape a json feed from a purple air monitor and if the air quaility index is 50 or higher it notifies google chat space  
this has only been tested with a purple air quality monitor but it should work on any monitor that produces a json feed


steps to use this script
1. create a chat space
2. in the space create a web hook, do not share and do not make public
3. create a new google cloud function with an http trigger that is using python3.7  runtime
4. If you have a purple air sensor you can use your link if you don't look for one near where you want to measure the air and grab its link
5. create a google scheduler that calls the http address when you need it called
6. invite your chat users into your new space
7. profits 

#next steps 
1. I would like to add a database to store key air quaility measures
2. I would like to allow chat users to ask simple questions of the bot about air quality and possible weather \

#update as of June 2022 Purple air has updated their api so you will need a new url, and key that you can request from them 
