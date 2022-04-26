## INSTRUCTION:

1. **Update your current** `forked repository` with respect to the `upstream-main`.
2. Go through the **videos** listed in the README in Python domain folder and get your self familiar with the python syntax.


## TASK :

I think everyone must have played **LUDO** in your childhood, where you had to roll a dice and you get a score between 1 to 6. Which offcourse used to move your player in the ludo board.

But in this task you have to do a little bit different .......

In this task there are two players **PLAYER_1** and **PLAYER_2** .They will be rolling dice alternatively and their score will be added to their previous score (initial score = 0). First player to reach the goal (User input) will be the winner.

But here is a twist ...

1. If score will exceed the goal then the recently generated score will be discarded.

    Example:
	
	if PLAYER_1 point is 48 and the goal is 50 and PLAYER_1 rolls the dice and get  4 as score then it will discard the score 4 as it exceeds the goal (48+4=52). And if PLAYER_1 score is 1 or 2 then it will be added to the point as 48+1=49 or 
	48+2=50 (winner as player point is equal to goal) which are oviously less than equal to the goal (here 50).

2. Winner will be decleared only if player point is equal to goal (mentioned in example).


## PYHTON LIBRARY USED FOR THIS TASK:
1. [RANDOM](https://www.geeksforgeeks.org/python-random-module/)

## Submission
1. Create a folder with your name inside `Python/task` folder and add the python file as well as a screenshot of the output.

2. commit, push and create a new pull request.