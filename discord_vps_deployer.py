import os
import subprocess
import asyncio
import discord
from discord.ext import commands
import docker  # Docker SDK for Python

# Configuration
ALLOWED_CHANNEL_IDS = [123456789012345678]  # Replace with your allowed channel IDs
ALLOWED_ROLE_IDS = [987654321098765432]     # Replace with your allowed role IDs
TOKEN = "YOUR_DISCORD_BOT_TOKEN"            # Replace with your Discord bot token

# Initialize Docker client
docker_client = docker.from_env()

# Track VPS instances and Docker containers
vps_instances = {}
docker_containers = {}

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

def generate_neofetch(os_name: str, ram: int, cpu: int):
    """
    Generates a neofetch output with a dynamic OS image based on the selected OS.
    """
    os_display_names = {
        "ubuntu": "Ubuntu",
        "debian": "Debian",
        "centos": "CentOS",
        "fedora": "Fedora",
        "arch": "Arch Linux",
        "alpine": "Alpine Linux",
        "kali": "Kali Linux",
        "opensuse": "openSUSE",
        "rocky": "Rocky Linux",
        "freebsd": "FreeBSD",
        "gentoo": "Gentoo",
        "manjaro": "Manjaro",
        "mint": "Linux Mint",
        "popos": "Pop!_OS",
        "zorin": "Zorin OS",
        "elementary": "elementary OS",
        "deepin": "Deepin",
        "mxlinux": "MX Linux",
        "slackware": "Slackware",
        "void": "Void Linux",
        "nixos": "NixOS",
        "clear": "Clear Linux",
        "tails": "Tails",
        "parrot": "Parrot OS",
        "blackarch": "BlackArch",
        "qubes": "Qubes OS",
        "reactos": "ReactOS",
        "haiku": "Haiku",
        "solus": "Solus",
        "puppy": "Puppy Linux",
        "tinycore": "Tiny Core Linux",
        "antix": "antiX",
        "bodhi": "Bodhi Linux",
        "peppermint": "Peppermint OS",
        "lubuntu": "Lubuntu",
        "kubuntu": "Kubuntu",
        "xubuntu": "Xubuntu",
        "ubuntu-budgie": "Ubuntu Budgie",
        "ubuntu-mate": "Ubuntu MATE",
        "ubuntu-studio": "Ubuntu Studio",
        "edubuntu": "Edubuntu",
        "kali-live": "Kali Linux (Live)",
        "kali-light": "Kali Linux (Light)",
        "kali-everything": "Kali Linux (Everything)",
    }
    os_display_name = os_display_names.get(os_name, "Linux OS")

    neofetch_output = f"""
    OS: {os_display_name} (Fresh Install)
    Host: VPS-01
    Kernel: 5.15.0-83-generic
    Uptime: 0 min
    Packages: 0 (dpkg), 0 (rpm)
    Shell: bash 5.1.16
    Resolution: 1024x768
    DE: None
    WM: None
    WM Theme: None
    Theme: None
    Icons: None
    Terminal: None
    CPU: Virtual CPU ({cpu} cores)
    GPU: None
    Memory: {ram}MB / {ram}MB
    Disk: 10GB / 10GB (100% free)
    """
    return neofetch_output

def generate_ssh():
    """
    Generates an SSH connection string.
    """
    ssh_connection = "ssh user@vps.example.com -p 22"
    return ssh_connection

async def cleanup_vps(vps_id: int, duration: int):
    """
    Function to automatically delete a VPS after a specified duration.
    """
    await asyncio.sleep(duration)
    if vps_id in vps_instances:
        del vps_instances[vps_id]
        print(f"VPS {vps_id} has been deleted.")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command(name="deploy")
async def deploy_vps(ctx, os_name: str, ram: int, cpu: int, duration: int = None):
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

    # Validate duration (if provided)
    if duration is not None and duration < 60:
        await ctx.send("❌ Duration must be at least 60 seconds.")
        return

    # Deploy the VPS
    await ctx.send(f"🚀 Deploying VPS with OS: {os_name}, RAM: {ram}MB, CPU: {cpu} cores...")
    try:
        # Generate neofetch output for the selected OS
        neofetch_output = generate_neofetch(os_name, ram, cpu)
        await ctx.send(f"```{neofetch_output}```")

        # Generate SSH connection
        ssh_connection = generate_ssh()
        await ctx.author.send(f"🔑 Your VPS SSH connection:\n```{ssh_connection}```")
        await ctx.send("📩 Check your DMs for the SSH connection details!")

        # Schedule cleanup if duration is specified
        if duration:
            vps_id = len(vps_instances) + 1
            vps_instances[vps_id] = None  # Placeholder for cleanup
            asyncio.create_task(cleanup_vps(vps_id, duration))
            await ctx.send(f"⏳ VPS {vps_id} will be deleted in {duration} seconds.")
    except Exception as e:
        await ctx.send(f"❌ Failed to deploy VPS: {e}")

@bot.command(name="docker")
async def docker_command(ctx, action: str, *args):
    """
    Discord command to manage Docker containers.
    Supported actions: run, ps, stop, rm
    """
    # Check if the command is used in an allowed channel
    if ctx.channel.id not in ALLOWED_CHANNEL_IDS:
        await ctx.send("❌ This command is not allowed in this channel.")
        return

    # Check if the user has an allowed role
    if not any(role.id in ALLOWED_ROLE_IDS for role in ctx.author.roles):
        await ctx.send("❌ You do not have permission to use this command.")
        return

    # Handle Docker actions
    try:
        if action == "run":
            # Deploy a Docker container
            if len(args) < 1:
                await ctx.send("❌ Usage: /docker run <image_name>")
                return

            image_name = args[0]
            await ctx.send(f"🚀 Deploying Docker container from image: {image_name}...")

            # Run the Docker container
            container = docker_client.containers.run(image_name, detach=True)
            docker_containers[container.id] = container

            await ctx.send(f"✅ Container deployed successfully! Container ID: `{container.id}`")

        elif action == "ps":
            # List running containers
            containers = docker_client.containers.list()
            if not containers:
                await ctx.send("❌ No running containers found.")
                return

            container_list = "\n".join([f"`{c.id}` - {c.name}" for c in containers])
            await ctx.send(f"📦 Running Containers:\n{container_list}")

        elif action == "stop":
            # Stop a running container
            if len(args) < 1:
                await ctx.send("❌ Usage: /docker stop <container_id>")
                return

            container_id = args[0]
            if container_id not in docker_containers:
                await ctx.send(f"❌ Container `{container_id}` not found.")
                return

            container = docker_containers[container_id]
            container.stop()
            await ctx.send(f"🛑 Container `{container_id}` stopped successfully.")

        elif action == "rm":
            # Delete a container
            if len(args) < 1:
                await ctx.send("❌ Usage: /docker rm <container_id>")
                return

            container_id = args[0]
            if container_id not in docker_containers:
                await ctx.send(f"❌ Container `{container_id}` not found.")
                return

            container = docker_containers[container_id]
            container.remove()
            del docker_containers[container_id]
            await ctx.send(f"🗑️ Container `{container_id}` deleted successfully.")

        else:
            await ctx.send("❌ Invalid action. Supported actions: run, ps, stop, rm")

    except Exception as e:
        await ctx.send(f"❌ Failed to execute Docker command: {e}")

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
