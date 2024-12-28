### **Comprehensive Hands-On Lab: `man` Pages, Command-Line Syntax, File Permissions, and ACL**

---

### **Lab Objectives**

By completing this lab, students will:

1. Learn to navigate and use the `man` pages effectively.
2. Practice command-line syntax with options and arguments.
3. Understand and modify file permissions using `chmod`, `chown`, and `chgrp`.
4. Implement Access Control Lists (ACL) for fine-grained permissions.

---

### **Part 1: Using the `man` Command**

### **Task 1: Explore the Manual Pages**

1. Use the `man` command to read the manual for the `ls` command:
    
    ```bash
    man ls
    
    ```
    
    - Find the option to display files in long listing format.
    - Find the option to include hidden files in the output.
2. Search for commands related to copying files:
    
    ```bash
    man -k copy
    
    ```
    
    - Identify the command used for secure copying.
3. Save the manual page for the `cp` command to a file:
    
    ```bash
    man cp > cp_manual.txt
    
    ```
    

---

### **Part 2: Practicing Command-Line Syntax**

### **Task 2: Execute Commands with Options and Arguments**

1. List all files in your home directory in long format:
    
    ```bash
    ls -l ~
    
    ```
    
2. Create a new directory structure:
    
    ```bash
    mkdir -p ~/lab/{scripts,logs}
    
    ```
    
3. Create three empty files in the `logs` directory:
    
    ```bash
    touch ~/lab/logs/{log1.log,log2.log,log3.log}
    
    ```
    
4. Copy all `.log` files to the `scripts` directory:
    
    ```bash
    cp ~/lab/logs/*.log ~/lab/scripts/
    
    ```
    
5. Redirect the output of `ls` to a file called `output.txt`:
    
    ```bash
    ls ~/lab > output.txt
    
    ```
    

---

### **Part 3: File Permissions**

### **Task 3: View and Modify Permissions**

1. Check the permissions of the `log1.log` file:
    
    ```bash
    ls -l ~/lab/logs/log1.log
    
    ```
    
2. Grant execute permission to the owner:
    
    ```bash
    chmod u+x ~/lab/logs/log1.log
    
    ```
    
3. Set permissions for the `log2.log` file to `rw-r--r--` using numeric mode:
    
    ```bash
    chmod 644 ~/lab/logs/log2.log
    
    ```
    
4. Change the owner of the `log3.log` file to `root`:
    
    ```bash
    sudo chown root ~/lab/logs/log3.log
    
    ```
    
5. Change the group of the `scripts` directory to `admin`:
    
    ```bash
    sudo chgrp admin ~/lab/scripts
    
    ```
    

---

### **Part 4: Access Control Lists (ACL)**

### **Task 4: Set and View ACL**

1. View the current ACL of the `log1.log` file:
    
    ```bash
    getfacl ~/lab/logs/log1.log
    
    ```
    
2. Add read and write permissions for the user `john` to `log1.log`:
    
    ```bash
    setfacl -m u:john:rw ~/lab/logs/log1.log
    
    ```
    
3. Add read-only permissions for the group `developers` to `log2.log`:
    
    ```bash
    setfacl -m g:developers:r ~/lab/logs/log2.log
    
    ```
    
4. Set a default ACL for the `scripts` directory to give the user `john` read and write permissions for all new files:
    
    ```bash
    setfacl -m d:u:john:rw ~/lab/scripts
    
    ```
    
5. Verify the ACL changes:
    
    ```bash
    getfacl ~/lab/scripts
    
    ```
    

---

### **Lab Questions**

### **Part 1: `man` Pages**

1. What option in `ls` displays hidden files?
2. How do you search for commands using the `man` command?

### **Part 2: Command-Line Syntax**

1. What does `ls -l` do?
2. Write the command to copy all `.log` files to another directory.

### **Part 3: File Permissions**

1. What command sets the permissions of a file to `rw-r--r--` using numeric mode?
2. What is the difference between `chmod` and `chown`?

### **Part 4: ACL**

1. How do you add read and write permissions for a specific user using `setfacl`?
2. What does a default ACL do?

---

### **Lab Summary**

- **`man` Pages**: Explored manual pages to understand command usage.
- **Command-Line Syntax**: Practiced commands with options and arguments.
- **File Permissions**: Modified file permissions using `chmod`, `chown`, and `chgrp`.
- **ACL**: Set fine-grained access controls for users and groups.