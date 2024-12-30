### Hands-On Lab: File Redirections, stdout, stdin, and stderr in Linux

**Duration:** 20-25 minutes

**Objective:** Help students understand and practice file redirections and standard streams (`stdout`, `stdin`, `stderr`) in Linux.

---

### **Lab Setup**

1. Students need access to a Linux terminal (local machine, VirtualBox, WSL, or cloud instance).
2. Create a working directory for this lab:
    
    ```bash
    mkdir file_redirection_lab
    cd file_redirection_lab
    ```
    

---

### **Lab Outline**

---

### **Part 1: File Redirections** (10 minutes)

1. **Tasks:**
    - **Redirect output to a file:**Use the `echo` command to create a file named `output.txt` and write a message to it:
        
        ```bash
        echo "This is a test message." > output.txt
        
        ```
        
    - **Verify the content of the file:**Display the contents of the file using `cat`:
        
        ```bash
        cat output.txt
        
        ```
        
    - **Append content to the file:**Add another line to the file using `>>`:
        
        ```bash
        echo "This is an appended line." >> output.txt
        
        ```
        
    - **Overwrite the file:**Replace the contents of the file with a single line using `>`:
        
        ```bash
        echo "This overwrites the content." > output.txt
        
        ```
        
    - **Combine outputs into a single file:**Use redirection to save the output of multiple commands into one file:
        
        ```bash
        echo "First command output" > combined_output.txt
        echo "Second command output" >> combined_output.txt
        
        ```
        
    - Display the content of the combined file:
        
        ```bash
        cat combined_output.txt
        
        ```
        
2. **Questions for Students:**
    - What is the difference between `>` and `>>`?
    - What happens when you use `>` with an existing file?

---

### **Part 2: stdout, stdin, and stderr** (15 minutes)

1. **Working with stdout (Standard Output):**
    - Run a simple command (`ls`) and observe its output:
        
        ```bash
        ls
        
        ```
        
    - Redirect the output to a file named `stdout_example.txt`:
        
        ```bash
        ls > stdout_example.txt
        
        ```
        
    - Verify the content of the file:
        
        ```bash
        cat stdout_example.txt
        
        ```
        
2. **Working with stderr (Standard Error):**
    - Generate an error by listing a non-existent file:
        
        ```bash
        ls nonexistent_file
        
        ```
        
    - Redirect the error message to a file named `error_log.txt`:
        
        ```bash
        ls nonexistent_file 2> error_log.txt
        
        ```
        
    - Display the content of `error_log.txt`:
        
        ```bash
        cat error_log.txt
        
        ```
        
3. **Combine stdout and stderr:**
    - Redirect both stdout and stderr into a single file:
        
        ```bash
        ls nonexistent_file existing_file 1> combined_output.txt 2>&1
        
        ```
        
    - Verify the combined output:
        
        ```bash
        cat combined_output.txt
        
        ```
        
4. **Working with stdin (Standard Input):**
    - Create a file interactively using the `cat` command:Type a few lines of text and press `CTRL + D` to save.
        
        ```bash
        cat > stdin_example.txt
        
        ```
        
    - Display the content of the file:
        
        ```bash
        cat stdin_example.txt
        
        ```
        
5. **Piping Data (Basic Example):**
    - Use a pipeline to pass the output of one command (`cat`) as input to another command (`grep`):
        
        ```bash
        cat stdin_example.txt | grep "text"
        
        ```
        
    - Explain how the pipe (`|`) works to pass data between commands.

---

### **Part 3: Working with Temporary Files** (10 minutes)

1. **Creating and Managing Temporary Files:**
    - Create a new file named `temp_file.txt` and add a message to it:
        
        ```bash
        echo "Temporary file content" > temp_file.txt
        
        ```
        
    - Verify the file content:
        
        ```bash
        cat temp_file.txt
        
        ```
        
    - Move the file to a new name:
        
        ```bash
        mv temp_file.txt renamed_temp_file.txt
        
        ```
        
    - Confirm the file was renamed:
        
        ```bash
        ls
        cat renamed_temp_file.txt
        
        ```
        
2. **Removing Files:**
    - Delete the file:
        
        ```bash
        rm renamed_temp_file.txt
        
        ```
        
    - Verify that the file has been deleted:
        
        ```bash
        ls
        
        ```
        
3. **Interactive Deletion:**
    - Create a file and attempt to delete it interactively:
        
        ```bash
        touch interactive_delete.txt
        rm -i interactive_delete.txt
        
        ```
        
    - Respond to the interactive prompt.

---

### **Wrap-Up Questions**

1. What are the differences between `stdout`, `stdin`, and `stderr`?
2. How would you redirect an error message to a file while keeping standard output displayed in the terminal?
3. How does `>>` differ from `>` when redirecting output to a file?