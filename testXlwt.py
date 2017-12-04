#_*_ coding:utf-8 _*_
__author__ = 'Findlay'
import xlwt
import random

if __name__ == '__main__':
    # 注意这里的excel文件的后缀是xls 如果是xlsx打开是会提示无效
    newPath = "E:\\xfyang\\appiumTest\\demo.xlsx"
    wtBook = xlwt.Workbook()

    # 新增一个sheet
    sheet = wtBook.add_sheet("sheet1", cell_overwrite_ok=True)

    # 写入数据头
    headList = [u'序号', u'数据1', u'数据2', u'数据3']
    rowIndex = 0
    col = 0
    # 循环写
    for head in headList:
         sheet.write(rowIndex, col, head)
         col =  col + 1

         # 写入10行 0-99的随机数据
         for index in range(1, 11):
               for col in range(1, 4):
                    data = random.randint(0,99)
                    sheet.write(index, 0, index)  # 写序号
                    sheet.write(index, col, data) # 写数据
               #print (u"写第[%d]行数据" % index)

     # 保存
    wtBook.save(newPath)