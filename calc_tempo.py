
from datetime import datetime
tempoi = datetime(2022, 4, 15, 9, 9, 28, 517380)
tempof = datetime.now()
tempo_aluguel = tempof - tempoi
segundos = tempo_aluguel.total_seconds()

semanas = segundos // 604800
dias = (segundos % 604800) // 86400
horas = ((segundos % 604800) % 86400) / 3600


print(semanas, dias, horas)
