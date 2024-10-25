jahr_input = int (input ("Bitte benötigtes Jahr angeben: "))
jung = 6
erwachsen = 9
alt = 12
jahr = 0

jung_neu = erwachsen * 4 + alt * 2
erwachsen_neu = jung // 2
alt = erwachsen // 3
jung = jung_neu
jahr = jahr + 1

while jahr < jahr_input:
    erwachsen = erwachsen_neu
    jung_neu = erwachsen_neu * 4 + alt * 2
    erwachsen_neu = jung // 2
    alt = erwachsen // 3
    jung = jung_neu
    jahr = jahr + 1

print(f"Die berechneten Populationswerte sind:")
print(f"Anzahl junger Mäuse: {jung_neu}")
print(f"Anzahl erwachsener Mäuse: {erwachsen_neu}")
print(f"Anzahl alter Mäuse: {alt}")