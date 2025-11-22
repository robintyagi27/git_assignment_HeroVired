### Question 1: CalculatorPlus Application (Total: 20 Points)  
- **Task Completion**: 18 points  
- **Code Review**: 2 points (Help at least one classmate by reviewing their code)  

#### Steps:  
1. Create a repository `git_assignment_HeroVired`.  
2. Create a `dev` branch and add the provided code.  
3. Implement the `square_root` function.  
4. Merge the `dev` branch into `main` and release version 1.  
5. Add a collaborator to the repository.  
6. Create a `feature/sqrt` branch and implement the square root feature.  
7. Fix a critical bug in the `divide` function in the `dev` branch:  
    ```python  
    def divide(self, a, b):  
         if b == 0:  
              raise ValueError("Cannot divide by zero.")  
         return a / b  
    ```  
8. Merge the `feature/sqrt` branch into `dev`, test, and release version 2.  

---

### Question 2: Git LFS Integration (Total: 10 Points)  
1. Create a branch `lfs`.  
2. Upload a large file (>200MB) and track it using Git LFS.  
3. Push the file to the repository.  
4. Clone the repository on another machine to verify the file is downloaded correctly.  

---

### Question 3: Geometry Calculator (Total: 20 Points)  
- **Task Completion**: 18 points  
- **Code Review**: 2 points  

#### Steps:  
1. Create a branch `feature/circle-area` and implement the circle area feature.  
2. Use `git stash` to save incomplete changes.  
3. Create a branch `feature/rectangle-area` and implement the rectangle area feature.  
4. Use `git stash` to save incomplete changes.  
5. Switch back to `feature/circle-area`, retrieve stashed changes, complete, and push.  
6. Switch to `feature/rectangle-area`, retrieve stashed changes, complete, and push.  
7. Create pull requests for both features targeting the `dev` branch.  
8. After review and approval, merge both features into the `main` branch.  
