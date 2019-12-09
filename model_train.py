from openpyxl import load_workbook
import numpy as np
import os

file_path = u'cleaned_data/'
target_file = u'train_data.xlsx'
comments = []

if __name__ == '__main__':
    files = os.listdir(file_path)

    for file in files:
        temp = []
        wb = load_workbook(file_path + file)
        ws = wb.active

        num = ws.max_row + 1
        for row in range(2, num + 1):
            temp.append(ws['B' + str(row)].value)

        temp = np.array(temp)
        index = np.random.choice(temp.shape[0], size=50, replace=False)
        comments.append(temp[index])
