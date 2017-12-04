#_*_ coding:utf-8 _*_
__author__ = 'xfyang'
import xlrd
import xlwt

import datetime

if __name__ == '__main__':
    # excel文件全路径
    xlPath = "E:\\xfyang\\appiumTest\\testExcel.xlsx"

    # 生成新建文件的文件名
    now = datetime.datetime.now()
    nowTime=str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+"_"+str(now.microsecond)
    print(nowTime)


    # 用于读取excel
    xlBook = xlrd.open_workbook(xlPath)

    # 新建新的Excel文档
    wtBook=xlwt.Workbook(encoding='utf-8')
    saveSheet=wtBook.add_sheet("Sheet1")

    # 获取excel工作簿数
    count = len(xlBook.sheets())
    print(u"工作簿数为:  ", count)

    # 获取 表 数据的行列数
    #table = xlBook.sheets()[0]     # 按序号读取
    table =xlBook.sheet_by_name("Sheet1")   # 按Sheet名称读取
    nrows = table.nrows
    ncols = table.ncols
    print(u"表数据行列为(%d, %d)" % (nrows, ncols))

    # 循环读取数据
    for i in range(0, nrows):
        rowValues = table.row_values(i) # 按行读取数据
        # 输出读取的数据
        acols=0
        for data in rowValues:
             print (data, "    ",)
             saveSheet.write(i, acols, data)  # 写入数据
             acols=acols+1
        print("")

    wtBook.save("E:\\xfyang\\appiumTest\\" + nowTime + ".xls")
    print("保存成功")