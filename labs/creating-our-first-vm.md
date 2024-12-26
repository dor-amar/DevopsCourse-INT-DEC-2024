### **Lab: Creating Your First Virtual Machine in VirtualBox**

This lab is designed for beginners to guide them step-by-step in creating their first virtual machine (VM) in VirtualBox.

---

### **Objective:**

By the end of this lab, you will:

1. Understand how to create a virtual machine.
2. Learn how to configure basic settings such as memory, storage, and operating system installation.
3. Boot the virtual machine and install an operating system.

---

### **Student Lab Instructions**

### **Lab Overview:**

You will repeat the steps demonstrated by the instructor to create and boot your first virtual machine. Take your time, and don’t hesitate to ask questions.

### **Lab Steps:**

1. **Open VirtualBox**
    - Launch VirtualBox on your computer.
2. **Download the Ubuntu ISO**
    - Download the ISO file from [Ubuntu Downloads](https://ubuntu.com/download/desktop).
3. **Create Your VM**
    - Click **New** and:
        - Name the VM: "My First VM".
        - Type: **Linux**, Version: **Ubuntu (64-bit)**.
    - Allocate **2048 MB (2 GB)** of RAM.
    - Create a **20 GB dynamically allocated virtual hard disk**.
4. **Attach the ISO**
    - Go to **Settings > Storage**.
    - Select the empty CD icon and attach your Ubuntu ISO.
5. **Start the VM**
    - Click **Start**.
    - Follow the on-screen instructions to install Ubuntu.
        - Set your username as **student** and password as **student** during the installation process.
6. **Post-Installation**
    - Once installed, restart the VM.
    - Log in to your Ubuntu desktop using the credentials you set.

---

### **Lab Checklist:**

- [ ]  I created a VM in VirtualBox.
- [ ]  I attached the Ubuntu ISO file.
- [ ]  I booted the VM and started the installation process.
- [ ]  I logged in to the Ubuntu desktop after installation.

---

### **Expected Outcome**

By the end of this lab, your virtual machine should:

- Boot to an Ubuntu desktop environment.
- Be functional and ready for future experiments.

---

### **Troubleshooting Tips**

- **VM Won’t Start:** Double-check the ISO file is correctly attached under **Settings > Storage**.
- **Installation Hangs:** Ensure you have enough free RAM and disk space on your host computer.
- **Boot Order Issues:** Go to **Settings > System** and verify the **Optical Drive** is first in the boot order.

---

### **Time Allocation:**

- **20-30 minutes**

---

### **Additional Notes for Students**

- Be patient as the VM boots for the first time; it may take a few minutes.
- Don’t worry if something doesn’t work right away. Learning virtualization is about experimenting and troubleshooting.