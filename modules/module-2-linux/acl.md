### **ACL (Access Control List) in Linux**

---

### **1. Introduction**

Linux file permissions (using `chmod`) are powerful but limited to the **owner**, **group**, and **others**. **Access Control List (ACL)** expands this functionality by allowing fine-grained permissions for individual users or groups.

---

### **2. What is ACL?**

An **Access Control List (ACL)** provides more flexible permissions by allowing you to specify:

- Which users or groups can access a file or directory.
- The type of access (read, write, execute) they are granted.

---

### **3. Why Use ACL?**

1. **Fine-Grained Control**: Assign specific permissions to multiple users or groups without changing ownership or primary group.
2. **Flexibility**: Overrides the traditional `chmod` permissions.
3. **Use Case**: When a file needs access by users from different groups.

---

### **4. Viewing ACL**

Use the `getfacl` command to view the ACL of a file or directory.

**Example:**

```bash
getfacl file.txt

```

**Output Example:**

```makefile
# file: file.txt
# owner: dor
# group: users
user::rw-
user:john:rw-
group::r--
mask::rw-
other::r--

```

**Explanation:**

- `user::rw-`: Permissions for the file owner.
- `user:john:rw-`: Permissions for the user `john`.
- `group::r--`: Permissions for the group.
- `mask::rw-`: Maximum effective permissions.
- `other::r--`: Permissions for others.

---

### **5. Modifying ACL**

Use the `setfacl` command to modify ACLs.

### **Grant Permissions to a User**

```bash
setfacl -m u:john:rw file.txt

```

- **`m`**: Modify ACL.
- **`u:john:rw`**: Grants read and write permissions to the user `john`.

### **Grant Permissions to a Group**

```bash
setfacl -m g:developers:r file.txt

```

- Grants read permissions to the `developers` group.

### **Remove ACL for a User**

```bash
setfacl -x u:john file.txt

```

- **`x`**: Removes the ACL entry for `john`.

### **Set Default ACL for a Directory**

Default ACLs are inherited by new files or subdirectories.

```bash
setfacl -m d:u:john:rw /mydir

```

---

### **6. Checking if ACL is Enabled**

To check if ACL is enabled on your file system:

```bash
mount | grep acl

```

If ACL is not enabled, remount the file system with the `acl` option:

```bash
sudo mount -o remount,acl /

```

---

### **7. Hands-On Practice**

### **Task 1: View ACL**

1. Create a file:
    
    ```bash
    touch acl_example.txt
    
    ```
    
2. View its ACL:
    
    ```bash
    getfacl acl_example.txt
    
    ```
    

---

### **Task 2: Add and Modify ACL**

1. Add read and write permissions for user `john`:
    
    ```bash
    setfacl -m u:john:rw acl_example.txt
    
    ```
    
2. Add read-only permissions for group `devops`:
    
    ```bash
    setfacl -m g:devops:r acl_example.txt
    
    ```
    
3. Verify the changes:
    
    ```bash
    getfacl acl_example.txt
    
    ```
    

---

### **Task 3: Set Default ACL**

1. Create a directory:
    
    ```bash
    mkdir acl_dir
    
    ```
    
2. Set default ACL for user `john`:
    
    ```bash
    setfacl -m d:u:john:rw acl_dir
    
    ```
    
3. Create a new file in `acl_dir` and verify that `john` has inherited the ACL.

---

### **8. Key Takeaways**

- ACL extends traditional Linux permissions, offering greater flexibility.
- Use `getfacl` to view ACLs and `setfacl` to modify them.
- Default ACLs help manage inherited permissions in directories.