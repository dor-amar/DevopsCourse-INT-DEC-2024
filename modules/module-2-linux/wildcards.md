# Wildcards

### **1. Introduction**

In Linux, **wildcards** are special characters used to represent patterns in file or directory names. They allow users to perform operations (like listing, copying, or deleting) on multiple files or directories without typing each name explicitly.

Wildcards make command-line tasks faster and more efficient by enabling pattern matching.

---

### **2. Types of Wildcards**

### **a) Asterisk ()**

- **What**: Matches zero or more characters.
- **Use Case**: To represent "anything."
- **Examples**:
    - `ls *.txt` → Lists all files ending with `.txt`.
    - `cp file* /backup/` → Copies all files starting with `file` to the `/backup/` directory.
    - `rm *` → Deletes all files in the current directory.

---

### **b) Question Mark (`?`)**

- **What**: Matches exactly one character.
- **Use Case**: To represent "any single character."
- **Examples**:
    - `ls file?.txt` → Lists files like `file1.txt` or `fileA.txt` but not `file12.txt`.
    - `mv doc?.pdf /docs/` → Moves files like `doc1.pdf` or `doc2.pdf` to `/docs/`.

---

### **c) Brackets (`[]`)**

- **What**: Matches any one character specified inside the brackets.
- **Use Case**: For character ranges or specific sets.
- **Examples**:
    - `ls file[123].txt` → Lists files like `file1.txt`, `file2.txt`, or `file3.txt`.
    - `ls file[a-z].txt` → Lists files like `filea.txt`, `fileb.txt`, etc., using a character range.

---

### **d) Negation (`!` or `^` inside `[]`)**

- **What**: Matches any character NOT specified inside the brackets.
- **Use Case**: To exclude certain characters.
- **Examples**:
    - `ls file[!a-z].txt` → Lists files that do not have a lowercase letter after `file`.
    - `ls file[^1-3].txt` → Lists files that do not end with `1`, `2`, or `3`.

---

### **e) Curly Braces (`{}`)**

- **What**: Matches a set of comma-separated strings or ranges.
- **Use Case**: For specific patterns.
- **Examples**:
    - `cp file{1,2,3}.txt /backup/` → Copies `file1.txt`, `file2.txt`, and `file3.txt` to `/backup/`.
    - `mv {file1,file2}.txt /docs/` → Moves `file1.txt` and `file2.txt` to `/docs/`.

---

### **3. Combining Wildcards**

You can combine wildcards to create complex patterns for better control.

### **Examples**:

1. `ls file*?.txt` → Lists files starting with `file`, followed by at least one character, ending in `.txt`.
2. `cp *[a-zA-Z].log /logs/` → Copies all `.log` files ending with a letter to the `/logs/` directory.
3. `rm *{.tmp,.bak}` → Deletes all `.tmp` and `.bak` files.

---

### **4. Wildcards vs. Regular Expressions**

- **Wildcards**: Simpler, used for filename matching in commands like `ls`, `cp`, or `rm`.
- **Regular Expressions**: More powerful and used in tools like `grep`, `sed`, or `awk`.

---

### **5. Common Use Cases**

### **Listing Files**

```bash
ls *.txt
```

Lists all files ending with `.txt`.

### **Copying Multiple Files**

```bash
cp file[1-5].txt /backup/

```

Copies `file1.txt` to `file5.txt` into `/backup/`.

### **Deleting Files**

```bash
rm file?.*
```

Deletes files like `file1.log` or `fileA.txt` but not `file12.log`.

### **Searching for Specific Patterns**

```bash
find . -name "*.log"
```

Finds all `.log` files in the current directory and its subdirectories.

---

### **6. Practical Examples**

### Example 1: Using the Asterisk ()

- Create sample files:
    
    ```bash
    touch file1.txt file2.txt file3.log file4.tmp
    
    ```
    
- List all `.txt` files:
    
    ```bash
    ls *.txt
    
    ```
    
- Delete all `.tmp` files:
    
    ```bash
    rm *.tmp
    
    ```
    

---

### Example 2: Using Question Mark (`?`)

- Create sample files:
    
    ```bash
    touch doc1.pdf doc2.pdf docA.pdf docAB.pdf
    
    ```
    
- List files with exactly one character after `doc`:
    
    ```bash
    ls doc?.pdf
    
    ```
    

---

### Example 3: Using Brackets (`[]`)

- Create sample files:
    
    ```bash
    touch file1.txt file2.txt file3.txt file4.txt
    ```
    
- List files ending with `1` or `2`:
    
    ```bash
    ls file[12].txt
    
    ```
    

---

### Example 4: Using Curly Braces (`{}`)

- Create files:
    
    ```bash
    touch test1.log test2.log test3.log
    
    ```
    
- Copy files:
    
    ```bash
    cp test{1,3}.log /backup/
    
    ```
    

---

### **7. Common Mistakes**

1. Using wildcards without caution (e.g., `rm *` can delete everything in the current directory).
2. Confusing `?` with  (remember, `?` matches one character, while  matches zero or more).

---

### **8. Hands-On Practice for Students**

### Task 1: Create Files and Use Wildcards

1. Create the following files:
    
    ```bash
    touch report1.txt report2.txt log1.log log2.tmp fileA fileB fileC
    
    ```
    
2. List all `.txt` files.
3. List files that start with `log`.
4. Copy files `report1.txt` and `log1.log` to a `backup/` directory.

### Task 2: Use Brackets and Curly Braces

1. List files that start with `file` and end with `A` or `B`.
2. Create files named `test1.log`, `test2.log`, and `test3.log` using a single command.

### Task 3: Delete Files Safely

1. Delete all `.tmp` files.
2. Delete files starting with `report`.

---

### **9. Key Takeaways**

- Wildcards simplify working with multiple files and directories.
- The asterisk () is the most versatile wildcard, while `?`, `[]`, and `{}` allow for more specific patterns.
- Always double-check your wildcard commands, especially with `rm`, to avoid accidental deletions.