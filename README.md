[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803274&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

[1] project title
[1] course number 
[1] semester
[3] project overview
[2] Lists additional modules with citation
[2] Class relationship diagram
[5] Data Permanence Feature
[3] Contains screenshots of the Final GUI
[2] Project file structure
[5] contains a copy of your ATP in table format
[5] Template text removed, proofread, etc.

# Deadly Decisions
## CS110 Final Project, Fall Semester, 2023

## Team Members
Hilary Rojas Rosales 
Daniela Suqui Estrella
***

## Project Description
A scary interactive game where the player will receive a letter with a message telling them that they have stumbled across a haunted house and they have to escape. The letter will explain the instructions and the player will face three different scenarios, where they will make a decision in order to escape. If the player fails to make the right choice, they will get jumpscared, and lose the game but if they do make the right choice, they will continue playing until they fail or win.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Feature 1 >>
2. << Feature 2 >>
3. << Feature 3 >>
4. << Feature 4 >>
5. << Feature 5 >>

### Classes

- << You should have a list of each of your classes with a description >>

## ATP
Test Case 1: Menu Navigation
Test Description: Verify player can start and quit the game
Test Steps: Navigate through the main menu, and confirm that the start button starts the game, and that the quit button quits the game or closes the window.
Expected Outcome: The main menu should allow the player to start and quit the game when they press the start/quit button.

Test Case 2: Volume Button
Test Description: Verify Player Can turn music on and off
Test Steps:
1.start game
2.Go to bottom right corner on menu where red button is
3.Click to turn music off
4.click once more to turn music on
Expected Outcome: Players control over sounds

Test Case 3: Name Check
Test Description: Verify that the player can input their name.
Test Steps: Once the game starts, the player will be prompted to input their name which will be later on used ..verify that the player is asked to input their name and that they can do so.
Expected Outcome: The player’s name should be displayed in the game.

Test Case 4: Jump scare
Test Description: Verify that when player loses in the room an image pops up
Test Steps:Start game, choose questions.If player chooses the answer no willing to interact with stuff, they will be jumpscared
Expected Outcome: A jump scare which leads to game over

Test Case 5: Game Over Condition
Test Description: Verify that the game ends once the player makes the wrong decision.
Test Steps: When the player is asked to choose between the choices given, if they choose the wrong one, a “Gave Over” message should be displayed.
Expected Outcome: The game will display a “Game Over” message when the player makes the wrong choice.

## ATP
| Case #   | Steps   | Outcome| Steps | Outcome |  ------- | -------|
| -------- | ------- | -------|
| Test Case 1: Menu Navigation | Go to the center of the display and click on the "Click To Play" text to begin the game. | The game initializes immediately and the timer begins to go down.|
| Test Case 2: Volume Button | Follow the orange circles and click on them in whichever order they appear. | Each time the orange circle is clicked on, the score increases by 1 point and the score tracker shows that occurring in the top left corner. | 
| Test Case 3: Name Check | Timer decreasing as long as game is still running| Timer tracker decreases each second until the 30 seconds are up and the game ends. | 
| Test Case 4: Jump scare |When an orange circle is clicked properly in the boundaries of the circle. | The orange circle disappears and another circle reappears in another position.|
| Test Case 5: |After 30 seconds passes and the timer tracker is down to 0, the game ends| Final Score display is shown and the player is congratulated and shown their final score| 
| 6 | If circle is not clicked or not clicked in the given time that it appears on display| The circle disappears and another appears in another random position. |


