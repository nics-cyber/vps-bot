import os
import subprocess
import asyncio
import discord
from discord.ext import commands

# Configuration
ALLOWED_CHANNEL_IDS = [123456789012345678]  # Replace with your allowed channel IDs
ALLOWED_ROLE_IDS = [987654321098765432]     # Replace with your allowed role IDs
TOKEN = "YOUR_DISCORD_BOT_TOKEN"            # Replace with your Discord bot token

# Supported OS options (40 operating systems)
SUPPORTED_OS = {
    # Original 10 OS
    "ubuntu": "https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso",
    "debian": "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso",
    "centos": "http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso",
    "fedora": "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Server/x86_64/iso/Fedora-Server-dvd-x86_64-38-1.6.iso",
    "arch": "https://mirror.rackspace.com/archlinux/iso/2023.10.14/archlinux-2023.10.14-x86_64.iso",
    "alpine": "https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-virt-3.18.4-x86_64.iso",
    "kali": "https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso",
    "opensuse": "https://download.opensuse.org/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64.iso",
    "rocky": "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.2-x86_64-dvd.iso",
    "freebsd": "https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-dvd1.iso",

    # Additional 30 OS
    "gentoo": "https://bouncer.gentoo.org/fetch/root/all/releases/amd64/autobuilds/20231008T170153Z/livegui-amd64-20231008T170153Z.iso",
    "manjaro": "https://download.manjaro.org/kde/22.1.0/manjaro-kde-22.1.0-230529-linux61.iso",
    "mint": "https://mirrors.edge.kernel.org/linuxmint/iso/stable/21.2/linuxmint-21.2-cinnamon-64bit.iso",
    "popos": "https://pop-iso.sfo2.cdn.digitaloceanspaces.com/22.04/amd64/intel/7/pop-os_22.04_amd64_intel_7.iso",
    "zorin": "https://mirrors.edge.kernel.org/zorinos-isos/16/Zorin-OS-16.2-Core-64-bit.iso",
    "elementary": "https://ams3.dl.elementary.io/download/MTY2NzI2NzI2OA==/elementaryos-7.0-stable.20230308.iso",
    "deepin": "https://cdimage.deepin.com/releases/23/Deepin-23-Beta2-amd64.iso",
    "mxlinux": "https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-23_x64.iso/download",
    "slackware": "https://mirrors.slackware.com/slackware/slackware64-15.0/iso/slackware64-15.0-install-dvd.iso",
    "void": "https://alpha.de.repo.voidlinux.org/live/current/void-live-x86_64-20230628.iso",
    "nixos": "https://channels.nixos.org/nixos-23.05/latest-nixos-plasma5-x86_64-linux.iso",
    "clear": "https://cdn.download.clearlinux.org/releases/38510/clear/clear-38510-live.iso",
    "tails": "https://tails.boum.org/install/vm/Tails.amd64.5.18.1-0.img",
    "parrot": "https://deb.parrot.sh/parrot/iso/5.3/Parrot-security-5.3_amd64.iso",
    "blackarch": "https://ftp.halifax.rwth-aachen.de/blackarch/iso/blackarch-linux-full-2023.09.01-x86_64.iso",
    "qubes": "https://mirrors.edge.kernel.org/qubes/iso/Qubes-R4.1.2-x86_64.iso",
    "reactos": "https://sourceforge.net/projects/reactos/files/ReactOS/0.4.15/ReactOS-0.4.15-iso.zip/download",
    "haiku": "https://download.haiku-os.org/nightly-images/x86_64/haiku-nightly-hrev57681-x86_64-anyboot.zip",
    "solus": "https://downloads.getsol.us/4.4/Solus-4.4-Budgie.iso",
    "puppy": "https://distro.ibiblio.org/puppylinux/puppy-fossa/fossapup64-9.5.iso",
    "tinycore": "http://tinycorelinux.net/13.x/x86_64/release/TinyCorePure64-13.0.iso",
    "antix": "https://sourceforge.net/projects/antix-linux/files/Final/antiX-23/antiX-23_x64-full.iso/download",
    "bodhi": "https://sourceforge.net/projects/bodhilinux/files/7.0.0/bodhi-7.0.0-64.iso/download",
    "peppermint": "https://peppermintos.com/iso/Peppermint-11-20230703-amd64.iso",
    "lubuntu": "https://cdimage.ubuntu.com/lubuntu/releases/22.04/release/lubuntu-22.04.3-desktop-amd64.iso",
    "kubuntu": "https://cdimage.ubuntu.com/kubuntu/releases/22.04/release/kubuntu-22.04.3-desktop-amd64.iso",
    "xubuntu": "https://cdimage.ubuntu.com/xubuntu/releases/22.04/release/xubuntu-22.04.3-desktop-amd64.iso",
    "ubuntu-budgie": "https://cdimage.ubuntu.com/ubuntu-budgie/releases/22.04/release/ubuntu-budgie-22.04.3-desktop-amd64.iso",
    "ubuntu-mate": "https://cdimage.ubuntu.com/ubuntu-mate/releases/22.04/release/ubuntu-mate-22.04.3-desktop-amd64.iso",
    "ubuntu-studio": "https://cdimage.ubuntu.com/ubuntustudio/releases/22.04/release/ubuntustudio-22.04.3-dvd-amd64.iso",
    "edubuntu": "https://cdimage.ubuntu.com/edubuntu/releases/22.04/release/edubuntu-22.04.3-desktop-amd64.iso",
    "kali-live": "https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-live-amd64.iso",
    "kali-light": "https://cdimage.kali.org/kali-2023.3/kali-linux-light-2023.3-amd64.iso",
    "kali-everything": "https://cdimage.kali.org/kali-2023.3/kali-linux-everything-2023.3-amd64.iso",
}

