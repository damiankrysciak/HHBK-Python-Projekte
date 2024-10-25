speed = float (input ("Geschwindigkeit (in KM/H):"))
rw = speed / 10 * 3
bw = (speed / 10) * (speed / 10)
aw= rw + bw

print (f"Der Anhalteweg beträgt {aw} m. Dieser ergibt sich aus einem Reaktionweg von {rw} m und einem Bremsweg von {bw} m")