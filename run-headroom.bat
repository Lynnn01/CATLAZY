@echo off
echo Starting Headroom Proxy on port 8787...
echo You can connect your AI clients to http://localhost:8787
echo.
docker run -p 8787:8787 ghcr.io/chopratejas/headroom
pause
