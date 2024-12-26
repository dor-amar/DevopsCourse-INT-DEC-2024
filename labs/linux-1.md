### **🧑‍💻 Lab: Directories, Basic Commands, and the "Everything is a File" Concept** 

This lab is designed to help students practice working with Linux directories, basic file commands, and understand how Linux treats "everything as a file." Follow the steps carefully, and answer the questions at the end.

### **Lab Objectives**

1. Create and navigate directories.
2. Practice basic Linux commands.
3. Explore and interact with special files.
4. Understand the "everything is a file" concept.

---

### **Lab Instructions**

### **Step 1: Creating and Navigating Directories**

1. Create a directory named `linux_lab` in your home directory.
    
    ```bash
    mkdir ~/linux_lab
    ```
    
2. Inside `linux_lab`, create two subdirectories: `projects` and `logs`.
    
    ```bash
    mkdir ~/linux_lab/projects ~/linux_lab/logs
    ```
    
3. Navigate into the `projects` directory.
    
    ```bash
    cd ~/linux_lab/projects
    ```
    
4. Create a new directory structure for a web project:
    
    ```bash
    mkdir -p web_app/{frontend,backend}
    ```
    
5. Verify your directory structure using:
    
    ```bash
    tree ~/linux_lab
    ```
    

### **Step 2: Basic File Commands**

1. Create a new empty file called `notes.txt` in the `web_app/frontend` directory.
    
    ```bash
    touch ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
2. Write "Hello, Linux World!" into the `notes.txt` file.
    
    ```bash
    echo "Hello, Linux World!" > ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
3. Display the contents of the file.
    
    ```bash
    cat ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
4. Copy the `notes.txt` file to the `backend` directory.
    
    ```bash
    cp ~/linux_lab/projects/web_app/frontend/notes.txt ~/linux_lab/projects/web_app/backend/
    ```
    
5. Rename the copied file in the `backend` directory to `backend_notes.txt`.
    
    ```bash
    mv ~/linux_lab/projects/web_app/backend/notes.txt ~/linux_lab/projects/web_app/backend/backend_notes.txt
    ```
    
6. Delete the `backend_notes.txt` file.
    
    ```bash
    rm ~/linux_lab/projects/web_app/backend/backend_notes.txt
    ```
    

### **Step 3: Understanding "Everything is a File"**

1. View CPU information using the `/proc` file system.
    
    ```bash
    cat /proc/cpuinfo
    ```
    
2. Check memory details.
    
    ```bash
    cat /proc/meminfo
    ```
    
3. Interact with a device file:
Write text directly to the terminal device.
    
    ```bash
    echo "Hello from /dev/tty" > /dev/tty
    ```
    
4. Create and use a named pipe:
    - Create a named pipe:
        
        ```bash
        mkfifo ~/linux_lab/my_pipe
        ```
        
    - In one terminal, read from the pipe:
        
        ```bash
        cat ~/linux_lab/my_pipe
        ```
        
    - In another terminal, write to the pipe:
        
        ```bash
        echo "Data through the pipe!" > ~/linux_lab/my_pipe
        
        ```
        

### **Step 4: Questions**

Answer the following questions based on your lab work:

1. What command did you use to create a new directory?
2. How do you display the contents of a file?
3. What is the purpose of the `/proc` directory?
4. How does Linux represent hardware devices in the file system?
5. What happens when you write to a named pipe?

---

### **Answers with Explanations**

### **Step 1: Directory Commands**

1. **Command to create a directory**:
    
    ```bash
    mkdir ~/linux_lab
    ```
    
    **Explanation**: The `mkdir` command creates a directory at the specified path.
    
2. **Verify directory structure**:
    
    ```bash
    tree ~/linux_lab
    ```
    
    **Explanation**: The `tree` command shows the hierarchy of directories and files.
    

---

### **Step 2: File Commands**

1. **Creating an empty file**:
    
    ```bash
    touch ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
    **Explanation**: The `touch` command creates an empty file if it doesn’t already exist.
    
2. **Writing to a file**:
    
    ```bash
    echo "Hello, Linux World!" > ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
    **Explanation**: The `echo` command outputs text. The `>` operator writes the output to the file, overwriting its contents.
    
3. **Displaying file contents**:
    
    ```bash
    cat ~/linux_lab/projects/web_app/frontend/notes.txt
    ```
    
    **Explanation**: The `cat` command reads and displays the contents of a file.
    
4. **Copying a file**:
    
    ```bash
    cp ~/linux_lab/projects/web_app/frontend/notes.txt ~/linux_lab/projects/web_app/backend/
    
    ```
    
    **Explanation**: The `cp` command copies a file from one location to another.
    
5. **Renaming a file**:
    
    ```bash
    mv ~/linux_lab/projects/web_app/backend/notes.txt ~/linux_lab/projects/web_app/backend/backend_notes.txt
    
    ```
    
    **Explanation**: The `mv` command moves or renames a file.
    
6. **Deleting a file**:
    
    ```bash
    rm ~/linux_lab/projects/web_app/backend/backend_notes.txt
    ```
    
    **Explanation**: The `rm` command removes (deletes) a file.
    

---

### **Step 3: Everything is a File**

1. **Viewing CPU information**:
    
    ```bash
    cat /proc/cpuinfo
    
    ```
    
    **Explanation**: The `/proc/cpuinfo` file provides details about the CPU, like model and speed.
    
2. **Checking memory details**:
    
    ```bash
    cat /proc/meminfo
    
    ```
    
    **Explanation**: The `/proc/meminfo` file shows system memory usage.
    
3. **Writing to a terminal device**:
    
    ```bash
    echo "Hello from /dev/tty" > /dev/tty
    
    ```
    
    **Explanation**: The `/dev/tty` file represents the terminal device. Writing to it displays the text on your terminal.
    
4. **Using a named pipe**:
    - Create a pipe:
        
        ```bash
        mkfifo ~/linux_lab/my_pipe
        
        ```
        
    - **Explanation**: A named pipe is a special file used for inter-process communication.
    - In one terminal, you can read from the pipe using:
        
        ```bash
        cat ~/linux_lab/my_pipe
        
        ```
        
    - In another terminal, writing to the pipe sends data to the reader:
        
        ```bash
        echo "Data through the pipe!" > ~/linux_lab/my_pipe
        
        ```