from XLUtil import XLUtils

def test_Readexcel():
    xlPath = 'C:\\Users\\admin\\Desktop\\Copy of Financial Sample.xlsx'
    xlOps = XLUtils.excelOps(xlPath,"Sheet1")
    rows = xlOps.getRowCount()
    cols = xlOps.getColCount()
    print()
    print(rows)
    print(cols)

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            print(xlOps.readData(r, c), end=" ")
        print()


def test_writeExcel():
    xlPath = 'C:\\Users\\admin\\Desktop\\Copy of Financial Sample.xlsx'
    xlOps = XLUtils.excelOps(xlPath, "TestSheet")

    l1 = ['', 'Hello', 'Vinay', 'Whats', 'Up', 'Pushkar']
    for r in range(1, 6):
        for c in range(1, 6):
            print(l1[c])

            xlOps.writeData( r, c, l1[c])
        print()

