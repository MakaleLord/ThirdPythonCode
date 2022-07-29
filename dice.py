
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   min-width:55%;
   max-width:100%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 28px;
  text-align:right;
  white-space: pre;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")
import magicwand

import random 

player = random.randint(1,6)
computer = random.randint(1,6)

def dice(num):
    if (num == 1) :
        print("&#9856;")
    elif (num == 2) :
        print("&#9857;")
    elif (num == 3) :
        print("&#9858;")
    elif (num == 4) :
        print("&#9859;")
    elif (num == 5) :
        print("&#9860;")
    else:
        print("&#9861;")
        
print("You got: ", player)
dice(player)

print("Computer got: ", computer)
dice(computer)


if player > computer: 
    print("Congratulations! You Won.")
elif player == computer:
    print("It's a draw")
else: 
    print("YOU LOST!!.")
