import http.server
import socketserver
import webbrowser
import os
import time
import json
import shutil
import csv
from threading import Timer
from urllib.parse import urlparse, parse_qs

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE = os.path.join(BASE_DIR, "job_applications.csv")
PDF_DIR = os.path.join(BASE_DIR, "Resume", "To_Apply")
APPLIED_DIR = os.path.join(BASE_DIR, "Resume", "Applied")
SKIPPED_DIR = os.path.join(BASE_DIR, "Resume", "Skipped")

def ensure_dirs():
    for d in [APPLIED_DIR, SKIPPED_DIR]:
        os.makedirs(d, exist_ok=True)

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/job_dashboard.html')
            self.end_headers()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            action = self.path.split('/')[-1]
            filename = data.get('filename')
            
            if not filename:
                self.send_response(400)
                self.end_headers()
                return

            success = False
            if action == 'mark_applied':
                success = self.handle_file_move(filename, APPLIED_DIR, "Applied")
            elif action == 'mark_skipped':
                success = self.handle_file_move(filename, SKIPPED_DIR, "Skipped")

            if success:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode('utf-8'))
            else:
                self.send_response(500)
                self.end_headers()
        else:
            super().do_POST()

    def handle_file_move(self, filename, dest_dir, new_status):
        try:
            # 1. Update CSV
            rows = []
            updated = False
            base_filename = os.path.basename(filename)
            
            # Map standard status to V2 Status (Uppercase)
            # "Applied" -> "APPLIED"
            # "Skipped" -> "SKIPPED"
            v2_status = new_status.upper()
            
            if os.path.exists(CSV_FILE):
                with open(CSV_FILE, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    fieldnames = reader.fieldnames
                    for row in reader:
                        # Check match by PDF filename in PDF_Path
                        # row['PDF_Path'] might be "Resume/To_Apply/foo.pdf"
                        if os.path.basename(row['PDF_Path']) == base_filename:
                            row['Status'] = v2_status
                            # Update path in CSV to reflect move
                            # New Path: Resume/Applied/foo.pdf
                            dest_folder_name = os.path.basename(dest_dir)
                            row['PDF_Path'] = f"Resume/{dest_folder_name}/{base_filename}"
                            updated = True
                        rows.append(row)

                if updated:
                    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)
                    print(f"✅ CSV Updated: {base_filename} -> {v2_status}")
            
            # 2. Move File
            src_path = os.path.join(PDF_DIR, base_filename)
            dest_path = os.path.join(dest_dir, base_filename)
            
            if os.path.exists(src_path):
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} -> {dest_path}")
                return True
            else:
                print(f"File not found: {src_path}")
                return updated

        except Exception as e:
            print(f"Error handling file move: {e}")
            return False

def open_browser(port):
    """Open browser after a short delay"""
    webbrowser.open(f'http://localhost:{port}/job_dashboard.html')

def start_server():
    """Start local server for dashboard"""
    ensure_dirs()
    
    # Change to the parent directory (project root)
    project_root = BASE_DIR
    os.chdir(project_root)
    
    # Try ports 8080 to 8090
    for port in range(8080, 8091):
        try:
            # allow_reuse_address allows restarting quickly
            socketserver.TCPServer.allow_reuse_address = True
            
            with socketserver.TCPServer(("", port), DashboardHandler) as httpd:
                print(f"🌐 Starting local server at http://localhost:{port}")
                print(f"📊 Dashboard URL: http://localhost:{port}/job_dashboard.html")
                print("🔄 Server will auto-refresh dashboard data")
                print("Press Ctrl+C to stop the server")
                print("-" * 50)
                
                # Open browser after 2 seconds
                Timer(2.0, lambda: open_browser(port)).start()
                
                httpd.serve_forever()
            break # Exit loop if successful
            
        except OSError as e:
            if "Address already in use" in str(e) or "Only one usage" in str(e):
                print(f"⚠️  Port {port} is in use, trying {port+1}...")
                continue
            else:
                print(f"❌ Error starting server: {e}")
                break
    else:
        print("❌ Could not find an open port between 8080 and 8090.")

def main():
    """Main function"""
    print("🚀 Job Applications Dashboard Server")
    print("This will serve your dashboard locally to avoid CORS issues")
    print()
    
    start_server()

if __name__ == "__main__":
    main()