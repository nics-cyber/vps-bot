Here’s the updated **README.md** file that includes all the features, installation instructions, and usage details for the **Discord VPS Deployer** bot. This README is designed to be comprehensive and user-friendly.

---

# Discord VPS Deployer

A Discord bot that allows you to deploy VPS instances with custom OS, RAM, and CPU configurations. The bot integrates with **FreeRoot** for OS customization, supports **tmate** for instant SSH access, and includes advanced features like automatic cleanup, status monitoring, and more.

---

## Features

1. **Custom VPS Deployment:**
   - Deploy a VPS with a simple `/deploy os ram cpu` command.
   - Supports **40 different operating systems**.

2. **FreeRoot Integration:**
   - Uses **FreeRoot** to customize the OS image before deployment (e.g., SSH keys, user accounts, pre-installed software).

3. **tmate SSH Access:**
   - Automatically generates a tmate SSH session and sends the connection details to the user via DM.

4. **Automatic VPS Cleanup:**
   - Automatically deletes a VPS after a specified timeout (e.g., 1 hour, 24 hours).

5. **VPS Status Monitoring:**
   - Check the status of a deployed VPS using the `/status` command.

6. **Discord Channel and Role Restrictions:**
   - Restrict VPS deployment to specific Discord channels and roles.

7. **Validation:**
   - Ensures RAM and CPU values are within acceptable ranges.

8. **No Docker or Systemd:**
   - Runs natively without requiring Docker or systemd.

9. **Multiple VPS Instances:**
   - Deploy and manage multiple VPS instances simultaneously.

10. **40 Supported Operating Systems:**
    - Includes popular Linux distributions, BSD variants, and specialized OS like Kali Linux and Tails.

---

## Supported Operating Systems

The bot supports the following **40 operating systems**:

