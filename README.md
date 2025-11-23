------------------------------------------
# Q1 — CalculatorPlus Application
------------------------------------------
# Goal

Create dev branch

Implement Calculator class

Add square root feature

Merge to main → Release v1.0

Add collaborator

Create branch feature/sqrt

Fix critical bug in divide()

Merge workflow

Final release v2.0

# Step 1 — Create dev Branch

git checkout -b dev

# Step 2 — Add Calculator Code

File: calculator.py

import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    # Square root feature
    def square_root(self, x):
        return math.sqrt(x)


if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

# Step 3 — Commit & Push

git add calculator.py
git commit -m "Added CalculatorPlus with square root feature"
git push --set-upstream origin dev

# Step 4 — Create Pull Request (dev → main)

On GitHub:

PR: dev → main

Title: "CalculatorPlus v1 — Initial Release"

Merge

# Step 5 — Create Release v1.0

GitHub → Releases:

Tag: v1.0

Title: CalculatorPlus v1

Includes add/sub/multiply/divide + square root

# Step 6 — Add Collaborator

GitHub → Repository → Settings → Collaborators → Add classmate

# Step 7 — Create Branch feature/sqrt

git checkout dev
git checkout -b feature/sqrt


Improve square_root:

def square_root(self, x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)


Commit & push:

git add calculator.py
git commit -m "Enhanced sqrt validation"
git push --set-upstream origin feature/sqrt

# Step 8 — Critical Bug Fix in divide()

Switch to dev:

git checkout dev


Fix divide:

def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


Commit & push:

git add calculator.py
git commit -m "Fixed divide by zero bug"
git push

# Step 9 — Update feature/sqrt Branch

git checkout feature/sqrt
git merge dev
git push

# Step 10 — PR feature/sqrt → dev

Open PR

Add collaborator for review

Fix comments

Merge

# Step 11 — Merge dev → main (Final)

Create PR

Merge

Testing completed

# Step 12 — Create Release v2.0

GitHub → Releases:

Tag: v2.0

Title: CalculatorPlus v2

Includes:

Bug fix (divide)

Improved sqrt validation

------------------------------------------
# Q2 — Git LFS (Large File Storage)
------------------------------------------
# Goal

Create lfs branch

Configure Git LFS

Upload >200MB binary file

Push to GitHub

Clone repo to verify LFS

# Step 1 — Create lfs Branch
git checkout -b lfs

# Step 2 — Install Git LFS
git lfs install

# Step 3 — Track Large Files

git lfs track "*.mp4"
git add .gitattributes
git commit -m "Configured Git LFS for mp4 files"

# Step 4 — Add Large File (>200MB)

git add sample_video.mp4
git commit -m "Added large video using Git LFS"
git push --set-upstream origin lfs


LFS Output Example:

Uploading LFS objects: 100% (1/1), 365 MB | 17 KB/s, done.

# Step 5 — Verify LFS

Clone repo in another folder:

git clone git url
cd repo folder
git checkout lfs


Check file size on powershell or VS code:

Get-ChildItem | Select Name, Length

------------------------------------------
# Q3 — Geometry Calculator (Git Stash Workflow)
------------------------------------------
# Goal

Use Git Stash

Work on two features

Use two feature branches

Commit both

Merge through PR

Merge into main

# Step 1 — Create Branch geometry-calculator

git checkout -b geometry-calculator


Create file:

geometry.py

import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()


Commit:

git add geometry.py
git commit -m "Added base geometry calculator"
git push --set-upstream origin geometry-calculator

# PART A — Circle Area (using stash)

# Step 2 — Create circle branch

git checkout -b feature/circle-area


Modify the file:

radius = 5
print(f"Circle area: {calculator.calculate_circle_area(radius)}")


Stash changes:

git stash
git status

# PART B — Rectangle Area (using stash)

# Step 3 — Create rectangle branch
git checkout -b feature/rectangle-area


Modify file:

length = 10
width = 6
print(f"Rectangle area: {calculator.calculate_rectangle_area(length, width)}")


Stash:

git stash
git status

# PART C — Finish Circle Feature

# Step 4 — Apply stash
git checkout feature/circle-area
git stash pop


Commit & push:

git add geometry.py
git commit -m "Completed circle area feature"
git push --set-upstream origin feature/circle-area


Open PR
→ base: dev
→ compare: feature/circle-area
→ Merge PR

# PART D — Finish Rectangle Feature

# Step 5 — Apply stash
git checkout feature/rectangle-area
git stash pop


Commit & push:

git add geometry.py
git commit -m "Completed rectangle area feature"
git push --set-upstream origin feature/rectangle-area


Open PR
→ base: dev
→ compare: feature/rectangle-area
→ Merge PR

# PART E — Final Merge
# Step 6 — Merge dev → main

Testing done → Create final PR:
dev → main → Merge.

# Screenshots (Add after completing work)

# Screenshot 1: Branch creation

<img width="884" height="44" alt="image" src="https://github.com/user-attachments/assets/10ac1d89-6d8d-4395-a9c4-94f8cba25fa2" />

# Screenshot 2: Stash operations
<img width="1083" height="485" alt="image" src="https://github.com/user-attachments/assets/1592cb73-bb7a-48e6-a4ef-f7ec1aef2264" />

<img width="1073" height="234" alt="image" src="https://github.com/user-attachments/assets/f21465f8-a375-4ac6-8f39-1301b254d520" />

# Screenshot 3: Pull Request page

<img width="571" height="425" alt="image" src="https://github.com/user-attachments/assets/e27e6ac2-8e22-4ecb-83ce-f48e04cd702c" />

# Screenshot 4: Git LFS upload logs

<img width="1251" height="681" alt="image" src="https://github.com/user-attachments/assets/29eab8c8-df1a-436a-932f-511749e984c2" />

# Screenshot 5: Release v1 and v2

<img width="1262" height="881" alt="image" src="https://github.com/user-attachments/assets/9deebfab-312d-4021-ad46-a0be7a742060" />
