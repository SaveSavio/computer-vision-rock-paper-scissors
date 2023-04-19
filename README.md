# Computer Vision RPS
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera. 

## Milestone 1: set up the environment

- In this project, we'll use GitHub to track changes to our code and save them online in a GitHub repo.
An automated bot provided by AI Core automatically creates a new GitHub repo called "computer-vision-rock-paper-scissors".

We have cloned the GitHub repo on our local machine.

## Milestone 2: create a computer vision system (model)

- We created a computer vision system with the tool provided by https://teachablemachine.withgoogle.com/
This is *"A fast, easy way to create machine learning models for your sites, apps, and more – no expertise or coding required"*

We have selected a "Image Project" and trained the model to recognize three classes: Rock, Paper, and Scissors. For this project, I have trained my model by taking snapshots of my hands whilst representing the three classes of the game.

After a quick validation with the provided tool, we have exported the model and labels as the following files:
- keras_model.h5
- labels.txt

We have copied those two files in the local repo "computer-vision-rock-paper-scissors" and then staged, committed and pushed the repo.