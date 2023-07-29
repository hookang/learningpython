#!/usr/bin/env python3

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file_path, title, paragraph):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['Title'])
    report_paragraph = Paragraph(paragraph, styles['Normal'])
    empty_line = Spacer(1, 20)
    report_content = [report_title, empty_line, report_paragraph, empty_line]
    doc.build(report_content)


student-01-79c6ce800f3c@linux-instance:~$ cat reports.py
#!/usr/bin/env python3

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file_path, title, paragraph):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['Title'])
    report_paragraph = Paragraph(paragraph, styles['Normal'])
    empty_line = Spacer(1, 20)
    report_content = [report_title, empty_line, report_paragraph, empty_line]
    doc.build(report_content)
