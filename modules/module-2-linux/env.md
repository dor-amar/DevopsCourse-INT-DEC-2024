### **Lecture: Environment Variables in Linux**

---

### **1. Introduction**

Environment variables are dynamic values stored within the operating system, used by applications and processes to communicate configuration details. They play a critical role in Linux for defining system behavior and application settings.

---

### **2. What Are Environment Variables?**

- **Definition**:
    - Key-value pairs used to store configuration details.
    - Example: `HOME=/home/username`, `PATH=/usr/local/bin:/usr/bin:/bin`.
- **Purpose**:
    - Provide a consistent way to share configuration data across processes.
    - Avoid hardcoding values directly into applications or scripts.
- **Common Environment Variables**:
    
    
    | **Variable** | **Description** |
    | --- | --- |
    | `HOME` | User's home directory |
    | `PATH` | Directories searched for executable commands |
    | `USER` | Current logged-in user |
    | `SHELL` | Default shell for the user |
    | `LANG` | System language and locale settings |

---

### **3. Viewing Environment Variables**

### **`env` Command**:

- Lists all environment variables.
    
    ```bash
    env
    
    ```
    

### **`printenv` Command**:

- Prints the value of a specific variable or all variables.
    
    ```bash
    printenv PATH
    
    ```
    

### **Accessing a Variable Directly**:

- Use `echo` to display the value:
    
    ```bash
    echo $HOME
    
    ```
    

---

### **4. Setting Environment Variables**

### **Temporarily Setting a Variable**

- Valid only for the current session or script.
    
    ```bash
    export MY_VAR="Hello, World!"
    echo $MY_VAR
    
    ```
    

### **Persistently Setting a Variable**

- Add the variable to a configuration file:
    - **For a single user**: Add to `~/.bashrc` or `~/.bash_profile`.
    - **System-wide**: Add to `/etc/environment` or `/etc/profile`.
    
    Example:
    
    ```bash
    echo 'export MY_VAR="Hello, Persistent World!"' >> ~/.bashrc
    source ~/.bashrc
    
    ```
    

### **Unsetting a Variable**

- Remove a variable from the environment.
    
    ```bash
    unset MY_VAR
    
    ```
    

---

### **5. Environment vs Shell Variables**

| **Environment Variables** | **Shell Variables** |
| --- | --- |
| Available to the current process and all child processes. | Limited to the current shell session. |
| Declared with `export`. | Declared without `export`. |
| Example: `export VAR="value"`. | Example: `VAR="value"`. |

---

### **6. Using Environment Variables in Scripts**

### **Example 1: Accessing an Environment Variable**

```bash
#!/bin/bash
echo "The home directory is $HOME"

```

### **Example 2: Passing Variables to Child Processes**

```bash
#!/bin/bash
export GREETING="Hello"
bash -c 'echo $GREETING'

```

### **Example 3: Using Variables for Configuration**

```bash
#!/bin/bash
LOG_FILE="/var/log/myapp.log"
echo "Logging to $LOG_FILE"

```

---

### **7. Best Practices**

1. **Use Meaningful Names**:
    - Use uppercase letters for variable names (e.g., `DB_HOST`, `APP_PORT`).
2. **Avoid Hardcoding**:
    - Use environment variables to make scripts and applications portable.
3. **Secure Sensitive Data**:
    - Avoid storing passwords or sensitive data directly in scripts.
    - Use secure methods like `.env` files or configuration management tools.
4. **Check Variable Existence**:
    - Verify if a variable is set before using it:
        
        ```bash
        if [ -z "$MY_VAR" ]; then
            echo "MY_VAR is not set"
        fi
        
        ```
        

---

### **8. Hands-On Practice**

### **Task 1: Viewing Variables**

1. Use the `env` and `printenv` commands to list and check variables like `HOME` and `PATH`.

### **Task 2: Setting and Accessing Variables**

1. Temporarily set a variable and access its value.
2. Persistently set a variable by adding it to `~/.bashrc`.

### **Task 3: Using Variables in Scripts**

1. Write a script that uses `HOME` and `USER` to display a message:
    - "Welcome, [USER]! Your home directory is [HOME]."

### **Task 4: Passing Variables**

1. Export a variable in a script and pass it to a child process.

---

### **9. Key Takeaways**

- Environment variables are essential for configuration management in Linux.
- Use commands like `env`, `printenv`, and `export` to view and manipulate them.
- Incorporate environment variables into scripts for dynamic and portable behavior.