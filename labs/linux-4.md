### **Lab: Exploring Text Editors, Reading Files, Adding Text, Pipelines, and the `tee` Command**

---

### **Lab Objectives**

By completing this lab, students will:

1. Practice using Linux text editors for file creation and modification.
2. Learn to read and analyze file content with different commands.
3. Understand how to append text to files using various techniques.
4. Work with pipelines to chain commands and process data.
5. Use the `tee` command for logging and real-time output.

---

### **Instructions**

### **Part 1: Working with Text Editors**

1. Create a file named `lab_notes.txt` using Nano and write the following text:
    
    ```vbnet
    Welcome to the Linux Lab!
    This is an example of using a text editor.
    
    ```
    
    Save the file and exit the editor.
    
2. Open the same file in Vim, add the line:
    
    ```arduino
    Adding another line using Vim.
    ```
    
    Save and quit the editor.
    
3. Verify the contents of the file.

---

### **Part 2: Reading from Files**

1. Display the entire content of `lab_notes.txt`.
2. View the file interactively, scrolling through the content.
3. Display only the first two lines of the file.
4. Display the last line of the file.

---

### **Part 3: Adding Text to a File**

1. Append the line:
    
    ```arduino
    Appended line using echo.
    ```
    
    to `lab_notes.txt`.
    
2. Add the line:
    
    ```vbnet
    Adding text interactively with cat.
    ```
    
    to `lab_notes.txt` interactively.
    
3. Verify the updated contents of the file.

---

### **Part 4: Using Pipelines**

1. Count the number of lines in `lab_notes.txt`.
2. Search for the word "line" in the file.
3. Display lines containing "line" in sorted order.
4. Extract and display only the 2nd and 3rd lines of the file.

---

### **Part 5: Working with `tee`**

1. Write the output of the `ls` command to a file named `output.txt` while also displaying it on the terminal.
2. Append the current date and time to `output.txt`.
3. Monitor changes to `output.txt` in real time.

---

### **Commands Reference**

### **Part 1: Text Editors**

1. Open a file in Nano:
    
    ```bash
    nano lab_notes.txt
    ```
    
    Save: `CTRL+O`, Exit: `CTRL+X`.
    
2. Open a file in Vim:
    
    ```bash
    vim lab_notes.txt
    
    ```
    
    Add text in Insert Mode: `i`, Save and Quit: `:wq`.
    
3. Display file contents:
    
    ```bash
    cat lab_notes.txt
    ```
    

---

### **Part 2: Reading Files**

1. Display the file:
    
    ```bash
    cat lab_notes.txt
    ```
    
2. View interactively:
    
    ```bash
    less lab_notes.txt
    ```
    
    Scroll: `Spacebar`, Quit: `q`.
    
3. Display the first two lines:
    
    ```bash
    head -n 2 lab_notes.txt
    ```
    
4. Display the last line:
    
    ```bash
    tail -n 1 lab_notes.txt
    ```
    

---

### **Part 3: Adding Text**

1. Append text with `echo`:
    
    ```bash
    echo "Appended line using echo." >> lab_notes.txt
    ```
    
2. Add text interactively:
    
    ```bash
    cat >> lab_notes.txt
    ```
    
    Type the line and press `CTRL+D` to save.
    
3. Verify the file:
    
    ```bash
    cat lab_notes.txt
    
    ```
    

---

### **Part 4: Using Pipelines**

1. Count lines:
    
    ```bash
    
    cat lab_notes.txt | wc -l
    
    ```
    
2. Search for a word:
    
    ```bash
    
    cat lab_notes.txt | grep "line
    
    ```
    
3. Sort and display lines:
    
    ```bash
    cat lab_notes.txt | grep "line" | sort
    
    ```
    
4. Extract specific lines:
    
    ```bash
    head -n 3 lab_notes.txt | tail -n 2
    ```
    

---

### **Part 5: Working with `tee`**

1. Write output to a file:
    
    ```bash
    ls | tee output.txt
    ```
    
2. Append to a file:
    
    ```bash
    date | tee -a output.txt
    ```
    
3. Monitor file changes:
    
    ```bash
    tail -f output.txt
    ```