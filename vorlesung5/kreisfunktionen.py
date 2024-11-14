PI = 3.1415

def kreisumfang(r: float) -> float:
    ''' Diese Funktion berechnet den Kreisumfang
    Parameter r: Radius '''
    return  2 * r * PI

def kreisflaeche(r: float) -> float:
    ''' Diese Funktion berechnet die Fläche in einem Kreis
    Parameter r: Radius '''
    return PI * r * r
