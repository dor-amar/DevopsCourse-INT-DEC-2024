### **Lecture: Text Searching and Filtering in Linux (`grep`, `sed`, `awk`)**

---

### **1. Introduction**

Searching and filtering text in Linux is a critical skill for analyzing files, processing logs, and extracting relevant information. Tools like **`grep`**, **`sed`**, and **`awk`** are powerful utilities designed for different aspects of text processing.

---

### **2. Overview of Tools**

| **Tool** | **Purpose** |
| --- | --- |
| `grep` | Searches for patterns in text. |
| `sed` | Edits text streams. |
| `awk` | Processes and extracts structured data. |

---

### **3. `grep`: Searching for Patterns**

### **Purpose**

`grep` searches for text patterns in files or streams and displays matching lines.

### **Syntax**

```bash
grep [options] "pattern" filename

```

### **Examples**

1. Search for a word in a file:
    
    ```bash
    grep "Linux" example.txt
    
    ```
    
2. Search case-insensitively:
    
    ```bash
    grep -i "linux" example.txt
    
    ```
    
3. Display line numbers with matches:
    
    ```bash
    grep -n "Linux" example.txt
    
    ```
    
4. Search recursively in directories:
    
    ```bash
    grep -r "Linux" /path/to/dir
    
    ```
    
5. Use regular expressions:
    
    ```bash
    grep -E "error|warning" logs.txt
    
    ```
    

---

### **4. `sed`: Stream Editing**

### **Purpose**

`sed` processes text streams, making it ideal for substitutions, deletions, and text transformations.

### **Syntax**

```bash
sed [options] 'command' filename

```

### **Examples**

1. Replace text in a file:
    
    ```bash
    sed 's/Linux/Unix/' example.txt
    
    ```
    
    - Replaces the first occurrence of "Linux" with "Unix" in each line.
2. Replace globally in each line:
    
    ```bash
    sed 's/Linux/Unix/g' example.txt
    
    ```
    
3. Delete lines matching a pattern:
    
    ```bash
    sed '/Linux/d' example.txt
    
    ```
    
4. Insert a line before a pattern:
    
    ```bash
    sed '/pattern/i\This is a new line.' file.txt
    
    ```
    
5. Save changes to a file:
    
    ```bash
    sed -i 's/Linux/Unix/g' example.txt
    
    ```
    

---

### **5. `awk`: Advanced Text Processing**

### **Purpose**

`awk` processes structured text, extracting and transforming data based on patterns and fields.

### **Syntax**

```bash
awk 'pattern {action}' filename

```

### **Examples**

1. Print the second column of a file:
    
    ```bash
    awk '{print $2}' example.txt
    
    ```
    
2. Search for lines containing "Linux" and print the first field:
    
    ```bash
    awk '/Linux/ {print $1}' example.txt
    
    ```
    
3. Perform calculations:
    
    ```bash
    awk '{sum += $1} END {print sum}' numbers.txt
    
    ```
    
4. Specify a field delimiter:
    
    ```bash
    awk -F: '{print $1}' /etc/passwd
    
    ```
    
5. Use conditional statements:
    
    ```bash
    awk '$3 > 1000 {print $1, $3}' users.txt
    
    ```
    

---

### **6. Combining Tools**

These tools become more powerful when combined.

### Example Workflow:

1. Extract lines containing "error" from a log:
    
    ```bash
    grep "error" logs.txt
    
    ```
    
2. Replace "ERROR" with "ALERT":
    
    ```bash
    grep "error" logs.txt | sed 's/ERROR/ALERT/g'
    
    ```
    
3. Extract the timestamp field:
    
    ```bash
    grep "error" logs.txt | awk '{print $1}'
    
    ```
    

---

### **7. Practical Use Cases**

### **Log Analysis**

1. Find all error messages in logs:
    
    ```bash
    grep "error" /var/log/syslog
    
    ```
    
2. Count occurrences of "error":
    
    ```bash
    grep -c "error" /var/log/syslog
    
    ```
    

### **Configuration Management**

1. Replace a configuration value:
    
    ```bash
    sed -i 's/old_value/new_value/' config.conf
    
    ```
    
2. Extract usernames from `/etc/passwd`:
    
    ```bash
    awk -F: '{print $1}' /etc/passwd
    
    ```
    

### **Data Processing**

1. Extract specific columns from a CSV:
    
    ```bash
    awk -F, '{print $1, $3}' data.csv
    
    ```
    
2. Summarize numerical data:
    
    ```bash
    awk '{sum += $1} END {print "Total:", sum}' numbers.txt
    
    ```
    

---

### **8. Hands-On Practice**

### Task 1: Using `grep`

1. Search for the word "error" in `example.txt`.
2. Display line numbers with matches.

### Task 2: Using `sed`

1. Replace "Linux" with "Unix" in `example.txt`.
2. Delete all lines containing "error".

### Task 3: Using `awk`

1. Print the second column of `example.txt`.
2. Calculate the sum of the first column in `numbers.txt`.

### Task 4: Combine Tools

1. Search for "error" in a log file, replace it with "alert", and extract the timestamps.

---

### **9. Key Takeaways**

- **`grep`**: Ideal for searching patterns in text files.
- **`sed`**: Useful for in-line text transformations and edits.
- **`awk`**: Best for structured data processing and field-based actions.
- Combining these tools creates powerful and flexible workflows.