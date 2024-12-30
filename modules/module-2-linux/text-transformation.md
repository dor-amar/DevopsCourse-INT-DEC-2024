### **Lecture: Text Transformation in Linux (`cut`, `tr`, `sort`, `uniq`)**

---

### **1. Introduction**

Text transformation involves modifying and organizing text to extract, rearrange, or clean up data. Linux provides efficient tools like **`cut`**, **`tr`**, **`sort`**, and **`uniq`** to handle these tasks effectively.

---

### **2. Overview of Tools**

| **Tool** | **Purpose** |
| --- | --- |
| `cut` | Extract specific fields or columns. |
| `tr` | Translate or delete characters. |
| `sort` | Sort lines alphabetically or numerically. |
| `uniq` | Remove or count duplicate lines. |

---

### **3. `cut`: Extract Specific Fields**

### **Purpose**

`cut` extracts specific portions of each line, such as columns or fields.

### **Syntax**

```bash
cut [options] filename

```

### **Examples**

1. Extract the first 10 characters of each line:
    
    ```bash
    cut -c 1-10 file.txt
    
    ```
    
2. Extract the second field from a colon-delimited file:
    
    ```bash
    cut -d ':' -f 2 /etc/passwd
    
    ```
    
3. Extract multiple fields (e.g., 1st and 3rd):
    
    ```bash
    cut -d ',' -f 1,3 data.csv
    
    ```
    

---

### **4. `tr`: Translate or Delete Characters**

### **Purpose**

`tr` transforms or removes characters from text streams.

### **Syntax**

```bash
tr [options] SET1 [SET2]

```

### **Examples**

1. Convert lowercase to uppercase:
    
    ```bash
    echo "hello world" | tr 'a-z' 'A-Z'
    
    ```
    
2. Remove all digits:
    
    ```bash
    echo "abc123" | tr -d '0-9'
    
    ```
    
3. Replace spaces with underscores:
    
    ```bash
    echo "hello world" | tr ' ' '_'
    
    ```
    

---

### **5. `sort`: Organize Lines**

### **Purpose**

`sort` arranges lines in files alphabetically, numerically, or by fields.

### **Syntax**

```bash
sort [options] filename

```

### **Examples**

1. Sort a file alphabetically:
    
    ```bash
    sort file.txt
    
    ```
    
2. Sort a file in reverse order:
    
    ```bash
    sort -r file.txt
    
    ```
    
3. Sort numerically:
    
    ```bash
    sort -n numbers.txt
    
    ```
    
4. Sort by the second field in a CSV:
    
    ```bash
    sort -t ',' -k 2 data.csv
    
    ```
    

---

### **6. `uniq`: Remove Duplicate Lines**

### **Purpose**

`uniq` eliminates duplicate lines in a sorted file.

### **Syntax**

```bash
uniq [options] filename

```

### **Examples**

1. Remove duplicate lines:
    
    ```bash
    uniq file.txt
    
    ```
    
2. Display duplicate lines with counts:
    
    ```bash
    uniq -c file.txt
    
    ```
    
3. Ignore case when identifying duplicates:
    
    ```bash
    uniq -i file.txt
    
    ```
    

---

### **7. Combining Tools**

These tools can be combined to create powerful text processing workflows.

### **Example Workflow**

1. Extract usernames from `/etc/passwd`, sort them, and remove duplicates:
    
    ```bash
    cut -d ':' -f 1 /etc/passwd | sort | uniq
    
    ```
    
2. Count occurrences of each username:
    
    ```bash
    cut -d ':' -f 1 /etc/passwd | sort | uniq -c
    
    ```
    
3. Clean up a CSV file by sorting it and removing duplicates:
    
    ```bash
    sort data.csv | uniq > cleaned_data.csv
    
    ```
    

---

### **8. Practical Use Cases**

### **Log Analysis**

1. Extract and count unique IP addresses from logs:
    
    ```bash
    grep "IP" logs.txt | cut -d ' ' -f 3 | sort | uniq -c
    
    ```
    

### **Data Cleaning**

1. Remove duplicate entries in a file:
    
    ```bash
    sort data.txt | uniq > cleaned.txt
    
    ```
    
2. Standardize case in a file:
    
    ```bash
    tr 'A-Z' 'a-z' < file.txt > lowercase.txt
    
    ```
    

### **Report Generation**

1. Sort numerical data for better visualization:
    
    ```bash
    sort -n sales.txt
    
    ```
    
2. Extract specific columns from a CSV file:
    
    ```bash
    cut -d ',' -f 2,5 data.csv
    
    ```
    

---

### **9. Hands-On Practice**

### Task 1: Using `cut`

1. Extract the first field from `/etc/passwd`.
2. Extract the first and third columns from `data.csv`.

### Task 2: Using `tr`

1. Convert the text in `example.txt` to uppercase.
2. Replace all commas with semicolons in `data.csv`.

### Task 3: Using `sort`

1. Sort the contents of `file.txt` alphabetically.
2. Sort `numbers.txt` numerically and save the output to `sorted_numbers.txt`.

### Task 4: Using `uniq`

1. Remove duplicates from `sorted_file.txt`.
2. Count the number of duplicate lines in `data.txt`.

### Task 5: Combine Tools

1. Extract, sort, and count unique words from a text file:
    
    ```bash
    tr ' ' '\n' < file.txt | sort | uniq -c
    
    ```
    

---

### **10. Key Takeaways**

- **`cut`**: Extract specific fields or characters from text.
- **`tr`**: Transform or delete characters in streams.
- **`sort`**: Organize text lines based on various criteria.
- **`uniq`**: Remove duplicates and count occurrences in sorted text.