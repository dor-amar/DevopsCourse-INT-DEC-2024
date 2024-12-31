### **Lab: Text Processing in Linux**

---

### **Lab Objectives**

This lab consolidates all the topics covered in the Text Processing module, including:

1. Basic Text Processing
2. Text Searching and Filtering (`grep`, `sed`, `awk`)
3. Text Transformation (`cut`, `tr`, `sort`, `uniq`)
4. Regular Expressions
5. Summarizing and Comparing Data
6. Formatting and Printing (`fmt`, `column`, `pr`)
7. Handling Large Files

By completing this lab, students will gain hands-on experience with various text processing techniques.

---

### **Instructions**

### **Part 1: Basic Text Processing**

1. Create a file named `example.txt` with the following content:
    
    ```mathematica
    Line 1: This is a test file.
    Line 2: Text processing in Linux is powerful.
    Line 3: Learn Linux and become a pro!
    
    ```
    
2. Display the contents of the file using `cat`.
3. View the first two lines of the file using `head`.
4. Display the last line of the file using `tail`.

---

### **Part 2: Text Searching and Filtering**

1. Search for the word "Linux" in `example.txt` using `grep`.
2. Use `grep` to display line numbers containing the word "test".
3. Replace the word "Linux" with "Unix" in `example.txt` using `sed`.
4. Extract and print the second word of each line in `example.txt` using `awk`.

---

### **Part 3: Text Transformation**

1. Create a CSV file named `data.csv` with the following content:
    
    ```sql
    Name,Age,Location
    Alice,30,New York
    Bob,25,San Francisco
    Charlie,35,Chicago
    
    ```
    
2. Extract the "Name" column using `cut`.
3. Convert all lowercase letters to uppercase in `data.csv` using `tr`.
4. Sort the entries in `data.csv` by age.
5. Remove duplicate lines in a file named `duplicates.txt`:
    
    ```
    apple
    orange
    apple
    banana
    orange
    
    ```
    

---

### **Part 4: Regular Expressions**

1. Extract all lines starting with "Line" from `example.txt`.
2. Find and extract email addresses from the following text saved in `emails.txt`:
    
    ```graphql
    Contact us at support@example.com or admin@linux.com for help.
    
    ```
    
3. Validate IPv4 addresses from a file named `ips.txt` containing:
    
    ```
    192.168.1.1
    255.255.255.255
    123.456.78.90
    
    ```
    

---

### **Part 5: Summarizing and Comparing Data**

1. Count the number of lines, words, and characters in `example.txt` using `wc`.
2. Compare two files, `file1.txt` and `file2.txt`, using `diff`.
3. Identify common and unique lines between two sorted files, `sorted1.txt` and `sorted2.txt`, using `comm`.

---

### **Part 6: Formatting and Printing**

1. Format a paragraph in `long_text.txt` to 50 characters per line using `fmt`.
2. Convert a space-separated file into columns using `column`.
3. Add a header "Formatted Report" and format a file for printing using `pr`.

---

### **Part 7: Handling Large Files**

1. Create a large file with repeated content:
    
    ```bash
    yes "This is a test line." | head -n 10000 > large_file.txt
    
    ```
    
2. Split the file into smaller chunks of 100 lines each using `split`.
3. Extract lines containing "test" and save them to `filtered_large_file.txt`.
4. Compress all chunks of the file in parallel using `gzip`.

---

### **Commands Reference**

The specific commands for the tasks will be provided after students attempt the lab to ensure they actively engage with the tasks.