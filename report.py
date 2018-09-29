import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')

query = '''SELECT * FROM alerts
		   WHERE age BETWEEN datetime('now', '-30 days')
		   				 AND datetime('now', 'localtime')
		'''

df = pd.DataFrame(pd.read_sql_query(query, conn))

print(df.to_string())