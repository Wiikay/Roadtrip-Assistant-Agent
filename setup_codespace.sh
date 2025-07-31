#!/bin/bash

echo "🚀 Setting up Road Trip Assistant in Codespace..."
echo "=================================================="

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Install Node.js MCP server
echo "🌐 Installing Google Maps MCP server..."
npm install -g @modelcontextprotocol/server-google-maps

# Check if API keys are set
echo ""
echo "🔑 Checking API keys..."
if [ -z "$GOOGLE_MAPS_API_KEY" ]; then
    echo "⚠️  GOOGLE_MAPS_API_KEY not set"
    echo "   Set it with: export GOOGLE_MAPS_API_KEY='your_actual_key'"
else
    echo "✅ GOOGLE_MAPS_API_KEY is set"
fi

if [ -z "$WEATHER_API_KEY" ]; then
    echo "⚠️  WEATHER_API_KEY not set"
    echo "   Set it with: export WEATHER_API_KEY='your_actual_key'"
    echo "   Get free API key from: https://www.weatherapi.com/"
else
    echo "✅ WEATHER_API_KEY is set"
fi

# Set Python path
echo ""
echo "🐍 Setting Python path..."
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
echo "PYTHONPATH set to include project directory"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your API keys (if not already set):"
echo "   export GOOGLE_MAPS_API_KEY='your_key'"
echo "   export WEATHER_API_KEY='your_key'"
echo ""
echo "2. Run the test script:"
echo "   python test_codespace.py"
echo ""
echo "3. Try running the agent (if ADK is available):"
echo "   cd adk_agent_samples/mcp_agent && adk web"