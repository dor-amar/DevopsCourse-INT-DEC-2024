# Copy and Paste from host to vm

[Toturial](https://www.youtube.com/watch?v=saiy4_XsLoA&ab_channel=InnoTechy)

To enable copy and paste functionality between your host machine and a VirtualBox virtual machine, follow these steps:

1. **Install VirtualBox Guest Additions**:
    - Start your virtual machine.
    - In the VirtualBox menu, go to `Devices` > `Insert Guest Additions CD Image`.
    - If prompted, run the installer inside the virtual machine to install Guest Additions.
    - Restart the virtual machine after installation.
2. **Enable Shared Clipboard**:
    - With the virtual machine powered off, select it in the VirtualBox Manager.
    - Click on `Settings` > `General` > `Advanced`.
    - Set `Shared Clipboard` to `Bidirectional` to allow copying and pasting in both directions.
    - Click `OK` to save the settings.
3. **Start the Virtual Machine**:
    - Launch the virtual machine.
    - Test the copy and paste functionality by copying text from the host and pasting it into the virtual machine, and vice versa.