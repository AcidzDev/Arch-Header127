#!/usr/bin/python
# Script to patch arch for header 127

# Requirements
import os
import wget
import time
import shutil


# Patch URL
PatchURL = "https://clbin.com/VCiYJ"

# Install Package requirements
os.system("sudo pacman -Syu base-devel pacman-contrib")

# Linux location
LinuxPath = 'linux/trunk'

# Checkout linux package
os.system("asp update")
os.system("asp checkout linux")
time.sleep(0.5)

# Change Dir
os.chdir(LinuxPath)

# Download patch
wget.download(PatchURL, LinuxPath)
time.sleep(0.5)

# Change name of patch
shutil.move('VCiYJ', 'pci.patch')

# Add pci.patch to PKGBUUILD
os.system("sed -i '/linux.preset   # standard config files for mkinitcpio ramdisk/a    \  pci.patch      # PCI Header 127 Fix' PKGBUILD")

# Increase MAKE Performance
os.system("sudo sed -i -e 's/#MAKEFLAGS="-j2"/MAKEFLAGS="-j$(nproc)"/g' /etc/makepkg.conf")

# Update Pacman NOMNOMNOM
os.system("sudo pacman -Syu")
time.sleep(0.5)

# update PKGBUILD
os.system("updpkgsums")

# Compile ya boi
print("Are you ready to compile the kernel\n")
input("Press ENTER to continue...")
os.system("makepkg -s")
time.sleep(0.5)

# Install compiled
os.system('clear')
answer = None
while answer not in ("yes", "no"):
    answer = input("Do you wish to install the kernel now?, Enter yes or no: ")
    if answer == "yes":
         os.system("sudo pacman -U linux-*")
         print("\nPlease update your bootloader with the new kernel and reboot")
    elif answer == "no":
         print("To install the kernel, navigate to linux/trunk and run sudo pacman -U linux-*")
         exit()
    else:
    	print("Please enter yes or no.")

