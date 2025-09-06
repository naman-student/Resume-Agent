#!/usr/bin/env python3
"""
Local Dashboard Server
Serves the job dashboard on localhost to avoid CORS issues
"""
import http.server
import socketserver
import webbrowser
import os
import time
from threading import Timer

def open_browser():
    """Open browser after a short delay"""
    webbrowser.open('http://localhost:8000/job_dashboard.html')

def start_server():
    """Start local server for dashboard"""
    PORT = 8000
    
    # Change to the parent directory (project root)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🌐 Starting local server at http://localhost:{PORT}")
            print(f"📊 Dashboard URL: http://localhost:{PORT}/job_dashboard.html")
            print("🔄 Server will auto-refresh dashboard data")
            print("Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Open browser after 2 seconds
            Timer(2.0, open_browser).start()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use. Try closing other servers or use a different port.")
        else:
            print(f"❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🚀 Job Applications Dashboard Server")
    print("This will serve your dashboard locally to avoid CORS issues")
    print()
    
    start_server()

if __name__ == "__main__":
    main()