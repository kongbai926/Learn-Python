"""
程序出错，需要更改
"""
# tabula-py是tabla-java的Python包装器，它可以读取PDF文件中的表。这意味着我们需要先安装Java
import tabula


df = tabula.read_pdf('D:\奇幻时空\Files\地理信息系统\课程设计\天津市A级景区.pdf', pages = 1, lattice=True)

# print(type(df))
df.columns = df.columns.str.replace('\r', ' ')

data = df.dropna()

data.to_excel(r'D:\奇幻时空\Files\地理信息系统\课程设计\天津市A级景区.xlsx')