# Track VPS instances
vps_instances = {}

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

    # Run FreeRoot to customize the OS image
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
    process = subprocess.Popen(command)
    return process

def generate_tmate_session():
    """
    Function to generate a tmate SSH session.
    Returns the SSH connection string.
    """
    print("Generating tmate session...")
    # Install tmate if not already installed
    if not os.path.exists("/usr/bin/tmate"):
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "tmate"], check=True)

    # Start tmate and get the SSH connection string
    result = subprocess.run(["tmate", "-S", "/tmp/tmate.sock", "new-session", "-d"], capture_output=True, text=True, check=True)
    subprocess.run(["tmate", "-S", "/tmp/tmate.sock", "wait", "tmate-ready"], check=True)
    result = subprocess.run(["tmate", "-S", "/tmp/tmate.sock", "display", "-p", "#{tmate_ssh}"], capture_output=True, text=True, check=True)
    ssh_connection = result.stdout.strip()
    return ssh_connection

def adjust_poweredge_resources(ram: int, cpu: int):
    """
    Function to adjust Free PowerEdge resources (RAM and CPU) based on VPS requirements.
    """
    print(f"Adjusting Free PowerEdge resources: RAM={ram}MB, CPU={cpu} cores")
    # Replace this with your actual Free PowerEdge resource adjustment logic
    subprocess.run(["sudo", "poweredge-adjust", "--ram", str(ram), "--cpu", str(cpu)], check=True)

async def cleanup_vps(vps_id: int, timeout: int):
    """
    Function to automatically delete a VPS after a specified timeout.
    """
    await asyncio.sleep(timeout)
    if vps_id in vps_instances:
        vps_instances[vps_id].terminate()
        del vps_instances[vps_id]
        print(f"VPS {vps_id} has been deleted.")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command(name="deploy")
async def deploy_vps(ctx, os_name: str, ram: int, cpu: int, timeout: int = None):
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

    # Adjust Free PowerEdge resources
    try:
        adjust_poweredge_resources(ram, cpu)
    except Exception as e:
        await ctx.send(f"❌ Failed to adjust Free PowerEdge resources: {e}")
        return

    # Deploy the VPS
    await ctx.send(f"🚀 Deploying VPS with OS: {os_name}, RAM: {ram}MB, CPU: {cpu} cores...")
    try:
        process = create_vps(os_name, ram, cpu)
        vps_id = len(vps_instances) + 1
        vps_instances[vps_id] = process
        await ctx.send(f"✅ VPS deployed successfully! VPS ID: {vps_id}")

        # Generate tmate SSH session
        ssh_connection = generate_tmate_session()
        await ctx.author.send(f"🔑 Your VPS SSH connection:\n```{ssh_connection}```")
        await ctx.send("📩 Check your DMs for the SSH connection details!")

        # Schedule cleanup if timeout is specified
        if timeout:
            asyncio.create_task(cleanup_vps(vps_id, timeout))
            await ctx.send(f"⏳ VPS {vps_id} will be deleted in {timeout} seconds.")
    except Exception as e:
        await ctx.send(f"❌ Failed to deploy VPS: {e}")

@bot.command(name="status")
async def vps_status(ctx, vps_id: int):
    """
    Discord command to check the status of a VPS.
    """
    if vps_id not in vps_instances:
        await ctx.send(f"❌ VPS {vps_id} not found.")
        return

    process = vps_instances[vps_id]
    if process.poll() is None:
        await ctx.send(f"✅ VPS {vps_id} is running.")
    else:
        await ctx.send(f"❌ VPS {vps_id} is not running.")

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
