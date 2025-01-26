
def GetDriverName(a):
    if a in f1_drivers:
        return f1_drivers[a]
    else:
        return 'Driver Not Found'
    
f1_drivers = {
    1: "Max Verstappen",
    4: "Lando Norris",
    10: "Pierre Gasly",
    11: "Sergio Pérez",
    14: "Fernando Alonso",
    16: "Charles Leclerc",
    18: "Lance Stroll",
    20: "Kevin Magnussen",
    22: "Yuki Tsunoda",
    23: "Alexander Albon",
    24: "Zhou Guanyu",
    27: "Nico Hülkenberg",
    31: "Esteban Ocon",
    44: "Lewis Hamilton",
    55: "Carlos Sainz"
}
