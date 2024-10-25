jahr_input = int (input ("Bitte benötigtes Jahr angeben: "))
g_0_14 = 12.3
g_15_49 = 39.1
g_50_64 = 15.5
g_65 = 16.3
jahr = 2005

while jahr < jahr_input:
    g_0_14_temp = g_0_14 * 0.93 + g_15_49 * 0.02
    g_15_49_temp = g_0_14 * 0.066 + g_15_49 * 0.97
    g_50_64_temp = g_15_49 * 0.029 + g_50_64 * 0.925
    g_65 = g_50_64 * 0.066 + g_65 * 0.972
    g_0_14 = g_0_14_temp
    g_15_49 = g_15_49_temp
    g_50_64 = g_50_64_temp
    jahr = jahr + 1

print(f"Die berechneten Populationswerte sind:")
print(f"Anzahl 0- bis 14-jähriger: {round(g_0_14, 2)} Mio.")
print(f"Anzahl 15- bis 49-jähriger: {round(g_15_49, 2)} Mio.")
print(f"Anzahl 50- bis 64-jähriger: {round(g_50_64, 2)} Mio.")
print(f"Anzahl über 65-jähriger: {round(g_65, 2)} Mio.")
