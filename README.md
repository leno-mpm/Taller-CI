# Gym Membership Quote

Aplicación de línea de comandos que cotiza el costo mensual de una membresía de gimnasio, desarrollada para el taller de Integración Continua de Ingeniería de Software II (ESPOL).

## Planes y extras

| Plan     | Precio por miembro | Extra                | Precio por miembro | Premium |
|----------|--------------------:|-----------------------|--------------------:|:-------:|
| BASIC    | 30                  | GROUP_CLASSES          | 15                  | No      |
| STANDARD | 45                  | PERSONAL_TRAINING      | 25                  | No      |
| PREMIUM  | 70                  | SPA                     | 30                  | Sí      |
|          |                     | SPECIALIZED_PROGRAM     | 40                  | Sí      |

Reglas de cálculo (R1-R7):

1. El plan debe ser uno de la tabla; cualquier otro es inválido.
2. Los extras premium (SPA, SPECIALIZED_PROGRAM) solo son válidos con el plan PREMIUM.
3. Subtotal = (precio del plan + precio de los extras) × número de miembros (mínimo 1).
4. Con 2 o más miembros, el subtotal recibe 10% de descuento.
5. Si el monto resultante es mayor a 400 se restan 50; si es mayor a 200 se restan 20 (no se acumulan).
6. Si la selección incluye al menos un extra premium, se añade 15% de recargo.
7. El total se redondea hacia arriba (half up) solo al final. Una selección inválida, o una respuesta "n" en la confirmación, da como resultado -1.

## Requisitos

- Python 3.10 o superior

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

El programa pide el plan, los extras y el número de miembros, muestra el subtotal, cada descuento/recargo y el total, y pide confirmación (y/n) antes de entregar el resultado.

## Tests

```bash
pytest
```

## Estructura del proyecto

```
gym/
  cotizacion.py    # R1, R2, R3, R7: planes, extras, subtotal y redondeo
  descuentos.py     # R4, R5, R6: descuento grupal, oferta especial y recargo premium
  membership.py      # Une R1-R7 en una sola función de cálculo (sin entrada/salida)
main.py               # R8: interfaz de línea de comandos
tests/                # Tests unitarios y de integración (R9)
```

## Equipo

| Rol              | Responsable de |
|------------------|----------------|
| Repository lead  | Repositorio, ramas, revisiones y merges de pull requests, interfaz de línea de comandos (R8) |
| Automation lead  | Jenkins, dirección pública, webhook, job de Jenkins, workflow de GitHub Actions |
| Developer A      | R1, R2, R3 y R7 (catálogo, validación, subtotal, redondeo) y sus tests unitarios |
| Developer B      | R4, R5 y R6 (descuento grupal, oferta especial, recargo premium) y sus tests unitarios |
