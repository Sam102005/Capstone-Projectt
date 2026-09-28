"""Regenerates test_data/testdata.xlsx  ->  python test_data/create_excel.py"""
from pathlib import Path
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "TestData"
ws.append(["firstname", "lastname", "email", "telephone",
           "password", "product_name", "update_quantity"])
ws.append(["Test", "Automation", "qa.user_{ts}@example.com", "9876543210",
           "Test@1234", "iPhone", 3])
out = Path(__file__).resolve().parent / "testdata.xlsx"
wb.save(out)
print("Created", out)
