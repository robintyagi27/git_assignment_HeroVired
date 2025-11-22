# Steps Involved:

1. **Repository Setup**:
    - Create a repository named `git_assignment_HeroVired`.
    - Clone the repository and navigate to the project directory:
      ```bash
      git clone https://github.com/<your-username>/git_assignment_HeroVired.git
      cd git_assignment_HeroVired
      ```

2. **Create and Switch to `dev` Branch**:
    - Create a `dev` branch and switch to it:
      ```bash
      git checkout -b dev
      ```

3. **Add Initial Code**:
    - Add the provided `Calculator` class code to a file named `calculator.py`.
    - Commit the changes:
      ```bash
      git add calculator.py
      git commit -m "Adding code chnages for generic functions"
      ```
      
4. **Merge `dev` Branch into `main` and Release Version 1**:
    - Switch to the `main` branch:
      ```bash
      git checkout main
      ```
    - Merge the `dev` branch:
      ```bash
      git merge dev
      ```
    - Tag the release:
      ```bash
      git tag -a v1.0.0 -m "Release version 1.0.0 of Calculator Plus App"  
      git push origin v1.0.0
      ```

5. **Add Collaborator**:
    - Add a classmate as a collaborator via the repository settings on GitHub.

6. **Create `feature/sqrt` Branch**:
    - Create a new branch for the square root feature:
      ```bash
      git checkout -b feature/sqrt
      ```
      
7. **Implement Square Root Function**:
    - Uncomment and implement the `square_root` function in the `Calculator` class:
      ```python
      def square_root(self, x):
            if x < 0:
                 raise ValueError("Cannot calculate the square root of a negative number.")
            return math.sqrt(x)
      ```
    - `git stash`

8. **Fix Critical Bug in `divide` Function in dev branch**:
    - Switch to the `dev` branch:
      ```bash
      git checkout dev
      ```
    - Update the `divide` function:
      ```python
      def divide(self, a, b):
            if b == 0:
                 raise ValueError("Cannot divide by zero.")
            return a / b
      ```
    - Commit the fix:
      ```bash
      git add .
      git commit -m "Fixed divide function to handle division by zero"
      ```
    - Push the changes:
      ```bash
      git push origin dev
      ```

9. **Rebase `feature/sqrt` Branch**:
    - Switch back to the `feature/sqrt` branch:
      ```bash
      git checkout feature/sqrt
      ```
    - Rebase the branch to include the latest changes from `dev`:
      ```bash
      git rebase dev
      git stash pop
      ```

10. **Complete and Test Square Root Feature**:
     - Ensure the square root feature works correctly by testing it in the `main` function.
     - Commit the changes:
        ```bash
        git add .
        git commit -m "Implement square root feature"
        ```

11. **Create Pull Request**:
     - Push the `feature/sqrt` branch:
        ```bash
        git push origin feature/sqrt
        ```
     
12. **Code Review and Merge**:
     - Request a code review from a team member.
     - Address any feedback and update the pull request if necessary.
     - After approval, merge the `feature/sqrt` branch into the `dev` branch:
        ```bash
        git checkout dev
        git merge feature/sqrt
        ```

13. **Test and Release Version 2**:
     - Test the application in the `dev` branch.
     - Merge the `dev` branch into the `main` branch:
        ```bash
        git checkout main
        git merge dev
        ```
     - Tag the release:
        ```bash
        git tag -a v2.0.0 -m "Release version 2.0.0 of Calculator Plus App"
        git push origin v2.0.0
        ```
    - add release note