| OS Name         | Download URL                                                                 |
|-----------------|------------------------------------------------------------------------------|
| Ubuntu          | [Ubuntu 22.04](https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso) |
| Debian          | [Debian 12](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso) |
| CentOS          | [CentOS 7](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) |
| Fedora          | [Fedora 38](https://download.fedoraproject.org/pub/fedora/linux/releases/38/Server/x86_64/iso/Fedora-Server-dvd-x86_64-38-1.6.iso) |
| Arch            | [Arch Linux](https://mirror.rackspace.com/archlinux/iso/2023.10.14/archlinux-2023.10.14-x86_64.iso) |
| Alpine          | [Alpine Linux](https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-virt-3.18.4-x86_64.iso) |
| Kali            | [Kali Linux](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso) |
| OpenSUSE        | [OpenSUSE Leap 15.5](https://download.opensuse.org/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64.iso) |
| Rocky           | [Rocky Linux 9](https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.2-x86_64-dvd.iso) |
| FreeBSD         | [FreeBSD 13.2](https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-dvd1.iso) |
| Gentoo          | [Gentoo LiveGUI](https://bouncer.gentoo.org/fetch/root/all/releases/amd64/autobuilds/20231008T170153Z/livegui-amd64-20231008T170153Z.iso) |
| Manjaro         | [Manjaro KDE](https://download.manjaro.org/kde/22.1.0/manjaro-kde-22.1.0-230529-linux61.iso) |
| Mint            | [Linux Mint 21.2](https://mirrors.edge.kernel.org/linuxmint/iso/stable/21.2/linuxmint-21.2-cinnamon-64bit.iso) |
| Pop!_OS         | [Pop!_OS 22.04](https://pop-iso.sfo2.cdn.digitaloceanspaces.com/22.04/amd64/intel/7/pop-os_22.04_amd64_intel_7.iso) |
| Zorin           | [Zorin OS 16.2](https://mirrors.edge.kernel.org/zorinos-isos/16/Zorin-OS-16.2-Core-64-bit.iso) |
| Elementary      | [elementary OS 7.0](https://ams3.dl.elementary.io/download/MTY2NzI2NzI2OA==/elementaryos-7.0-stable.20230308.iso) |
| Deepin          | [Deepin 23 Beta](https://cdimage.deepin.com/releases/23/Deepin-23-Beta2-amd64.iso) |
| MX Linux        | [MX Linux 23](https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-23_x64.iso/download) |
| Slackware       | [Slackware 15.0](https://mirrors.slackware.com/slackware/slackware64-15.0/iso/slackware64-15.0-install-dvd.iso) |
| Void            | [Void Linux](https://alpha.de.repo.voidlinux.org/live/current/void-live-x86_64-20230628.iso) |
| NixOS           | [NixOS 23.05](https://channels.nixos.org/nixos-23.05/latest-nixos-plasma5-x86_64-linux.iso) |
| Clear           | [Clear Linux](https://cdn.download.clearlinux.org/releases/38510/clear/clear-38510-live.iso) |
| Tails           | [Tails](https://tails.boum.org/install/vm/Tails.amd64.5.18.1-0.img) |
| Parrot          | [Parrot Security](https://deb.parrot.sh/parrot/iso/5.3/Parrot-security-5.3_amd64.iso) |
| BlackArch       | [BlackArch Linux](https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2023.09.01-x86_64.iso) |
| Qubes           | [Qubes OS](https://mirrors.edge.kernel.org/qubes/iso/Qubes-R4.1.2-x86_64.iso) |
| ReactOS         | [ReactOS](https://sourceforge.net/projects/reactos/files/ReactOS/0.4.15/ReactOS-0.4.15-iso.zip/download) |
| Haiku           | [Haiku OS](https://download.haiku-os.org/nightly-images/x86_64/haiku-nightly-hrev57681-x86_64-anyboot.zip) |
| Solus           | [Solus](https://downloads.getsol.us/4.4/Solus-4.4-Budgie.iso) |
| Puppy           | [Puppy Linux](https://distro.ibiblio.org/puppylinux/puppy-fossa/fossapup64-9.5.iso) |
| TinyCore        | [TinyCore Linux](http://tinycorelinux.net/13.x/x86_64/release/TinyCorePure64-13.0.iso) |
| antiX           | [antiX Linux](https://sourceforge.net/projects/antix-linux/files/Final/antiX-23/antiX-23_x64-full.iso/download) |
| Bodhi           | [Bodhi Linux](https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download) |
| Peppermint      | [Peppermint OS](https://peppermintos.com/iso/Peppermint-11-20230703-amd64.iso) |
| Lubuntu         | [Lubuntu](https://cdimage.ubuntu.com/lubuntu/releases/22.04/release/lubuntu-22.04.3-desktop-amd64.iso) |
| Kubuntu         | [Kubuntu](https://cdimage.ubuntu.com/kubuntu/releases/22.04/release/kubuntu-22.04.3-desktop-amd64.iso) |
| Xubuntu         | [Xubuntu](https://cdimage.ubuntu.com/xubuntu/releases/22.04/release/xubuntu-22.04.3-desktop-amd64.iso) |
| Ubuntu Budgie   | [Ubuntu Budgie](https://cdimage.ubuntu.com/ubuntu-budgie/releases/22.04/release/ubuntu-budgie-22.04.3-desktop-amd64.iso) |
| Ubuntu MATE     | [Ubuntu MATE](https://cdimage.ubuntu.com/ubuntu-mate/releases/22.04/release/ubuntu-mate-22.04.3-desktop-amd64.iso) |
| Ubuntu Studio   | [Ubuntu Studio](https://cdimage.ubuntu.com/ubuntustudio/releases/22.04/release/ubuntustudio-22.04.3-dvd-amd64.iso) |
| Edubuntu        | [Edubuntu](https://cdimage.ubuntu.com/edubuntu/releases/22.04/release/edubuntu-22.04.3-desktop-amd64.iso) |
| Kali Live       | [Kali Linux Live](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-live-amd64.iso) |
| Kali Light      | [Kali Linux Light](https://cdimage.kali.org/kali-2023.3/kali-linux-light-2023.3-amd64.iso) |
| Kali Everything | [Kali Linux Everything](https://cdimage.kali.org/kali-2023.3/kali-linux-everything-2023.3-amd64.iso) |

---

## Prerequisites

1. **Python 3.8 or higher:** Ensure Python is installed on your system.
2. **Discord Bot Token:** Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and get the bot token.
3. **Virtualization Tools:** Install tools like `qemu` or `VirtualBox` for VPS deployment.
4. **Git:** Install Git to clone the FreeRoot repository.
5. **tmate:** Install tmate for instant SSH access.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/discord-vps-deployer.git
   cd discord-vps-deployer
   ```

2. **Install Dependencies:**
   ```bash
   pip install discord.py
   sudo apt update
   sudo apt install wget git qemu-kvm tmate
   ```

3. **Configure the Bot:**
   - Open the `discord_vps_deployer.py` file.
   - Replace `YOUR_DISCORD_BOT_TOKEN` with your actual bot token.
   - Replace `ALLOWED_CHANNEL_IDS` and `ALLOWED_ROLE_IDS` with the IDs of the channels and roles you want to allow.

4. **Run the Bot:**
   ```bash
   python3 discord_vps_deployer.py
   ```

---

## Usage

### Deploy a VPS

Use the `/deploy` command to deploy a VPS with the specified OS, RAM, and CPU.

**Command Format:**
```
/deploy <os> <ram> <cpu> [--timeout <seconds>]
```

**Example:**
```
/deploy ubuntu 2048 2 --timeout 3600
```

This command will deploy a VPS with:
- OS: Ubuntu
- RAM: 2048MB (2GB)
- CPU: 2 cores
- Timeout: 3600 seconds (1 hour)

### Check VPS Status

Use the `/status` command to check the status of a deployed VPS.

**Command Format:**
```
/status <vps_id>
```

**Example:**
```
/status 1
```

### Automatic Cleanup

If a timeout is specified during deployment, the VPS will be automatically deleted after the specified time.

---

## Example Workflow

1. **User in Allowed Channel:**
   ```
   User: /deploy ubuntu 2048 2 --timeout 3600
   Bot: 🚀 Deploying VPS with OS: ubuntu, RAM: 2048MB, CPU: 2 cores...
   Bot: ✅ VPS deployed successfully! VPS ID: 1
   Bot: 📩 Check your DMs for the SSH connection details!
   Bot: ⏳ VPS 1 will be deleted in 3600 seconds.
   ```

2. **User Receives DM:**
   ```
   Bot (DM): 🔑 Your VPS SSH connection:
   ```
   ssh user@tmate.io
   ```

3. **User in Disallowed Channel:**
   ```
   User: /deploy ubuntu 2048 2
   Bot: ❌ This command is not allowed in this channel.
   ```

4. **User Without Allowed Role:**
   ```
   User: /deploy ubuntu 2048 2
   Bot: ❌ You do not have permission to use this command.
   ```

5. **Invalid Input:**
   ```
   User: /deploy ubuntu 128 2
   Bot: ❌ Invalid RAM amount. Please specify a value between 512 and 16384 MB.
   ```

---

## Notes

- Replace `YOUR_DISCORD_BOT_TOKEN` with your actual bot token.
- Ensure the bot has the necessary permissions in your Discord server.
- Test the script thoroughly before deploying it in a production environment.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy deploying VPS instances with ease using the **Discord VPS Deployer**! 🚀

---

This README provides a comprehensive guide to setting up and using the bot. Let me know if you need further assistance! 🚀
