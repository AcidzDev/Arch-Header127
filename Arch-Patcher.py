
# Script to patch arch for header 127

# Requirements
import os
import sys
import wget
import time
import shutil


# Patch URL
PatchURL = "https://clbin.com/VCiYJ"

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
os.system()
