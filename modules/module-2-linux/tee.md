### **The `tee` Command in Linux**

---

### **1. Introduction**

The **`tee` command** in Linux is used to read input from **standard input (stdin)** and write it to both **standard output (stdout)** and one or more files simultaneously. It is a versatile tool for logging, debugging, and capturing command outputs without interrupting the workflow.

---

### **2. Syntax**

```bash
command | tee [options] filename
```

- **`command`**: The command whose output you want to process.
- **`|`**: The pipe operator to redirect the output.
- **`tee`**: The command that splits the output to both the terminal and the file.
- **`filename`**: The file to which the output is written.

---

### **3. Key Features of `tee`**

### **a) Write to a File**

- Overwrites the file if it already exists.
- Example:
    
    ```bash
    echo "Hello, World!" | tee output.txt
    ```
    
    - Writes `Hello, World!` to `output.txt` and displays it on the terminal.

### **b) Append to a File**

- Use the `a` option to append to a file instead of overwriting it.
- Example:
    
    ```bash
    echo "Appending text" | tee -a output.txt
    ```
    

### **c) Write to Multiple Files**

- Write the same output to multiple files.
- Example:
    
    ```bash
    echo "Writing to multiple files" | tee file1.txt file2.txt
    ```
    

---

### **4. Practical Use Cases**

### **a) Logging Command Output**

Capture the output of a command to a log file while still displaying it on the terminal.

- Example: Log the output of `ls` to a file:
    
    ```bash
    ls | tee log.txt
    ```
    

### **b) Real-Time Monitoring**

Capture and save output while observing it in real time.

- Example: Monitor system logs and save them:
    
    ```bash
    tail -f /var/log/syslog | tee live_logs.txt
    ```
    

### **c) Debugging and Verification**

Verify the output of a script or command while saving it for later analysis.

- Example: Debug a script and save its output:
    
    ```bash
    ./script.sh | tee debug.log
    ```
    

---

### **5. Combining `tee` with Other Commands**

### **Example 1: Combine with `grep`**

Filter specific lines and save them:

```bash
grep "error" /var/log/syslog | tee errors.log
```

### **Example 2: Chain with `wc`**

Count lines in a file and save the result:

```bash
wc -l file.txt | tee line_count.txt
```

### **Example 3: Run Commands with Elevated Privileges**

Redirect output to files requiring root permissions:

```bash
echo "Configuration Updated" | sudo tee /etc/config.txt
```

---

### **6. Advanced Options**

| Option | Description |
| --- | --- |
| `-a` | Append to the file instead of overwriting. |
| `-i` | Ignore interrupt signals. |

### **Example with `i`:**

```bash
command | tee -i output.txt
```

This prevents the process from being interrupted by signals like `Ctrl+C`.

---

### **7. Hands-On Practice**

### Task 1: Basic Usage

1. Write "Hello, Linux!" to a file and display it on the terminal:
    
    ```bash
    echo "Hello, Linux!" | tee hello.txt
    ```
    
2. View the contents of `hello.txt`:
    
    ```bash
    cat hello.txt
    ```
    

---

### Task 2: Appending Output

1. Append the current date to `hello.txt`:
    
    ```bash
    date | tee -a hello.txt
    ```
    
2. Verify the file content:
    
    ```bash
    cat hello.txt
    ```
    

---

### Task 3: Real-Time Monitoring

1. Monitor system logs and save them to `system_logs.txt`:
    
    ```bash
    tail -f /var/log/syslog | tee system_logs.txt
    ```
    
2. Open another terminal and trigger a system event (e.g., plug in a USB device).

---

### Task 4: Write to Multiple Files

1. Write "Learning `tee`" to two files:
    
    ```bash
    echo "Learning tee command" | tee file1.txt file2.txt
    ```
    
2. Verify the contents:
    
    ```bash
    cat file1.txt
    cat file2.txt
    ```
    

---

### **8. Key Takeaways**

- The `tee` command splits output to the terminal and files, making it ideal for logging and debugging.
- Use `a` to append data to files.
- Combine `tee` with commands like `grep`, `wc`, and `sudo` for powerful workflows.