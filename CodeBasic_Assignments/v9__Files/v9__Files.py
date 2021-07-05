filePath = 'D:\\Learning\\Git_Repository\\Data-Science_Learning_Path\\CodeBasic_Assignments\\v9__Files\\'

with open(filePath+'Stocks.csv', 'r') as f, open(filePath+'processed_stock.csv','w') as out:
    out.write('Company Name, PE Ratio, PB Ratio\n')
    next(f)     #This will skip first line so that we can extract exact data from input files
    for line in f:
        tokens = line.split(',')
        stock = tokens[0]
        price = int(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])

        pe = round(price/eps, 2)
        pb = round(price/book, 2)

        out.write(f"{stock},{pe},{pb}\n")