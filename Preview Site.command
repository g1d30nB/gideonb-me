#!/bin/bash
# Opens your website in a local preview server
# Just double-click this file in Finder!

cd "$(dirname "$0")"
echo ""
echo "  Starting local preview server..."
echo "  Your site will open in your browser."
echo ""
echo "  To stop: close this window or press Ctrl+C"
echo ""

# Open browser after a short delay
(sleep 1 && open "http://localhost:8000") &

# Start server
python3 -m http.server 8000
