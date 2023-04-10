TotalSegundos = float(input("Por favor, entre com o número de segundos que deseja converter: "))

Dias = int(TotalSegundos // (3600*24))
SegundoRestDias = int(TotalSegundos % (3600*24))
Horas = int(SegundoRestDias//3600)
SegundosRestHoras = int(TotalSegundos % 3600)
Minutos = int(SegundosRestHoras // 60)
SegundosRestMinutos = int(SegundosRestHoras % 60)

print(Dias, "dias,", Horas, "horas,", Minutos, "minutos e", SegundosRestMinutos, "segundos")
