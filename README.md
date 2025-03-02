Here’s a comprehensive **README.md** for your VPS management script. It explains the supported OS, installation steps, usage instructions, features, and more.

---

# VPS Management Script

This script allows you to create and manage VPS-like environments using `tmux` and `tmate`. It is designed to work without Docker or systemd, making it lightweight and easy to use. Admins can create VPS instances, choose the OS, and send `tmate` SSH connection strings to specific users via Discord DM.

---

## **Features**

- **OS Selection**: Choose from supported operating systems (Ubuntu, Debian, CentOS).
- **Admin-Only Commands**: Only users with the admin role can create VPS instances.
- **Discord Integration**: Send `tmate` SSH connection strings to users via DM.
- **No Docker or Systemd**: Uses `tmux` and `tmate` for session management.
- **Lightweight**: No heavy dependencies or complex setup required.

---

## **Supported Operating Systems**

The script supports the following operating systems:

- **Ubuntu**
- **Debian**
- **CentOS**

You can easily extend the script to support more OS options by modifying the `SUPPORTED_OS` array.

---

## **Installation**

### **Prerequisites**

1. **Server Requirements**:
   - A Linux-based server (e.g., Ubuntu, Debian, CentOS).
   - `tmux` and `tmate` installed.

2. **Discord Bot**:
   - Create a Discord bot and get its token from the [Discord Developer Portal](https://discord.com/developers/applications).
   - Ensure the bot has the following permissions:
     - Read Messages
     - Send Messages
     - Direct Messages

### **Install Dependencies**

1. Install `tmux` and `tmate`:
   ```bash
   sudo apt update
   sudo apt install tmux tmate
   ```

2. Install `curl` (for sending Discord messages):
   ```bash
   sudo apt install curl
   ```

---

## **Setup**

1. **Download the Script**:
   - Save the script as `vps-manager.sh`:
     ```bash
     wget https://example.com/vps-manager.sh
     ```

2. **Make the Script Executable**:
   ```bash
   chmod +x vps-manager.sh
   ```

3. **Configure the Script**:
   - Open the script in a text editor:
     ```bash
     nano vps-manager.sh
     ```
   - Update the following variables:
     ```bash
     DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"
     ADMIN_ROLE_ID="ADMIN_ROLE_ID"  # Replace with your admin role ID
     ```

4. **Run the Script**:
   ```bash
   ./vps-manager.sh
   ```

---

## **Usage**

### **Commands**

| Command               | Description                                                                 | Permissions       |
|-----------------------|-----------------------------------------------------------------------------|-------------------|
| `!create-vps <os> <user_id>` | Creates a VPS with the specified OS and DMs the user with `tmate` info. | Admins only       |

### **Examples**

1. **Create a VPS with Ubuntu**:
   ```
   !create-vps ubuntu 123456789012345678
   ```

2. **Create a VPS with Debian**:
   ```
   !create-vps debian 123456789012345678
   ```

3. **Create a VPS with CentOS**:
   ```
   !create-vps centos 123456789012345678
   ```

---

## **How It Works**

1. **Admin Command**:
   - Admins use the command `!create-vps <os> <user_id>` to create a VPS.

2. **OS Selection**:
   - The script validates the OS choice (e.g., `ubuntu`, `debian`, `centos`).

3. **VPS Creation**:
   - The script starts a `tmux` session with `tmate` and captures the SSH connection string.

4. **DM User**:
   - The script sends the SSH connection string to the specified user via Discord DM.

---

## **Security Considerations**

1. **Role-Based Access**:
   - Only users with the admin role can create VPS instances.

2. **Input Validation**:
   - The script validates the OS choice and user ID to prevent errors.

3. **Logging**:
   - Log all activities for auditing purposes.

4. **Environment Isolation**:
   - Run the script in a restricted environment to limit access to the host system.

---

## **Extending the Script**

### **Add More OS Options**

To add more OS options, update the `SUPPORTED_OS` array in the script:

```bash
SUPPORTED_OS=("ubuntu" "debian" "centos" "alpine" "fedora")
```

### **Customize Discord Messages**

You can customize the Discord message by modifying the `send_discord_message` function:

```bash
send_discord_message() {
    local user_id=$1
    local message=$2

    curl -s -X POST \
        -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"content\":\"$message\"}" \
        "https://discord.com/api/v9/users/$user_id/channels" > /dev/null
}
```

---

## **Troubleshooting**

### **Common Issues**

1. **`tmux` or `tmate` not installed**:
   - Ensure `tmux` and `tmate` are installed and available in your system's PATH.

2. **Discord DM not working**:
   - Ensure the bot has the necessary permissions to send DMs.
   - Check the Discord bot token for errors.

3. **Failed to capture `tmate` SSH string**:
   - Ensure the `tmux` session is running and `tmate` is properly configured.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request.

---

## **Support**

For support, please open an issue on the [GitHub repository](https://github.com/your-repo/vps-manager).

---

Let me know if you need further assistance!
