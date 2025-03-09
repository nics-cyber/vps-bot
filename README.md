

---

# Discord VPS Deployer Bot

A Discord bot that allows users to deploy fake VPS instances and manage Docker containers directly from Discord. The bot simulates VPS deployment and provides fake `neofetch` outputs, SSH connections, and Docker container management.

---

## **Features**
1. **Fake VPS Deployment**:
   - Simulates the deployment of a VPS with custom RAM, CPU, and OS.
   - Generates a fake `neofetch` output to display system information.
   - Provides a fake SSH connection string.
   - Supports customizable duration for automatic deletion.

2. **Docker Container Management**:
   - Deploy, list, stop, and delete Docker containers.
   - Supports any Docker image available on Docker Hub.

3. **Role-Based Access Control**:
   - Restricts commands to specific roles and channels.

---

## **Supported Operating Systems**
The bot supports the following operating systems for fake VPS deployment:

| OS Name       | Display Name      |
|---------------|-------------------|
| `ubuntu`      | Ubuntu            |
| `debian`      | Debian            |
| `centos`      | CentOS            |
| `fedora`      | Fedora            |
| `arch`        | Arch Linux        |
| `alpine`      | Alpine Linux      |
| `kali`        | Kali Linux        |
| `opensuse`    | openSUSE          |
| `rocky`       | Rocky Linux       |
| `freebsd`     | FreeBSD           |
| `gentoo`      | Gentoo            |
| `manjaro`     | Manjaro           |
| `mint`        | Linux Mint        |
| `popos`       | Pop!_OS           |
| `zorin`       | Zorin OS          |
| `elementary`  | elementary OS     |
| `deepin`      | Deepin            |
| `mxlinux`     | MX Linux          |
| `slackware`   | Slackware         |
| `void`        | Void Linux        |
| `nixos`       | NixOS             |
| `clear`       | Clear Linux       |
| `tails`       | Tails             |
| `parrot`      | Parrot OS         |
| `blackarch`   | BlackArch         |
| `qubes`       | Qubes OS          |
| `reactos`     | ReactOS           |
| `haiku`       | Haiku             |
| `solus`       | Solus             |
| `puppy`       | Puppy Linux       |
| `tinycore`    | Tiny Core Linux   |
| `antix`       | antiX             |
| `bodhi`       | Bodhi Linux       |
| `peppermint`  | Peppermint OS     |
| `lubuntu`     | Lubuntu           |
| `kubuntu`     | Kubuntu           |
| `xubuntu`     | Xubuntu           |
| `ubuntu-budgie` | Ubuntu Budgie   |
| `ubuntu-mate` | Ubuntu MATE       |
| `ubuntu-studio` | Ubuntu Studio   |
| `edubuntu`    | Edubuntu          |
| `kali-live`   | Kali Linux (Live) |
| `kali-light`  | Kali Linux (Light)|
| `kali-everything` | Kali Linux (Everything) |

---

## **Prerequisites**
1. **Python 3.8+**:
   - Ensure Python 3.8 or later is installed.

2. **Docker**:
   - Install Docker on your system:
     ```bash
     sudo apt update
     sudo apt install docker.io
     sudo systemctl start docker
     sudo systemctl enable docker
     ```

3. **Discord Bot Token**:
   - Create a Discord bot and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications).

---

## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nics-cyber/vps-bot.git
   cd discord-vps-deployer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Bot**:
   - Open the script and replace the following placeholders:
     - `ALLOWED_CHANNEL_IDS`: Add the IDs of the channels where the bot is allowed to operate.
     - `ALLOWED_ROLE_IDS`: Add the IDs of the roles that can use the bot.
     - `TOKEN`: Replace with your Discord bot token.

4. **Run the Bot**:
   ```bash
   python3 discord_vps_deployer.py
   ```

---

## **Commands**
### **VPS Deployment**
- **`/deploy <os_name> <ram> <cpu> [duration]`**:
  - Deploys a fake VPS with the specified OS, RAM, and CPU.
  - The `duration` parameter specifies how long the VPS will run before being deleted (in seconds). If not provided, the VPS will not be automatically deleted.
  - Example: `/deploy ubuntu 2048 2 3600` deploys an Ubuntu VPS with 2GB RAM and 2 CPU cores, which will be deleted after 1 hour.

- **`/status <vps_id>`**:
  - Checks the status of a VPS instance.
  - Example: `/status 1` checks the status of VPS with ID 1.

### **Docker Management**
- **`/docker run <image_name>`**:
  - Deploys a Docker container from the specified image.
  - Example: `/docker run ubuntu` deploys an Ubuntu container.

- **`/docker ps`**:
  - Lists all running Docker containers.

- **`/docker stop <container_id>`**:
  - Stops a running container.
  - Example: `/docker stop abc123` stops the container with ID `abc123`.

- **`/docker rm <container_id>`**:
  - Deletes a container.
  - Example: `/docker rm abc123` deletes the container with ID `abc123`.

---

## **Examples**
1. **Deploy a Fake VPS for 1 Hour**:
   ```
   /deploy ubuntu 2048 2 3600
   ```
   - Deploys an Ubuntu VPS with 2GB RAM and 2 CPU cores, which will be deleted after 1 hour.

2. **Deploy a Fake VPS for 30 Minutes**:
   ```
   /deploy debian 4096 4 1800
   ```
   - Deploys a Debian VPS with 4GB RAM and 4 CPU cores, which will be deleted after 30 minutes.

3. **Deploy a Docker Container**:
   ```
   /docker run nginx
   ```
   - Deploys an Nginx container.

4. **List Running Containers**:
   ```
   /docker ps
   ```

5. **Stop a Container**:
   ```
   /docker stop abc123
   ```

6. **Delete a Container**:
   ```
   /docker rm abc123
   ```

---

## **Security**
- **Role-Based Access Control**:
  - Restrict bot commands to specific roles and channels by configuring `ALLOWED_CHANNEL_IDS` and `ALLOWED_ROLE_IDS`.

- **Docker Permissions**:
  - Ensure only trusted users have access to Docker commands, as they can manipulate containers and potentially affect the host system.

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
