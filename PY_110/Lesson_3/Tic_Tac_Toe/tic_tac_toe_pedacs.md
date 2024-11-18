### Improved Join function

Create a function that joins items in a list and seperates the last item with 'or'.  
Note that `join_or` has more functionality than we need for this program;  for instance, it lets you specify different delimiters and different words for the last item. Make sure that you test the additional features even if you don't need them in your program; you may need this function again some day.

Examples:  
print(join_or([1, 2, 3]))               # => "1, 2, or 3"  
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"  
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"  
print(join_or([]))                      # => ""  
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"  

#### Problem

- Input:  
A List, delimeter (default is `,`), a join word (default argument is `'or'`)
- output:  
String

- Explicit rules:  
List can be empty or contain only one single element

- Implicit rules:  
White space must be added after the delimeter.  
White space must be added before and after the join word.  

#### Examples / Test Cases

print(join_or([1, 2, 3]))               # => "1, 2, or 3"  
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"  
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"  
print(join_or([]))                      # => ""  
print(join_or([5]))                     # => "5"  
print(join_or([1, 2]))                  # => "1 or 2"  

#### Data Structure

Not needed

#### Algorithm

-- High Level:  

- Function must have three parameters with the last two parameters having default values.  
- If input list is empty, return an empty list.  
- If input list has one value, return the value as a string.  
- If input has two value, return those value seperated by the join word or default as string.  
- If input has more than three value, return the concantenation of all the value.  
  - Add the delimiter between each pair of values.  
  - Add the join word for the last value.
  - Return string  

### Keep Score

Keep track of how many times the player and computer each win, and report the scores after each game. The first player to win 5 games wins the overall match (a series of 2 or more games). The score should reset to 0 for each player when beginning a new match. Don't use any global variables. However, you may want to use a global constant to represent the number of games needed to win the match.

#### Problem

- Input:  
Integer which increases player or computer count for each win
- output:  
winner when winning condition is met.

- Explicit rules:  
Scores Should reset to zero for each player at the start of the match
- Do not use any global variables
- You can use a global constant to represent the number of games needed to win.

- Implicit rules:  

#### Examples / Test Cases

#### Data Structure

A Dictionary would best since we can access the value via the key and increase it after each round of game.

#### Algorithm

-- High Level:  

1. Create an empty dictionary to keep track of the game scores with keys being `player`, `computer` and set the initial value to `0`.
2. For a game round of tic-tac-toe, if winner is `player` or `computer`, increase their respective values by 1.
3. If no winner, values remain unchanged.
4. Check if the value is equall to the winning value
    - if yes, return winner.
    - if not, repeat step 2 and 3
5. Display the final score of the the game and display winner.

### Computer AI: Defense

The computer currently picks a square at random. That's not very interesting. Let's make the computer defensive-minded so that, when an immediate threat exists, it will try to defend the 3rd square. An immediate threat occurs when the human player has 2 squares in a row with the 3rd square unoccupied. If there's no immediate threat, the computer can pick a random square.

#### Problem

- Input:  
Moves made by both the player and the computer.
- output:  
The computer’s move to either block the player or pick a random square.

- Explicit rules:  
An immediate threat occurs when the human player has 2 squares in a row with the 3rd square unoccupied.  
In the absence of an imediate threat, the computer can pick a random square.

- Implicit rules:  

#### Examples / Test Cases
Depends on the game in play, for example, if player marks position 1, 5 (needs 9 to have a winning combination), computer must place at 9. If no winning case in view, computer randomly selects a position

#### Data Structure

Using a list comprehension to retrieve winning combinations

#### Algorithm

-- High Level:  

1. Check for immediate threat before computer makes a move by iterating over all winning combination
2. If any winning combination has two player markers, return the free position 
3. Computer next play must be the free postion
4. If there is no immediate threat, computer picks a random choice 
