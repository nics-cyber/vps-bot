import os
import subprocess
import discord
from discord.ext import commands

# Configuration
ALLOWED_CHANNEL_IDS = [123456789012345678]  # Replace with your allowed channel IDs
ALLOWED_ROLE_IDS = [987654321098765432]     # Replace with your allowed role IDs
TOKEN = "YOUR_DISCORD_BOT_TOKEN"            # Replace with your Discord bot token

# Supported OS options
SUPPORTED_OS = {
    "ubuntu": "https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso",
    "debian": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso",
    "centos": "http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso",
    "fedora": "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Server/x86_64/iso/Fedora-Server-dvd-x86_64-38-1.6.iso",
    "arch": "https://mirror.rackspace.com/archlinux/iso/2023.10.14/archlinux-2023.10.14-x86_64.iso",
    "alpine": "https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-virt-3.18.4-x86_64.iso",
    "kali": "https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso",
    "opensuse": "https://download.opensuse.org/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64.iso",
    "rocky": "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.2-x86_64-dvd.iso",
    "freebsd": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-dvd1.iso"
}

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

def create_vps(os_name: str, ram: int, cpu: int):
    """
    Function to create a VPS with the specified OS, RAM, and CPU.
    Uses FreeRoot to customize the OS.
    """
    print(f"Creating VPS with OS: {os_name}, RAM: {ram}MB, CPU: {cpu} cores")

    # Step 1: Download the OS image
    os_url = SUPPORTED_OS.get(os_name)
    if not os_url:
        raise ValueError(f"Unsupported OS: {os_name}")

    os_image = f"/tmp/{os_name}.iso"
    if not os.path.exists(os_image):
        print(f"Downloading OS image: {os_url}")
        subprocess.run(["wget", "-O", os_image, os_url], check=True)

    # Step 2: Use FreeRoot to customize the OS
    print("Customizing OS with FreeRoot...")
    freeroot_repo = "https://github.com/foxytouxxx/freeroot.git"
    freeroot_dir = "/tmp/freeroot"
    if not os.path.exists(freeroot_dir):
        subprocess.run(["git", "clone", freeroot_repo, freeroot_dir], check=True)
    subprocess.run(["python3", f"{freeroot_dir}/freeroot.py", "--image", os_image], check=True)

    # Step 3: Deploy the VPS using QEMU (replace with your preferred tool)
    print("Deploying VPS...")
    command = [
        "qemu-system-x86_64",
        "-m", str(ram),
        "-smp", str(cpu),
        "-cdrom", os_image,
        "-boot", "d",
        "-nographic"
    ]
    subprocess.run(command, check=True)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command(name="deploy")
async def deploy_vps(ctx, os_name: str, ram: int, cpu: int):
    """
    Discord command to deploy a VPS.
    Only allowed in specific channels and for specific roles.
    """
    # Check if the command is used in an allowed channel
    if ctx.channel.id not in ALLOWED_CHANNEL_IDS:
        await ctx.send("❌ This command is not allowed in this channel.")
        return

    # Check if the user has an allowed role
    if not any(role.id in ALLOWED_ROLE_IDS for role in ctx.author.roles):
        await ctx.send("❌ You do not have permission to use this command.")
        return

    # Validate OS
    if os_name not in SUPPORTED_OS:
        await ctx.send(f"❌ Unsupported OS. Available options: {', '.join(SUPPORTED_OS.keys())}")
        return

    # Validate RAM and CPU
    if ram < 512 or ram > 16384:
        await ctx.send("❌ Invalid RAM amount. Please specify a value between 512 and 16384 MB.")
        return
    if cpu < 1 or cpu > 16:
        await ctx.send("❌ Invalid CPU count. Please specify a value between 1 and 16 cores.")
        return

    # Deploy the VPS
    await ctx.send(f"🚀 Deploying VPS with OS: {os_name}, RAM: {ram}MB, CPU: {cpu} cores...")
    try:
        create_vps(os_name, ram, cpu)
        await ctx.send("✅ VPS deployed successfully!")
    except Exception as e:
        await ctx.send(f"❌ Failed to deploy VPS: {e}")

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
