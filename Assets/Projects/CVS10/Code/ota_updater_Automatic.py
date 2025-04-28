#!/bin/bash

# Start ngrok and extract public URL
echo "Starting ngrok..."
./ngrok http 5000 > /dev/null &

sleep 5  # wait for ngrok to start

# Extract ngrok public URL
NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-zA-Z.-]*ngrok-free.app' | head -n1)
echo "Ngrok URL: $NGROK_URL"

# Update GitHub webhook dynamically using GitHub API (you need a token)
GITHUB_TOKEN="ota_update_token"
REPO="Manishankarmolleti/ota-firmware"
WEBHOOK_ID="536847108"

echo "Updating GitHub Webhook URL..."
curl -X PATCH \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"config\": {\"url\": \"$NGROK_URL/webhook\", \"content_type\": \"json\"}}" \
  https://api.github.com/repos/$REPO/hooks/$WEBHOOK_ID

# Start Flask Webhook Server
echo "Starting webhook_server.py..."
python3 /home/pi/ota_project/webhook_server.py &

# Start AI OTA Checker
echo "Starting AI OTA Detection..."
python3 /home/pi/ota_project/ai_update_checker.py &
