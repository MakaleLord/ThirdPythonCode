
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


def race(track, player_car, computer_car): 
    player = random.randint(15,30)
    computer = random.randint(15,30)
    
    print(player_car, track*player)
    print(computer_car, track*computer)
 
    if player > computer: 
        print(F"You're a winner by {player - computer} lengths!") 
    elif player == computer:
        print("Draw, got the same lengths")
    else: 
        print(F"You got beat by {computer - player} lengths")


print("Race 1")
print()
race("_", "&#128663;", "&#127950;")

print()
print("Race 2")
race("_", "&#128663;", "&#127950;")
