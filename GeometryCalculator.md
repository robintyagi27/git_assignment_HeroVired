# Steps Involved:
## Step 1: Create a New Branch for Circle Area Feature
A. Create a new branch named `feature/circle-area` and add the code for calculating area for the circle :

    ```bash
    git checkout -b feature/circle-area
    git add .
    ```
 
## Step 2: Stash Changes for Circle Area Feature
A. Stash the incomplete changes:

    ```bash
    git stash
    ```

B. Verify that the working directory is clean:

    ```bash
    git status
    ```

## Step 3: Create a New Branch for Rectangle Area Feature
A. Create a new branch named `feature/rectangle-area` and add the code for calculating area for the rectangle :

    ```bash
    git checkout -b feature/rectangle-area
    git add .
    ```

## Step 4: Stash Changes for Rectangle Area Feature
A. Stash the incomplete changes:

    ```bash
    git stash
    ```

B. Verify that the working directory is clean:

    ```bash
    git status
    ```

## Step 5: Switch Back to Circle Area Branch
A. Switch back to the `feature/circle-area` branch:

    ```bash
    git checkout feature/circle-area
    ```
    
    B. Retrieve the stashed changes:
    
    ```bash
    git stash apply "stash@{1}"
    ```

C. Complete the circle area feature implementation and save the changes.

## Step 6: Commit and Push Circle Area Feature
A. Commit the changes:

    ```bash
    git add .
    git commit -m "Completed circle area feature"
    ```

B. Push the changes to the remote repository:

    ```bash
    git push origin feature/circle-area
    ```
    
## Step 7: Switch Back to Rectangle Area Branch
A. Switch back to the `feature/rectangle-area` branch:

    ```bash
    git checkout feature/rectangle-area
    ```

B. Retrieve the stashed changes:

    ```bash
    git stash pop
    ```

C. Complete the rectangle area feature implementation and save the changes.

## Step 8: Commit and Push Rectangle Area Feature
A. Commit the changes:

    ```bash
    git add .
    git commit -m "Completed rectangle area feature"
    ```

B. Push the changes to the remote repository:

    ```bash
    git push origin feature/rectangle-area
    ```
## Step 9.a: Create Pull Requests
A. Create a pull request to merge feature/circle-area branch to dev after review.
## Step 9.b: Create Pull Requests
A. Create a pull request to merge feature/rectangle-area branch to dev after review.
## Step 10: Review and Merge
A. After review , merge the changes to main branch.
