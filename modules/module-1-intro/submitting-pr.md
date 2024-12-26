### **Guide: How to Submit Your Answers via a Pull Request**

### Step 1: Clone the Repository

1. Go to the repository on GitHub.
2. Click the green **Code** button and copy the HTTPS URL.
3. Clone the repository to your local machine using the terminal:
    
    ```bash
    git clone <repository-url>
    ```
    

### Step 2: Create a New Branch

1. Navigate to the repository folder:
    
    ```bash
    cd <repository-folder>
    ```
    
2. Create a new branch for your quiz answers:
    
    ```bash
    git checkout -b quiz-answers
    ```
    

### Step 3: Edit the Quiz File

1. Open the repository in a code editor (e.g., VS Code).
2. Navigate to the quiz file (e.g., `quizzes/linux-quiz.md`).
3. Mark your answers by replacing `[ ]` with `[x]`.

### Step 4: Commit Your Changes

1. Save the file and stage your changes:
    
    ```bash
    git add quizzes/linux-quiz.md
    ```
    
2. Commit your changes with a meaningful message:
    
    ```bash
    git commit -m "Submit answers for Linux Basics Quiz"
    
    ```
    

### Step 5: Push Your Branch to GitHub

1. Push your branch to GitHub:
    
    ```bash
    git push origin quiz-answers
    ```
    

### Step 6: Create a Pull Request

1. Go to the repository on GitHub.
2. You’ll see a banner offering to create a Pull Request for your new branch. Click **Compare & Pull Request**.
3. Fill in the Pull Request details:
    - **Title:** "[Quiz Submission] Linux Basics"
    - **Description:** Include any notes or questions about your submission.
4. Click **Create Pull Request**.