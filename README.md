# Git & GitHub

Objective:  Familiarize yourself with essential Git and GitHub commands and workflows. Get hands-on practice with creating repositories, making commits, working with branches, and handling merge conflicts. 

Submission: After following all of the instructions below, add me (byu-kerby) as a collaborator (under settings in GitHub) to your repository and add your repo's link below. Be sure to commit your changes and push to GitHub (if updating this locally).

Link: [Your GitHub Username Here](Your Link Here)

Instructions:  

## Initializing a new repository
1. Create an empty folder called `git_practice` in a sensible location on your computer. 
2. Navigate into the new folder
3. Initialize the folder as a git repository.  
    * *Remember that every project should be its own git repository.*
    * *Do NOT initialize root directories or parent folders relating to different projects*
4. Verify that the .git folder is now in the directory.

## Making your first commit
1. Check the git status 
2. Create a new file called `file_1.txt` 
3. Create another new file called `file_2.txt` 
4. Check the git status 
5. Add both files to the staging area
6. Check the git status
7. Commit the new files using the commit message "create new files"
8. Check the git status 
9. Check the git log 

## More git practicing
 1. Open `file_1.txt` in a text editor.   Add the following to the file:
    ```
    This is my first file.
    ```
2. Open the the `file_2.txt` in a text editor.  Add the following to the file: 
    ```
    This is my second file.
    ```
3. Save the changes to both files.  Check the git status
4. Add and commit only the changes from the `file_1.txt` file.  Check the git status.
5. Make another commit with only the changes from the `file_2.txt` file.
6. Check the git log

## Creating a Readme file
1. Create a file called "Readme.md"
2. Write a description of the repository with a title
3. Add and commit the readme file.
    
## Creating a .gitignore
1. Create a .gitignore file with the following text "api-keys.txt" 
2. Add and commit the .gitignore file
3. Create a file called "api-keys.txt" 
4. Check the status of the git repo
5. Add some text to the "api-keys.txt" file.  Save the changes and check the status. 
6. IMPORTANT:  For best results, add all files that you want to ignore to the .gitignore file **before** any of the ignored files get committed. (Git will still track and push files that were committed before they were added to the .gitignore.)  

## Creating branches
1. Make a new branch called "features"
2. Switch to the "features" branch
3. Look at the log and notice where HEAD is
4. Create a new file called `new_features.txt`
5. Add and commit the new file with an appropriate commit message.
6. Open `new_features.txt` in a text editor.   Add the following to the file:
    ```
    This file will have some new features.
    ```
7. Commit the changes to the current ("features") branch

## Merging
1. Switch back to the main branch.  Notice the "new_features.txt" file is no longer in the directory. 
2. Open "file_1.txt" and add a line of text to the file.  
3. Commit the changes.
4. Merge the main branch with the "features" branch.  (Your default editor should open to ask you for a commit message.  Type your message and close the file.) 
5. Look at the git log.

## Handling Merge Conflicts
 1. While on the main branch, open the `new_feature.txt` file and **replace** the old text with `No new features will be created.`  Save the changes. 
 2. Add and commit the changes.
 3. Switch back to the "features" branch.
 4. Open the "new_features.txt" file and **replace** the old text with `This file has some new text`. Save the file.
 5. Add and commit the changes on the features branch
 6. Switch back to the main branch. 
 7. Merge the main branch with the "features" branch.
 8. You should get a merge conflict error and your default editor will open to have you resolve the conflict.
 9. Resolve the conflict and commit the merge.
10. Delete the `features` branch.
 
## Pushing to GitHub
1. Login to GitHub and create a blank repository  called "Git_practice.  Do not initialize it with a readme file or a .gitignore file.
2. Copy the SSH url (if you set up ssh keys).
3. In your local repository, set the remote branch by typing `git remote add origin <ssh url>`
4. Push the local repo up to GitHub by typing `git push -u origin main`
5. Check that your GitHub repo was updated with your local work.

## Pulling from GitHub
1. Make changes to your Readme.md file **directly on GitHub**.
2. Sync your remote changes by running `git pull` (locally).
3. Verify that your changes were made.

## Share with Me
1. Add me (byu-kerby) as a collaborator to your repository.
***
