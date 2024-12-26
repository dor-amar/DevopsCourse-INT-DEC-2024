# **Hands-On Lab: Links and Wildcards**

This lab combines the concepts of **soft and hard links** and **wildcards** to give students hands-on practice. Follow the steps and answer the questions provided.

---

### **Lab Objectives**

1. Understand how to create and use **hard links** and **soft links**.
2. Practice using **wildcards** to manage multiple files and directories efficiently.

---

### **Lab Instructions**

---

### **Part 1: Links**

### **Step 1: Create a File and a Hard Link**

1. Create a file called `hardlink_example.txt` and write some text into it:
    
    ```bash
    echo "This is a hard link example." > hardlink_example.txt
    ```
    
2. Create a hard link named `hardlink_copy.txt` pointing to `hardlink_example.txt`:
    
    ```bash
    ln hardlink_example.txt hardlink_copy.txt
    
    ```
    
3. Verify that both files share the same inode:
    
    ```bash
    ls -li
    
    ```
    
4. Add more text to `hardlink_example.txt`:
    
    ```bash
    echo "Hard links share the same data." >> hardlink_example.txt
    
    ```
    
5. Check the contents of `hardlink_copy.txt`:
    
    ```bash
    cat hardlink_copy.txt
    
    ```
    

---

### **Step 2: Create a Soft Link**

1. Create a soft link named `softlink_example.txt` pointing to `hardlink_example.txt`:
    
    ```bash
    ln -s hardlink_example.txt softlink_example.txt
    
    ```
    
2. List the files to see the symbolic link:
    
    ```bash
    ls -l
    
    ```
    
3. Delete the original file:
    
    ```bash
    rm hardlink_example.txt
    
    ```
    
4. Try to read the contents of `softlink_example.txt`:
    
    ```bash
    cat softlink_example.txt
    
    ```
    

---

### **Step 3: Questions**

1. What happens to the hard link (`hardlink_copy.txt`) after the original file is deleted?
2. Why does the soft link (`softlink_example.txt`) break after the original file is deleted?

---

### **Part 2: Wildcards**

### **Step 1: Prepare the Lab Environment**

1. Create a directory called `wildcard_lab`:
    
    ```bash
    mkdir wildcard_lab
    
    ```
    
2. Navigate into the directory:
    
    ```bash
    cd wildcard_lab
    
    ```
    
3. Create the following files:
    
    ```bash
    touch file1.txt file2.txt file3.log fileA.log fileB.txt fileC.tmp
    
    ```
    

---

### **Step 2: Use Wildcards**

1. List all `.txt` files:
    
    ```bash
    ls *.txt
    
    ```
    
2. List all files that start with `file` and end with `.log`:
    
    ```bash
    ls file*.log
    
    ```
    
3. List all files that have exactly one character after `file` and end with `.txt`:
    
    ```bash
    ls file?.txt
    
    ```
    
4. List files ending with `A` or `B`:
    
    ```bash
    ls file[A-B].*
    
    ```
    
5. Copy all `.log` files to a new directory named `logs`:
    
    ```bash
    mkdir logs
    cp *.log logs/
    
    ```
    
6. Delete all `.tmp` files:
    
    ```bash
    rm *.tmp
    
    ```
    

---

### **Step 3: Questions**

1. What command lists all files starting with `file` and ending with any extension?
2. How can you list all `.txt` files that have exactly one character after the word `file`?
3. What happens when you use `ls file[A-Z]*`?

---

### **Lab Summary**

1. **Links**:
    - Hard links share the same data, even after the original file is deleted.
    - Soft links break if the original file is removed.
2. **Wildcards**:
    - Use  to match zero or more characters.
    - Use `?` to match exactly one character.
    - Use `[]` to specify ranges or sets of characters.

---

### **Lab Answers**

---

### **Part 1: Links**

1. **What happens to the hard link (`hardlink_copy.txt`) after the original file is deleted?**
    - The hard link still works because it shares the same inode and data as the original file.
2. **Why does the soft link (`softlink_example.txt`) break after the original file is deleted?**
    - The soft link points to the original file’s path. When the file is deleted, the path becomes invalid.

---

### **Part 2: Wildcards**

1. **What command lists all files starting with `file` and ending with any extension?**
    - `ls file*`
2. **How can you list all `.txt` files that have exactly one character after the word `file`?**
    - `ls file?.txt`
3. **What happens when you use `ls file[A-Z]*`?**
    - It lists all files starting with `file` followed by an uppercase letter (A to Z).