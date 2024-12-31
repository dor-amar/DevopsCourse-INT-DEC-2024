### **Lecture: Regular Expressions in Linux**

---

### **1. Introduction**

**Regular Expressions (Regex)** are patterns used to match and manipulate text in Linux. They are powerful tools for searching, validating, and transforming text data, widely used with commands like **`grep`**, **`sed`**, and **`awk`**.

---

### **2. Why Learn Regex?**

1. **Text Searching**: Quickly find patterns in files or logs.
2. **Validation**: Ensure text matches specific formats (e.g., email addresses, IPs).
3. **Automation**: Simplify tasks like replacing text or extracting fields.

---

### **3. Regex Basics**

### **a) Literal Characters**

- Matches exact text.
- Example: `grep "Linux" file.txt` matches lines containing "Linux".

### **b) Special Characters**

| **Character** | **Meaning** | **Example** |
| --- | --- | --- |
| `.` | Matches any single character. | `h.t` matches `hat`, `hit`, etc. |
| `^` | Matches the start of a line. | `^This` matches lines starting with `This`. |
| `$` | Matches the end of a line. | `end$` matches lines ending with `end`. |
| `*` | Matches zero or more of the preceding character. | `fo*` matches `f`, `fo`, `foo`, etc. |
| `+` | Matches one or more of the preceding character. | `fo+` matches `fo`, `foo`, but not `f`. |
| `?` | Matches zero or one of the preceding character. | `colou?r` matches `color` and `colour`. |
| `[]` | Matches any character in brackets. | `[abc]` matches `a`, `b`, or `c`. |
| `[^]` | Matches any character not in brackets. | `[^abc]` matches any character except `a`, `b`, or `c`. |
| `{}` | Specifies the number of matches. | `a{2,4}` matches `aa`, `aaa`, or `aaaa`. |
| ` | ` | Logical OR. |
| `()` | Groups expressions. | `(ab)+` matches `ab`, `abab`, etc. |

---

### **4. Regex Examples**

### **a) Matching Patterns**

1. Find lines starting with "Error":
    
    ```bash
    grep "^Error" logs.txt
    
    ```
    
2. Find lines ending with a period:
    
    ```bash
    grep "\.$" file.txt
    
    ```
    
3. Find lines containing "log" or "error":
    
    ```bash
    grep "log|error" file.txt
    
    ```
    

### **b) Matching Character Ranges**

1. Match any digit:
    
    ```bash
    grep "[0-9]" file.txt
    
    ```
    
2. Match lowercase letters:
    
    ```bash
    grep "[a-z]" file.txt
    
    ```
    
3. Match anything except vowels:
    
    ```bash
    grep "[^aeiou]" file.txt
    
    ```
    

### **c) Quantifiers**

1. Match lines with at least two `a` characters:
    
    ```bash
    grep "a{2,}" file.txt
    
    ```
    
2. Match lines with exactly three digits:
    
    ```bash
    grep "^[0-9]{3}$" file.txt
    
    ```
    

---

### **5. Using Regex with Common Tools**

### **a) `grep`**

1. Basic Regex:
    
    ```bash
    grep "pattern" file.txt
    
    ```
    
2. Extended Regex:
    
    ```bash
    grep -E "pattern" file.txt
    
    ```
    

### **b) `sed`**

1. Replace text matching a pattern:
    
    ```bash
    sed 's/[0-9]/#/g' file.txt
    
    ```
    
2. Delete lines matching a pattern:
    
    ```bash
    sed '/^$/d' file.txt
    
    ```
    

### **c) `awk`**

1. Print lines matching a pattern:
    
    ```bash
    awk '/pattern/ {print $0}' file.txt
    
    ```
    
2. Extract specific fields based on patterns:
    
    ```bash
    awk '/[0-9]/ {print $1}' file.txt
    
    ```
    

---

### **6. Practical Use Cases**

### **Log Analysis**

1. Extract error messages:
    
    ```bash
    grep -E "ERROR|WARN" /var/log/syslog
    
    ```
    
2. Find lines with timestamps:
    
    ```bash
    grep "^[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}" logs.txt
    
    ```
    

### **Validation**

1. Match valid email addresses:
    
    ```bash
    grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" emails.txt
    
    ```
    
2. Match IPv4 addresses:
    
    ```bash
    grep -E "^[0-9]{1,3}(\.[0-9]{1,3}){3}$" ips.txt
    
    ```
    

### **Data Extraction**

1. Extract fields from a CSV file:
    
    ```bash
    awk -F, '/^[A-Z]/ {print $1, $2}' data.csv
    
    ```
    

---

### **7. Hands-On Practice**

### Task 1: Basic Matching

1. Find lines containing the word "Linux" in `example.txt`.
2. Find lines starting with "Error" in `logs.txt`.

### Task 2: Advanced Matching

1. Match all lines with exactly 5 characters.
2. Extract lines with valid email addresses from `emails.txt`.

### Task 3: Combine Tools

1. Replace all digits with `#` in `example.txt`.
2. Extract and sort unique IP addresses from `logs.txt`.

---

### **8. Key Takeaways**

- Regex allows precise text matching and manipulation.
- Use basic patterns (`^`, `$`, `.`) for quick searches.
- Employ advanced patterns (`{}`, `|`, `()`) for complex requirements.
- Combine regex with tools like `grep`, `sed`, and `awk` for powerful workflows.