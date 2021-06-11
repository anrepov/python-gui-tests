import os

import comtypes.client as client

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = client.CreateObject("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range["A%s" % (i + 1)].Value[()] = "group %s" % i

wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()
