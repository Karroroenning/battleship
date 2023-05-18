# Battleships

![Picture of, am i responsive to all differents screensizes](/Images/am_i_responsive.png)

## **How To Play**


This is a classic battleship game.
The rules are simple.
This is a game that you play against the computer.
The player Begins by placing his own ships on his map. You must put out ships that are 2, 3 or 4 columns long.
The player does not see where the computer deploys its ships.
When you have deployed your 3 ships, the game is started. Then you have to write where you want to put your first "peg" on the computer's map to guess where it has its boats. When it is a miss a "-" shows up on the map and when it is a hit a "X" show up on the map.
You guess every other time until one has sunk the other's ship.


## Features

**Existing Features**

- Start

When the game runs the text BATTLESHIPS comes up and the text how the player will deploy there ships to the board. 

![Start screen, where player will set there boats.](/Images/start.png)

- Players gameboard. Computer does not see this.

Before the game starts, the player gets to see where he has placed his three ships.

![Players gameboard, where they put there ships](/Images/player_ships.png)

- Start to attack the computers ships on the board.

Time to attack. You first choose which number to put and then the letter. So you choose position in both horizontal and vertical.

![](/Images/guess.png)

- Hit and miss

The computers game board and the players game board are shown here. "-" is a miss and "X" is a hit.

![Hit and miss](/Images/hit_miss.png)


**Future Features**

- Want to develop so that you have a first page so that you can start the game with enter.
- Have multiple ships
- Easier to guess where the ships are. For example 3G. 
- Add your High scores

## Data model

## Testing

**Solved Bugs**


- I had a bug after I had placed my ships, that I saw where the computers had their ships before the game started. I had written that you would see it. So I removed it and that fixed it.


![Printed out that we would see the computer ships before the game startde.](/Images/bug.png)


- I got an error message on PEP8 so I fixed it
![bug from PEP8](/Images/bug_from_pep8.png)

- I had accidentally switched places on [column][i] so when you were to deploy your ships, it deployed the first ship automatically.
![switched places on column and i.](/Images/change_column.png)

- When i for example press enter instead of a number when i should press a number it came up an error message.
I had typed TypeError on all of them.
![TypeError on all of them.](/Images/typeError.png)


**Validator testing**


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:

- Clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJs in that order
- Link the Heroku app to the repository
- Click Deploy

## Credits
- [Battleship Game code in python](https://copyassignment.com/battleship-game-code-in-python/)
- [Mushbt on github](https://github.com/Mushbt/battleships-pp3/blob/main/run.py)
- My start text "Battleship" is all taken from [sean-meade on github](https://github.com/sean-meade/cli-battleship-game/blob/main/run.py)