import math

# Constantes
mu = 398600.4418  # km^3/s^2, constante gravitacional da Terra
n_revs_per_day = 14.55684828  # movimento médio em revoluções por dia

# Converter n de revoluções por dia para radianos por segundo
n_rad_per_sec = n_revs_per_day * (2 * math.pi) / 86400  # 2*pi rad por revolução, 86400 segundos por dia
print(n_rad_per_sec)

# Calcular o semieixo maior a
a = (mu / n_rad_per_sec**2) ** (1/3)  # km
print(a)

# Calcular o período orbital T
T = (2 * math.pi) / n_rad_per_sec  # segundos
T_minutes = T / 60  # converter para minutos
print(T_minutes)


# Dados extraídos do TLE
e = 0.0366552  # excentricidade
M_deg = 51.7108  # anomalia média em graus
M_rad = M_deg * math.pi / 180  # convertendo anomalia média para radianos
print(M_rad)

# Definir a função f(x) e sua derivada para o método de Newton-Raphson
def f(x):
    return x - e * math.sin(x) - M_rad

def df(x):
    return 1 - e * math.cos(x)

from scipy.optimize import newton
# Inicializar E com a aproximação inicial de M (anomalia média)
E_initial = M_rad

# Usar Newton-Raphson para encontrar a anomalia excêntrica E
E = newton(f, E_initial, df)
print(E)

# Calcular a anomalia verdadeira nu
nu = 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))

# Convertendo a anomalia verdadeira de radianos para graus
nu_deg = math.degrees(nu)

# Correção de quadrante para a anomalia verdadeira nu
if nu_deg > 180:
    corrected_nu_deg = nu_deg - 360
elif nu_deg < 0:
    corrected_nu_deg = nu_deg + 360
else:
    corrected_nu_deg = nu_deg
corrected_nu_deg  # Anomalia verdadeira corrigida em graus

print(nu_deg) # Anomalia verdadeira em graus

# Tempo de integração em minutos e em segundos
T_seconds = T  # período orbital em segundos
print(T_minutes, T_seconds)  # período orbital em minutos e segundos

