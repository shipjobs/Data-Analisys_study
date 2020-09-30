import csv

max_temp = -999 #최고값을 저장할 변수
max_date = '' #최고값의 날짜 저장
f = open('D:/99. STUDY/01. Seoul data analisys/KMA_20200930141313.csv','r', encoding='cp949')
data = csv.reader(f, delimiter =',')

header = next(data)  #Stopiteration 주의

for row in data:
    if row[-1] == "":
        row[-1] = -999
        
    row[4] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]
        print(row)

print("서울의 최고 기온은" + max_date + "일" , max_temp ,"도 였습니다." )   # 문자, 숫자 출력 