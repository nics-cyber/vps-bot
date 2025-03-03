

# Discord VPS Deployer

A Discord bot that allows you to deploy VPS instances with custom OS, RAM, and CPU configurations. The bot integrates with **FreeRoot** for OS customization and supports 10 different operating systems.

---

## Features

- **Easy Deployment Command:** Deploy a VPS with a simple `/deploy os ram cpu` command.
- **Custom OS Customization:** Uses **FreeRoot** to customize the OS before deployment.
- **10 Supported OS Options:** Choose from 10 different operating systems.
- **Discord Channel and Role Restrictions:** Only allow deployment in specific channels and for specific roles.
- **Validation:** Ensures RAM and CPU values are within acceptable ranges.

---

## Supported Operating Systems

The bot supports the following operating systems:

| OS Name   | Download URL                                                                 |
|-----------|------------------------------------------------------------------------------|
| Ubuntu    | [Ubuntu 22.04](https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso) |
| Debian    | [Debian 12](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso) |
| CentOS    | [CentOS 7](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) |
| Fedora    | [Fedora 38](https://download.fedoraproject.org/pub/fedora/linux/releases/38/Server/x86_64/iso/Fedora-Server-dvd-x86_64-38-1.6.iso) |
| Arch      | [Arch Linux](https://mirror.rackspace.com/archlinux/iso/2023.10.14/archlinux-2023.10.14-x86_64.iso) |
| Alpine    | [Alpine Linux](https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-virt-3.18.4-x86_64.iso) |
| Kali      | [Kali Linux](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso) |
| OpenSUSE  | [OpenSUSE Leap 15.5](https://download.opensuse.org/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64.iso) |
| Rocky     | [Rocky Linux 9](https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.2-x86_64-dvd.iso) |
| FreeBSD   | [FreeBSD 13.2](https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-dvd1.iso) |

---

## Prerequisites

1. **Python 3.8 or higher:** Ensure Python is installed on your system.
2. **Discord Bot Token:** Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and get the bot token.
3. **Virtualization Tools:** Install tools like `qemu` or `VirtualBox` for VPS deployment.
4. **Git:** Install Git to clone the FreeRoot repository.

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
   sudo apt install wget git
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
/deploy <os> <ram> <cpu>
```

**Example:**
```
/deploy ubuntu 2048 2
```

This command will deploy a VPS with:
- OS: Ubuntu
- RAM: 2048MB (2GB)
- CPU: 2 cores

### Supported OS Options

You can deploy the following operating systems:
- `ubuntu`
- `debian`
- `centos`
- `fedora`
- `arch`
- `alpine`
- `kali`
- `opensuse`
- `rocky`
- `freebsd`

### Validation

- **RAM:** Must be between 512MB and 16384MB.
- **CPU:** Must be between 1 and 16 cores.

---

## Example Workflow

1. **User in Allowed Channel:**
   ```
   User: /deploy ubuntu 2048 2
   Bot: 🚀 Deploying VPS with OS: ubuntu, RAM: 2048MB, CPU: 2 cores...
   Bot: ✅ VPS deployed successfully!
   ```

2. **User in Disallowed Channel:**
   ```
   User: /deploy ubuntu 2048 2
   Bot: ❌ This command is not allowed in this channel.
   ```

3. **User Without Allowed Role:**
   ```
   User: /deploy ubuntu 2048 2
   Bot: ❌ You do not have permission to use this command.
   ```

4. **Invalid Input:**
   ```
   User: /deploy ubuntu 128 2
   Bot: ❌ Invalid RAM amount. Please specify a value between 512 and 16384 MB.
   ```

---

## Notes

- Replace the `create_vps` function with your actual VPS deployment logic (e.g., using QEMU, VirtualBox, or another virtualization tool).
- Ensure the bot has the necessary permissions to read messages and manage roles in your Discord server.
- Test the script thoroughly before deploying it in a production environment.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy deploying VPS instances with ease using the **Discord VPS Deployer**! 🚀
