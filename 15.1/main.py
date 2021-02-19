import avgspeed

distance = int(input("Jaką drogę przebyłeś? "))
time = int(input("Ile godzin Ci to zajęło? "))

print(f"Twoja średnia prędkość to: ", {avgspeed.avg_speed(distance, time)})

