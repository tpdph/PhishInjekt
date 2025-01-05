import sqlite3
import yaml

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def get_reports(report_type=None):
    try:
        conn = sqlite3.connect(config['database']['path'])
        cursor = conn.cursor()
        if report_type:
            cursor.execute("SELECT * FROM reports WHERE report_type = ?", (report_type,))
        else:
            cursor.execute("SELECT * FROM reports")
        reports = cursor.fetchall()
        conn.close()
        return reports
    except Exception as e:
        print(f"Error fetching reports from database: {e}")
        return None

def generate_summary_report():
    reports = get_reports()
    if reports:
        report_counts = {}
        for report in reports:
            report_type = report[1]
            report_counts[report_type] = report_counts.get(report_type, 0) + 1
        print("Report Summary:")
        for report_type, count in report_counts.items():
            print(f"- {report_type}: {count}")
    else:
        print("No reports found.")

if __name__ == '__main__':
    generate_summary_report()
