#!/usr/bin/env python3
"""
Job Application Tracker Viewer
View and manage your job application history
"""

import os
import csv
from datetime import datetime

def view_applications():
    """Display all job applications from CSV"""
    csv_file = "../job_applications.csv"
    
    if not os.path.exists(csv_file):
        print("📄 No applications tracked yet.")
        print("Applications will be automatically logged when you create PDFs.")
        return
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            applications = list(reader)
        
        if not applications:
            print("📄 No applications found in tracking file.")
            return
        
        print("📊 JOB APPLICATION TRACKER")
        print("=" * 60)
        
        for i, app in enumerate(applications, 1):
            print(f"\\n{i}. {app['Company']} - {app['Position']}")
            print(f"   📅 Date: {app['Date']} at {app['Time']}")
            print(f"   📄 Files: {app['Resume_File']} → {app['PDF_File']}")
            print(f"   📈 Status: {app['Status']}")
            if app['Notes']:
                print(f"   📝 Notes: {app['Notes']}")
        
        print(f"\\n📊 Total Applications: {len(applications)}")
        
        # Show recent activity
        recent = [app for app in applications if app['Date'] == datetime.now().strftime("%Y-%m-%d")]
        if recent:
            print(f"📅 Today's Activity: {len(recent)} applications")
        
    except Exception as e:
        print(f"❌ Error reading applications: {e}")

def add_manual_entry():
    """Add a manual application entry"""
    csv_file = "job_applications.csv"
    
    print("\\n➕ ADD MANUAL APPLICATION ENTRY")
    print("-" * 35)
    
    company = input("Company: ").strip()
    position = input("Position: ").strip()
    status = input("Status (Applied/Interview/etc): ").strip() or "Applied"
    notes = input("Notes (optional): ").strip()
    
    if not company or not position:
        print("❌ Company and Position are required")
        return
    
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    row_data = [
        date_str,
        time_str,
        company,
        position,
        "Manual Entry",
        "Manual Entry",
        status,
        notes
    ]
    
    try:
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            if not file_exists:
                headers = ["Date", "Time", "Company", "Position", "Resume_File", "PDF_File", "Status", "Notes"]
                writer.writerow(headers)
            
            writer.writerow(row_data)
        
        print(f"✅ Added {company} - {position} to tracking")
        
    except Exception as e:
        print(f"❌ Error adding entry: {e}")

def show_stats():
    """Show application statistics"""
    csv_file = "job_applications.csv"
    
    if not os.path.exists(csv_file):
        print("📄 No application data available.")
        return
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            applications = list(reader)
        
        print("\\n📈 APPLICATION STATISTICS")
        print("=" * 30)
        
        # Count by company
        companies = {}
        statuses = {}
        
        for app in applications:
            company = app['Company']
            status = app['Status']
            
            companies[company] = companies.get(company, 0) + 1
            statuses[status] = statuses.get(status, 0) + 1
        
        print(f"Total Applications: {len(applications)}")
        print(f"Unique Companies: {len(companies)}")
        
        print("\\n🏢 By Company:")
        for company, count in sorted(companies.items()):
            print(f"   {company}: {count}")
        
        print("\\n📊 By Status:")
        for status, count in sorted(statuses.items()):
            print(f"   {status}: {count}")
        
    except Exception as e:
        print(f"❌ Error generating stats: {e}")

def main():
    """Main menu"""
    while True:
        print("\\n🎯 JOB APPLICATION TRACKER")
        print("=" * 30)
        print("1. View All Applications")
        print("2. Add Manual Entry")
        print("3. Show Statistics")
        print("4. Exit")
        
        choice = input("\\nChoose option (1-4): ").strip()
        
        if choice == "1":
            view_applications()
        elif choice == "2":
            add_manual_entry()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()