# WSL Setup

To properly run this application, the user needs to be working on a Unix System as most of the dependencies for this program is unable to be ran on a Windows System.

The options available are to:

    1. Migrate to a Dedicated Unix Machine (a MacOs Machine, or Linux-based Machine).
    2. Install WSL to your Windows machine.

I'm under the impression that most users who will visit this repo are Windows users as well, so I made this guide to so that you able to run this application locally, as intended.

## 1) Installing WSL through the Terminal
You can install everything you need to run WSL with a single command, `wsl --install`. This command will install all the features necessary to run WSL along with the Ubuntu distribution of Linux as the default. 

I recommend that you stick with this distribution, as the following commands in this guide will be 1-to-1 to this distribution.

## 2) WSL User Setup
Here is what user setup will look like in it's entirety:
```
Launching Ubuntu...
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: <your_username>
New password: <your_password>
Retype new password: <your_password_again>
passwd: password updated successfully
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.153.1-microsoft-standard-WSL2 x86_64)

- Documentation: https://help.ubuntu.com
- Management: https://landscape.canonical.com
- Support: https://ubuntu.com/advantage

This message is shown once a day. To disable it please create the
/home/<your_username>/.hushlogin file.
<your_username>@DESKTOP-JHLTR9B:~$
```

## 3) Adding your Github Credentials to your Ubuntu Terminal
### Generate SHH Key
First, you'll need to generate an SSH key pair. Open your terminal and run:
```
<your_username>@DESKTOP-JHLTR9B:~$ ssh-keygen -t ed25519 -C <your_github_email@example.com>
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/<your_username>/.ssh/id_ed25519): <Hit Enter/Return>
Enter passphrase (empty for no passphrase): <your_passphrase>
Enter same passphrase again: <your_passphrase>
Your identification has been saved in /home/<your_username>/.ssh/id_ed25519
Your public key has been saved in /home/<your_username>/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX <your_github_email@example.com>
The key's randomart image is:
+--[ED25519 256]--+
|  xxx            |
|x . x.           |
|.. xx.           |
|xx. x .          |
|x x...x.xx       |
| x..x.x.         |
|x.x .x xx x .    |
|x+++xx. .X X     |
|x +xx+. +x.x .   |
+----[SHA256]-----+
```
Note: **REMEMBER TO WRITE DOWN YOUR PASSPHRASES SOMEWHERE!**

### Add the SSH Key to the SSH Agent
``` 
<your_username>@DESKTOP-JHLTR9B:~$ eval "$(ssh-agent -s)"
Agent pid 572
<your_username>@DESKTOP-JHLTR9B:~$ ssh-add ~/.ssh/id_ed25519
Enter passphrase for /home/<your_username>/.ssh/id_ed25519: <your_passphrase>
Identity added: /home/<your_username>/.ssh/id_ed25519 (<your_github_email@example.com>)
```
### Add SSH Key to Your GitHub Account
1. Copy your SSH public key to your clipboard:
```
<your_username>@DESKTOP-JHLTR9B:~$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX <your_github_email@example.com>
```

2. On Github, navigate to your account settings, click on the SSH and GPG keys tab, and then the New SSH key option. You will then paste key from the terminal into the "Key" field.


![Setup Image 0](https://github.com/tcnj-acm/halo/blob/main-dev/.github/IMAGES/setup-image-0.png)

![Setup Image 1](https://github.com/tcnj-acm/halo/blob/main-dev/.github/IMAGES/setup-image-1.png)

![Setup Image 2](https://github.com/tcnj-acm/halo/blob/main-dev/.github/IMAGES/setup-image-2.png)

![Setup Image 3](https://github.com/tcnj-acm/halo/blob/main-dev/.github/IMAGES/setup-image-3.png)

3. Test the Connection

```
<your_username>@DESKTOP-JHLTR9B:~$ ssh -T git@github.com
The authenticity of host 'github.com (140.82.112.3)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? <yes>
Hi <your_github_username>! You've successfully authenticated, but GitHub does not provide shell access.
```
### Clone the Repository
Now you can clone the repository using SSH:
```
<your_username>@DESKTOP-JHLTR9B:~$ git clone git@github.com:tcnj-acm/halo.git
Cloning into 'halo'...
remote: Enumerating objects: 3898, done.
remote: Counting objects: 100% (1265/1265), done.
remote: Compressing objects: 100% (485/485), done.
remote: Total 3898 (delta 756), reused 1094 (delta 711), pack-reused 2633
Receiving objects: 100% (3898/3898), 15.28 MiB | 22.80 MiB/s, done.
Resolving deltas: 100% (2305/2305), done.
```
The repo will now be cloned to your working directory.
```
<your_username>@DESKTOP-JHLTR9B:~$ ls
halo
```

## 4) Getting the Packages to support the Application's Dependencies
Now we'll install all the dependencies so the HALO works as intended. This may be outdated by the time you're reading this, so if you happen need to run extra commands to getting the application up-and-running I implore to make a issue so that contributors of this repo can update this guide.

### Needed Packages (You will need to enter your for Ubuntu password all of these commands):
```
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt update -y && sudo apt upgrade -y
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y python-is-python3
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y python3-pip
<your_username>@DESKTOP-JHLTR9B:~$ pip install pipenv
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y pipenv
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y libpq-dev
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y libmysqlclient-dev
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y mysql-client mysql-server
<your_username>@DESKTOP-JHLTR9B:~$ sudo apt install -y python3-dev 
```

**After doing following these instructions, you should be good to continue the HALO Setup!**

