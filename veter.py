def get_wind_class(wind): #объявление функции
 wind = int(input("Введите скорость ветра:"))
 if 1<=wind<=4:
    return("слабый(1)")
 elif 5<=wind<=10:
    return("умеренный(2)")
 elif 11<=wind <=18:
    return("сильный(3)")
 elif wind>=19:
    return("ураганный(4)")
for wind in range(1,20):
 print (get_wind_class(wind))