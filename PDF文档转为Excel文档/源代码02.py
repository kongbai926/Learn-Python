import pdfplumber
import xlwt


def toEcel():
    workbook = xlwt.Workbook()  # 定义workbook
    sheet = workbook.add_sheet('Sheet1')  # 添加sheet
    i = 0  # Excel起始位置
    pdf = pdfplumber.open(r"D:\奇幻时空\Files\地理信息系统\课程设计\天津市A级景区.pdf")
    print('开始读取数据')

    for page in pdf.pages[0:5]:  # 这里的page[0:20]可以根据实际pdf的页数来进行扩大
        # 获取当前页面的全部文本信息，包括表格中的文字
        for table in page.extract_tables():
            # print(table)
            for row in table:
                # print(row)
                for j in range(len(row)):
                    sheet.write(i, j, row[j])
                i += 1

    pdf.close()

    # 保存Excel表
    workbook.encoding = "utf-8"
    workbook.save(r'D:\奇幻时空\Files\地理信息系统\课程设计\天津市A级景区.csv')
    print('写入excel成功')


if __name__ == '__main__':
    print("开始")
    toEcel()