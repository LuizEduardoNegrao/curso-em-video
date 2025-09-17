print('Conversor de Metros para TODAS as medidas de distancias')
m = float(input('Digite quantos metros: '))
km = float(m) / 1000
hm = float(m) / 100
dam = float(m) / 10
ml = float(m) * 1000
cm = float(m) * 100
dec = float(cm) * 10
print(f'Voce digitou: {m} metros, que da {km}Km, {hm}Hm, {dam}dam, {ml}Mm, {cm}cm, {dec}dem')
