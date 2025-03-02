#!/bin/bash

# Configuration
DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"
ADMIN_ROLE_ID="ADMIN_ROLE_ID"  # Replace with your admin role ID
PREFIX="!"  # Command prefix
SUPPORTED_OS=("ubuntu" "debian" "centos")  # Supported OS options

# Function to start a VPS with tmate
start_vps() {
    local os=$1
    local user_id=$2

    # Validate OS choice
    if [[ ! " ${SUPPORTED_OS[@]} " =~ " ${os} " ]]; then
        echo "Unsupported OS. Choose from: ${SUPPORTED_OS[*]}"
        return 1
    fi

    # Start a tmux session with tmate
    tmux new -s "vps-${os}-${user_id}" -d "tmate -F"
    if [ $? -ne 0 ]; then
        echo "Failed to start tmux session."
        return 1
    fi

    # Capture tmate SSH connection string
    local tmate_info=$(tmux capture-pane -p -t "vps-${os}-${user_id}" | grep ssh)
    if [ -z "$tmate_info" ]; then
        echo "Failed to capture tmate SSH connection string."
        return 1
    fi

    echo "$tmate_info"
    return 0
}

# Function to send a Discord message
send_discord_message() {
    local user_id=$1
    local message=$2

    curl -s -X POST \
        -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"content\":\"$message\"}" \
        "https://discord.com/api/v9/users/$user_id/channels" > /dev/null
}

# Main script logic
while true; do
    echo "Waiting for commands..."
    read -r command

    if [[ "$command" == "${PREFIX}create-vps"* ]]; then
        # Parse command arguments
        args=($command)
        os=${args[1]}
        user_id=${args[2]}

        if [ -z "$os" ] || [ -z "$user_id" ]; then
            echo "Usage: ${PREFIX}create-vps <os> <user_id>"
            continue
        fi

        # Check if the user has admin role (simplified for script)
        # In a real bot, you would use Discord's API to check roles
        echo "Assuming user has admin role for simplicity."

        # Start the VPS and capture tmate info
        tmate_info=$(start_vps "$os" "$user_id")
        if [ $? -eq 0 ]; then
            # Send tmate info to the user via DM
            send_discord_message "$user_id" "Your VPS is ready! Connect using:\n\`\`\`$tmate_info\`\`\`"
            echo "VPS created with OS: $os. tmate info sent to user: $user_id."
        else
            echo "Failed to create VPS."
        fi
    else
        echo "Unknown command. Available commands: ${PREFIX}create-vps <os> <user_id>"
    fi
done
