TotalSegundos = float(input("Por favor, entre com o número de segundos que deseja converter: "))

Dias = TotalSegundos // (3600*24)
SegundoRestDias = TotalSegundos % (3600*24)
Horas = SegundoRestDias//3600
SegundosRestHoras = TotalSegundos % 3600
Minutos = SegundosRestHoras // 60
SegundosRestMinutos = SegundosRestHoras % 60

print(Dias, "dias,", Horas, "horas,", Minutos, "minutos e", SegundosRestMinutos, "segundos")
