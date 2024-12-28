# Mini Project: Organize a Linux System for a Small Company
**Objective:**

Set up a simple Linux environment to simulate a small company's file structure and user management, applying what you've learned about Linux commands, directories, permissions, and links.

---

### **Project Tasks**

### 1. **Set Up the Directory Structure**

Create a structure representing a company with two departments:

```bash
/company
  ├── finance
  ├── it
  └── shared

```

- **Task:** Use the `mkdir` command to create these directories.
- **Submission Requirement:** Provide a screenshot of the output of `tree /company` (install `tree` if not available).

---

### 2. **Create Users and Groups (Bonus)**

Create the following:

- **Users:** `finance1`, `finance2`, `it1`, `it2`
- **Groups:** `finance_team`, `it_team`
- Assign users to their respective groups:
    - `finance1` and `finance2` → `finance_team`
    - `it1` and `it2` → `it_team`
- **Task:** Use the `useradd`, `groupadd`, and `usermod` commands.
- **Submission Requirement:** Provide the output of `cat /etc/group` showing the group memberships.

---

### 3. **Set Directory Permissions**

- Set permissions so:
    - Only `finance_team` can access `/company/finance`.
    - Only `it_team` can access `/company/it`.
    - Everyone can access `/company/shared`, but only members of `finance_team` and `it_team` can write to it.
- **Task:** Use `chmod`, `chown`, and `chgrp` commands to configure permissions.
- **Submission Requirement:** Provide the output of `ls -ld /company/*` showing the permission settings.

---

### 4. **Create Links**

- Create a **hard link** for a file in `/company/finance` inside `/company/shared`.
- Create a **soft link** for a file in `/company/it` inside `/company/shared`.
- **Task:** Use the `ln` command for hard links and `ln -s` for soft links.
- **Submission Requirement:** Provide the output of `ls -l /company/shared` showing the links.

---

### 5. **Set an Environment Variable**

- Set an environment variable `COMPANY_HOME` pointing to `/company` for all users.
- **Task:** Add the environment variable to `/etc/environment` or each user's `.bashrc` file. (Bonus)
- **Submission Requirement:** Provide the output of `env | grep COMPANY_HOME` for any user.

---

### 6. **Create a Documentation File**

- Write a short report explaining:
    - The steps you took.
    - The commands you used and their purpose.
    - Any challenges faced and how you resolved them.
- **Submission Requirement:** Submit the report as a text file or document (e.g., `report.txt`).

---

### **Bonus Tasks (Optional)**

1. Create a cron job that backs up the `/company/shared` directory daily to `/company/backups`.
2. Add another user (`manager1`) with access to all directories.