**Duration:** 20–30 minutes

**Objective:** Provide hands-on experience with essential Linux commands covered in the lecture.

---

### **Lab Setup**

1. **Environment:** Access to a Linux terminal.
2. **Prerequisites:** None; this lab is beginner-friendly.

---

### **Lab Outline**

### **Part 1: Navigating the File System**

1. **Tasks:**
    1. Open the terminal and run `pwd` to display your current working directory.
    2. Use `ls` to list all files in the current directory.
        - Use `ls -l` to view detailed information about files.
        - Use `ls -a` to include hidden files in the output.
    3. Navigate to the `/tmp` directory using `cd /tmp` and confirm with `pwd`.
    4. Create a new directory named `lab_test` using `mkdir lab_test`.
    5. Navigate into the newly created directory using `cd lab_test`.
    6. Return to the home directory using `cd ~`.

---

### **Part 2: Managing Files and Directories**

1. **Tasks:**
    1. Inside your home directory, create an empty file named `test_file.txt` using `touch`.
    2. Verify the file’s creation with `ls`.
    3. Rename `test_file.txt` to `renamed_file.txt` using `mv`.
    4. Create a directory named `sample_dir` using `mkdir`.
    5. Move `renamed_file.txt` into `sample_dir` using `mv`.
    6. Copy the `renamed_file.txt` file inside `sample_dir` to create a duplicate named `copy_file.txt` using `cp`.
    7. Delete `copy_file.txt` using `rm`.
    8. Remove the entire `sample_dir` directory and its contents using `rm -r`.

---

### **Part 3: Viewing and Editing Files**

1. **Tasks:**
    1. Create a new file named `example.txt` using `touch`.
    2. Add the text "Welcome to the Linux lab!" to the file using `echo "Welcome to the Linux lab!" > example.txt`.
    3. Display the content of `example.txt` using `cat`.
    4. Append the text "This is a hands-on session." to the file using `echo`.
    5. View the content one page at a time using `less`. (Press `q` to exit `less`.)
    6. Open the file in the `nano` text editor and add a line: "Enjoy learning Linux!" Save and exit using `CTRL + O`, then `Enter`, and `CTRL + X`.

---

### **Part 4: Checking File Information**

1. **Tasks:**
    1. List detailed information about `example.txt` using `ls -l`.
    2. Check the disk usage of the current directory using `du -h`.
    3. Check the free disk space on the filesystem using `df -h`.
    4. Use the `stat` command to display detailed information about `example.txt`.

---

### **Part 5: Finding Files**

1. **Tasks:**
    1. Search for `example.txt` in the current directory using `find . -name "example.txt"`.
    2. Try using the `locate` command to find files named `example.txt`.(If `locate` is unavailable, explain how it relies on a prebuilt index and can be installed if needed.)

---

### **Part 6: Getting Help**

1. **Tasks:**
    1. Open the manual page for the `ls` command using `man ls`.
    2. Use `ls --help` to display quick reference information for the `ls` command.
    3. Experiment with the `man` command for any other command used in this lab (e.g., `man mkdir`).

---

### **Reference Commands**

Commands covered in this lab:

- `pwd`, `ls`, `cd`, `mkdir`, `rmdir`, `touch`, `rm`, `mv`, `cp`
- `cat`, `nano`, `less`
- `ls -l`, `du`, `df`, `stat`
- `find`, `locate`
- `man`, `-help`