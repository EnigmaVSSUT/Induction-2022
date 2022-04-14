# Task 2

Hopefully in the last task you got some basic idea on what git and GitHub is and how to use it to collaborate on projects.

In this task you'll learn some more useful git commands.

## Objective for this task
Your objective for this task is to update the text file you created in task 1 and add a field for the domain you're interested to work on in Enigma.

## How to do that?

Now, anytime any changes take place in the main repository, your forked repository must <code>pull</code> those changes from the main repository before it can <code>push</code> other changes to the main repository.




1) For that, go to the [Enigma repository](https://github.com/EnigmaVSSUT/Induction-2022) and copy the repo address just like you copied your forked repo's address in task 1.


2) now open gitbash in your cloned repo and type <code>git remote add upstream <i>\<copied repo address></i> </code>. This adds a reference to the main repository from which we can pull the updates.


3) Now enter <code>git pull upstream main</code>. this should now pull all the changes that have been made to the main repo from merging the pull requests.

4) Now you need to find your txt file that you created in task 1 and add in which domain you'd like to work on.
5) Now add, commit and push the changes just like you did in task 1 and create a pull request. 


# Congrats on completing task 2 on git and GitHub! 


