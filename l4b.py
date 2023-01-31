import os, sys, subprocess, base64

os.system("apt update")
subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
os.system("export DEBIAN_FRONTEND=noninteractive")
os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
os.system("apt remove --assume-yes gnome-terminal")
os.system("apt install --assume-yes xscreensaver")
os.system("systemctl disable lightdm.service")
subprocess.run(["apt-get", "-y", "install", "firefox"], stdout=subprocess.PIPE)
