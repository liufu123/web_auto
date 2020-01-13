import xlrd
import os
class Excel_read():
    def __init__(self,excel_path,excel_name = "Sheet1"):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(excel_name)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range (self.rowNum-1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j = j + 1
            return r

if __name__=="__main__":
    file = "testdata.xlsx"
    report_path = 'E:\liufu-selenium\common'
    file_name = os.path.join(report_path, file)
    a = Excel_read(file_name)
    print(a.dict_data())