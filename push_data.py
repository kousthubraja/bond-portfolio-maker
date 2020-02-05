import csv
from datetime import datetime
from bondportfolio.models import Bond

with open('cbm_security_master.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	
	for row in csv_reader:
		if line_count <= 5:
			line_count += 1
			continue
		else:
			isin = row[23]
			name = row[3]
			try:
				issue_date = datetime.strptime(row[7], '%d-%b-%Y')
				maturity_date = datetime.strptime(row[8], '%d-%b-%Y')
				ytm = row[19]
				tenor = maturity_date.year - issue_date.year
				if ytm != '':
					print(isin, name, tenor, ytm)
					b = Bond(isin=isin, name=name, tenor=tenor, ytm=ytm)
					b.save()
			except:
				print('Exception parsing')
			line_count += 1

