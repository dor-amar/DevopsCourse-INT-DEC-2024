# Quiz Time!

### **Quiz: Text Processing in Linux**

Choose the correct answer for each question. Each question has one correct answer.

---

### **Part 1: Basic Text Processing**

**1. Which command displays the entire contents of a file?**

- [ ] a) `head`  
- [ ] b) `cat`  
- [ ] c) `tail`  
- [ ] d) `grep`  

---

**2. How do you display the last 3 lines of a file?**

- [ ] a) `cat -n 3 file.txt`  
- [ ] b) `head -n 3 file.txt`  
- [ ] c) `tail -n 3 file.txt`  
- [ ] d) `wc -l file.txt`  

---

### **Part 2: Text Searching and Filtering**

**3. What does the `grep` command do?**

- [ ] a) Sort lines in a file.  
- [ ] b) Search for patterns in text.  
- [ ] c) Count lines in a file.  
- [ ] d) Replace text in a file.  

---

**4. How do you replace all occurrences of "Linux" with "Unix" in a file using `sed`?**

- [ ] a) `sed -r "Linux/Unix" file.txt`  
- [ ] b) `sed "s/Linux/Unix/g" file.txt`  
- [ ] c) `sed "r/Linux/Unix" file.txt`  
- [ ] d) `sed "Linux Unix" file.txt`  

---

**5. Which `awk` command prints the first column of a file?**

- [ ] a) `awk '{print $1}' file.txt`  
- [ ] b) `awk '{print $2}' file.txt`  
- [ ] c) `awk '{print $0}' file.txt`  
- [ ] d) `awk '{print $3}' file.txt`  

---

### **Part 3: Text Transformation**

**6. Which command extracts the first field from a colon-delimited file?**

- [ ] a) `cut -f 1 file.txt`  
- [ ] b) `cut -d ':' -f 1 file.txt`  
- [ ] c) `cut -d ',' -f 1 file.txt`  
- [ ] d) `cut -d ':' -c 1 file.txt`  

---

**7. How do you convert all lowercase characters in a file to uppercase?**

- [ ] a) `cat file.txt | tr 'A-Z' 'a-z'`  
- [ ] b) `cat file.txt | tr 'a-z' 'A-Z'`  
- [ ] c) `cat file.txt | tr -d 'a-z'`  
- [ ] d) `cat file.txt | tr 'A-Z'`  

---

**8. Which command removes duplicate lines from a file?**

- [ ] a) `uniq`  
- [ ] b) `cut`  
- [ ] c) `wc`  
- [ ] d) `awk`  

---

### **Part 4: Regular Expressions**

**9. What does the regex `^Error` match?**

- [ ] a) Lines ending with "Error".  
- [ ] b) Lines starting with "Error".  
- [ ] c) Lines containing "Error".  
- [ ] d) Lines not containing "Error".  

---

**10. Which regex matches an email address?**

- [ ] a) `[a-z0-9]+@[a-z]+\.[a-z]{2,}`  
- [ ] b) `[a-z0-9]+@+.[a-z]+`  
- [ ] c) `[a-z]+#[a-z]+.[a-z]`  
- [ ] d) `[0-9]@[a-z]{2}`  

---

### **Part 5: Summarizing and Comparing Data**

**11. Which command counts the number of lines in a file?**

- [ ] a) `wc -l file.txt`  
- [ ] b) `grep -c file.txt`  
- [ ] c) `awk -l file.txt`  
- [ ] d) `sort -l file.txt`  

---

**12. What does `diff` do?**

- [ ] a) Counts differences between two files.  
- [ ] b) Compares two files line-by-line.  
- [ ] c) Sorts files.  
- [ ] d) Replaces text in a file.  

---

### **Part 6: Formatting and Printing**

**13. Which command formats text to a specific width?**

- [ ] a) `column`  
- [ ] b) `fmt`  
- [ ] c) `pr`  
- [ ] d) `awk`  

---

**14. How do you add a header "Report" to a file for printing?**

- [ ] a) `column -h "Report" file.txt`  
- [ ] b) `fmt -h "Report" file.txt`  
- [ ] c) `pr -h "Report" file.txt`  
- [ ] d) `awk -h "Report" file.txt`  

---

### **Part 7: Handling Large Files**

**15. Which command splits a file into 1MB chunks?**

- [ ] a) `split -l 1M file.txt`  
- [ ] b) `split -b 1M file.txt`  
- [ ] c) `split -s 1M file.txt`  
- [ ] d) `split -n 1M file.txt`  

---

**16. How do you process a large file line-by-line to avoid memory issues?**

- [ ] a) `grep`  
- [ ] b) `awk`  
- [ ] c) `sed`  
- [ ] d) Both `awk` and `sed`  
