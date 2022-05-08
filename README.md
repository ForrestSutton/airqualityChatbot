#Air Quality ChatBot
this is a simple app that uses Googe cloud functions to scan a purple air monitor and if the air quaility index is 50 or higher it notifies google chat space  


steps to use this script
1. create a chat space
2. in the space create a web hook, do not share and do not make public
3. create a new google cloud function with an http trigger that is using python3.7  runtime
4. If you have a purple air sensor you can use your link if you don't look for one near where you want to measure the air and grab its link
5. create a google scheduler that calls the http address when you need it called
6. invite your chat users into your new space
7. profits 
