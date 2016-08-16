# Tic-tac-toe

## Introduction
This is a simple tic-tac-toe game made using Python 3.2.3. You can play against either another player or a bot, with the bot having two difficulties.

## The code
At the time of making this game, I did not know too much about AI and programming in general. This is evident in the way I implemented the victory conditions and the bot.

### Victory conditions
Since tic-tac-toe is a game with few permutations (unlike chess), I was able to list out all the possible victory conditions. The program just has to check any of the possible several victory conditions were met.

### The bot
As stated earlier, there are two difficulties for this bot. The easier difficulty just involves randomly selecting an empty cell to place the O or X. The harder difficulty makes it impossible for the player to achieve a victory, either by the bot winning the game or drawing a tie. Since tic-tac-toe has very few board permutations, the bot can choose the best possible outcome for itself, which is to place an O or X which secures a victory or tie for itself.