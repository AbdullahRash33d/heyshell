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
subprocess.run(["sudo", "apt-get", "-y", "install", "firefox"], stdout=subprocess.PIPE)
prefs = ['user_pref("beacon.enabled", false);', 'user_pref("browser.cache.disk.enable", false);', 'user_pref("browser.privatebrowsing.autostart", true);', 'user_pref("browser.safebrowsing.appRepURL", "");', 'user_pref("browser.safebrowsing.malware.enabled", false);', 'user_pref("browser.send_pings", false);', 'user_pref("dom.battery.enabled", false);', 'user_pref("extensions.autoDisableScopes", 14);', 'user_pref("media.navigator.enabled", false);', 'user_pref("media.peerconnection.enabled", false);', 'user_pref("media.video_stats.enabled", false);', 'user_pref("network.cookie.cookieBehavior", 1);', 'user_pref("network.dns.disablePrefetch", true);', 'user_pref("network.dns.disablePrefetchFromHTTPS", true);', 'user_pref("network.http.referer.XOriginPolicy", 2);', 'user_pref("network.predictor.enable-prefetch", false);', 'user_pref("network.predictor.enabled", false);', 'user_pref("network.prefetch-next", false);', 'user_pref("extensions.autoDisableScopes", 14);']
os.system("sudo -u user firefox -CreateProfile 'DEFAULT'")
firefox_path = '/home/user/.mozilla/firefox'
folders = [name for name in os.listdir(firefox_path) if os.path.isdir(os.path.join(firefox_path, name))]
for folder in folders:
    if 'DEFAULT' in folder:
        user_prefs = open(f"{firefox_path}/{folder}/prefs.js".replace("/","//"), "w+")
        for pref in prefs:
            user_prefs.write(f"{pref}\n")
        user_prefs.close()
        os.system(f"sudo -u user wget https://github.com/AbdullahRash33d/heyshell/raw/main/extensions.zip -P {firefox_path}/{folder}/")
        os.system(f"sudo -u user unzip {firefox_path}/{folder}/extensions.zip -d {firefox_path}/{folder}/")
        os.system(f"sudo -u user rm -rf {firefox_path}/{folder}/extensions.zip")
        os.system("""sudo -u user touch /home/user/Desktop/firefox.sh && echo 'firefox -P "DEFAULT"' >> /home/user/Desktop/firefox.sh && chmod +x /home/user/Desktop/firefox.sh""")
