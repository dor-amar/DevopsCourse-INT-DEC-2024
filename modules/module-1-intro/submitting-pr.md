## **Guide: How to Answer a Quiz and Submit it on GitHub**

### **Step 1: Navigate to the Repository**

1. Open the repository link shared by your instructor.
2. Find the quiz file (e.g., `quizzes/linux-quiz-1.md`) in the repository.

---

### **Step 2: Create a Branch**

1. Open a terminal or Git Bash on your computer.
2. Clone the repository to your local machine by copying the repository's HTTPS URL:
    
    ```bash
    git clone <repository-url>
    
    ```
    
    Replace `<repository-url>` with the repository link (e.g., `https://github.com/your-repo-name.git`).
    
3. Navigate to the repository directory:
    
    ```bash
    cd <repository-folder>
    
    ```
    
4. Create a new branch to work on your quiz answers:
    
    ```bash
    git checkout -b <branch-name>
    
    ```
    
    Replace `<branch-name>` with a descriptive name, such as `quiz-answers`.
    
    **Screenshot Example:**
    

---

### **Step 3: Edit the Quiz File**

1. Open the repository folder in a code editor (e.g., VS Code).
2. Navigate to the quiz file (e.g., `quizzes/linux-quiz-1.md`).
3. Replace `[ ]` with `[x]` to mark your answers.
    
    **Example:**
    
    ```markdown
    markdown
    - [x] a) `mkdir`
    - [ ] b) `cd`
    
    ```
    
    **Screenshot Example:**
    

---

### **Step 4: Commit Your Changes**

1. Save the file.
2. Stage your changes:
    
    ```bash
    git add quizzes/linux-quiz-1.md
    
    ```
    
3. Commit the changes with a meaningful message:
    
    ```bash
    git commit -m "Completed Linux Quiz 1"
    
    ```
    
    **Screenshot Example:**
    

---

### **Step 5: Push Your Branch**

1. Push your branch to GitHub:
    
    ```bash
    git push --set-upstream origin <branch-name>
    
    ```
    
    Replace `<branch-name>` with the name of the branch you created earlier.
    
    **Screenshot Example:**
    

---

### **Step 6: Create a Pull Request**

1. Go to the repository on GitHub.
2. You’ll see a banner at the top offering to create a Pull Request for your branch. Click **"Compare & pull request"**.
    
    **Screenshot Example:**
    
3. Fill in the Pull Request details:
    - **Title:** "[Quiz Submission] Linux Quiz 1"
    - **Description:** Include any notes or questions for the instructor.
4. Click **"Create pull request"**.

---

### **Step 7: Wait for Feedback**

Once your Pull Request is submitted, your instructor will review it and provide feedback directly on GitHub. If changes are requested, update your quiz file locally, commit the changes, and push them to the same branch.