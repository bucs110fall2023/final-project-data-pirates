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
## CS110 Final Project, Fall Semester 2023

## Team Members
Hilary Rojas Rosales 
Daniela Suqui Estrella
***

## Project Description
A scary interactive game where the player will receive a letter with a message telling them that they have stumbled across a haunted house and they have to escape. The letter will explain the instructions and the player will face three different scenarios, where they will make a decision in order to escape. If the player fails to make the right choice, they will get jumpscared, and lose the game but if they do make the right choice, they will continue playing until they fail or win.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpeg)

### Final Design

![final gui](assets/finalgui.jpeg)

## Program Design

### Features

1. << Feature 1 >>
2. << Feature 2 >>
3. << Feature 3 >>
4. << Feature 4 >>
5. << Feature 5 >>

### Classes

1. GameState - Defines different states of the game: MAIN_MENU, NAME_INPUT, GAMEPLAY. 
2. Window Setup- Handles the game window configuration, including dimensions and title.
3. PlayerInput - Manages user input for entering the player's name and switches between game states.
4. ScenarioDisplay - Displays different scenarios to the player and handles the buttons for choices.
5. GameOutcome - Manages the display of game-over or success screens based on player choices.
6. GameLoop - Controls the continuous execution of the game, handling events, rendering screens, and checking for user input.


## ATP
| Case #   | Description | Steps | Outcome |
| -------- | ----------- | ----- | ------- |
| Test Case 1: Menu Navigation | Verify player can start and quit the game. |  Navigate through the main menu, and confirm that the start button starts the game, and that the quit button quits the game or closes the window.| The main menu should allow the player to start and quit the game when they press the start/quit button. |
| Test Case 2: Volume Button | Verify Player can turn music on and off. | 1. start game. 2. Go to bottom right corner on menu where red button is. 3. Click to turn music off. 4. Click once more to turn music on.| Players control over sounds |
| Test Case 3: Name Check | Verify that the player can input their name | Once the player clicks the start button and then clicks the box that appears. The player will be prompted to input their name which will be later on used during the game. The player should be able to write their name. | The player’s name should be displayed throughout the game. |
| Test Case 4: Jump scare | Verify that when player loses or picks the wrong choice in one of the scenarios, an image pops up. | Start game, and when an scenario appears, they will have to pick yes or no. If they pick the wrong choice, they will be jumpscared.| A jump scare with sound. |
| Test Case 5: | Verify that the game ends once the player makes the wrong decision. | When the player is asked to choose between the choices given, if they choose the wrong one, a “Gave Over” message should be displayed. | The game will display a “Game Over” message when the player makes the wrong choice. |


