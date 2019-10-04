#!/usr/bin/python
# Script to patch arch for header 127

# Requirements
import os
import wget
import time
import shutil


# Patch URL
PatchURL = 'https://clbin.com/VCiYJ'

# Linux location
LinuxPath = 'linux/trunk/'

# Increase MAKE Performance
f = open("makeupdate.txt", "r")
string = f.read()
os.system("sudo "+ string)

#Script Start
print("This script will patch the current kernel for ArchLinux")
print("WARNING: Sometimes after patching the kernel you may have driver issues, please have another system that you able to SSH to resolve any driver issues")
input ("Press ENTER to Begin....")

# Install required packages
os.system("sudo pacman -Syu base-devel asp pacman-contrib")

# Checkout linux package
print("Obtaining the kernel")
os.system("asp update")
os.system("asp checkout linux")
time.sleep(0.5)

# Change Dir
os.chdir(LinuxPath)
print(LinuxPath)

# Download patch
wget.download(PatchURL)
time.sleep(0.5)

# Change name of patch
print("Obtaining Patch")
shutil.move('VCiYJ', 'pci.patch')

# Add pci.patch to PKGBUUILD
os.system("sed -i '/linux.preset   # standard config files for mkinitcpio ramdisk/a    \  pci.patch      # PCI Header 127 Fix' PKGBUILD")

# Update Pacman NOMNOMNOM
os.system("sudo pacman -Syu")
time.sleep(0.5)

# update PKGBUILD
os.system("updpkgsums")

# Compile ya boi
print("Are you ready to compile the kernel")
input("Press ENTER to continue...")
os.system("makepkg -s")
time.sleep(0.5)

# Install compiled
answer = None
while answer not in ("yes", "no"):
    answer = input("Do you wish to install the kernel now?, Enter yes or no: ")
    if answer == "yes":
         os.system("sudo pacman -U *.tar.gz")
         print("\nPlease update your bootloader with the new kernel and reboot")
    elif answer == "no":
         print("To install the kernel, navigate to linux/trunk and run sudo pacman -U linux-*")
         exit()
    else:
        print("Please enter yes or no.")
