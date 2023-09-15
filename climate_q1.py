import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
        
years = []
co2 = []
temp = []

cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData ORDER BY Year")  
records = cursor.fetchall()

for record in records:
    years.append(record[0])
    co2.append(record[1])
    temp.append(record[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png")

conn.close()
