#!/usr/bin/env python3
"""
Dashboard Updater Script
Updates the job_dashboard.html with fresh CSV data to avoid CORS issues
"""
import os
import csv

def update_dashboard_data():
    """Update the dashboard HTML with fresh CSV data"""
    
    csv_file = "../job_applications.csv"
    dashboard_file = "../job_dashboard.html"
    
    if not os.path.exists(csv_file):
        print(f"❌ CSV file not found: {csv_file}")
        return False
    
    if not os.path.exists(dashboard_file):
        print(f"❌ Dashboard file not found: {dashboard_file}")
        return False
    
    # Read CSV data
    csv_content = ""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            csv_content = f.read().strip()
        
        # Fix Windows backslashes for JavaScript compatibility
        csv_content = csv_content.replace('\\', '/')
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return False
    
    # Read dashboard HTML
    dashboard_content = ""
    try:
        with open(dashboard_file, 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
    except Exception as e:
        print(f"❌ Error reading dashboard: {e}")
        return False
    
    # Find and replace the CSV data section
    start_marker = "const csvText = `"
    end_marker = "`;"
    
    start_idx = dashboard_content.find(start_marker)
    if start_idx == -1:
        print("❌ Could not find CSV data section in dashboard")
        return False
    
    start_idx += len(start_marker)
    end_idx = dashboard_content.find(end_marker, start_idx)
    if end_idx == -1:
        print("❌ Could not find end of CSV data section")
        return False
    
    # Replace the CSV data
    new_dashboard = (
        dashboard_content[:start_idx] + 
        csv_content + 
        dashboard_content[end_idx:]
    )
    
    # Write updated dashboard
    try:
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(new_dashboard)
        print("✅ Dashboard updated successfully!")
        return True
    except Exception as e:
        print(f"❌ Error writing dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Updating Job Applications Dashboard...")
    
    if update_dashboard_data():
        print("🎯 Dashboard is now ready to use!")
        print("   Open job_dashboard.html in your browser to view analytics")
    else:
        print("❌ Failed to update dashboard")

if __name__ == "__main__":
    main()