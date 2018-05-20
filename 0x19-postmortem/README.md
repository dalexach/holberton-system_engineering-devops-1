# Issue Summary

For 5 hours between 15:00 and 20:00 on May 18th, 2018 the system failure occurred. For the 5 hours I was unable to access my Linux distro, Pop!_OS. The root cause of the outage was running the command `sudo apt-get purge python3` while trying to downgrade the Python version on Pop!_OS to Python 3.4.

# Timeline

* 15:00 - The user ran `sudo apt-get purge python3` and noticed that it started uninstalling important files in the function of the distro.
* 16:00 - After looking into ways to solve the problem without having to reinstall the distro the user tried to reinstall all the packages that were deleted to no avail.
* 18:00 - The user decides to reboot the computer in the hopes that restarting will allow the user to find the recovery OS.
* 18:15 - After searching the BIOS and UEFI the user determines that the distro is unrecoverable and boots the computer into Windows 10.
* 19:00 - Does more research to see if there is a way to fix the issue from the command line and decides that the easiest course of action is to flash the OS onto a USB and reinstall the OS.
* 20:00 - The OS is reinstalled from the USB and all functionality is restored to the previous settings.

# Root Cause

The user didn't understand the implications of running `sudo apt-get purge python3`.

# Resolution

The user had to fresh reinstall the OS from a USB.

# Corrective/Preventative Measures

The user will now research in more depth what will happen before running any sort of `sudo apt-get purge` on their machine.
