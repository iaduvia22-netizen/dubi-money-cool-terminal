# Siguientes tareas exactas para Codex

Usa este orden.

## Task 1

Arregla cualquier error de instalación/build. Ejecuta:

```bash
docker compose up --build
```

Corrige hasta que Web y API levanten.

## Task 2

Agrega persistencia PostgreSQL:

- SQLAlchemy o SQLModel;
- tabla `signals`;
- tabla `audit_logs`;
- seed inicial con mock signals;
- endpoints leyendo desde DB.

## Task 3

Agrega vista de detalle de señal:

- ruta `/signals/[id]`;
- panel de gráfico placeholder;
- tabla SL/TP/BE;
- explicación;
- botón preparar demo;
- estado de risk guard.

## Task 4

Implementa `MarketDataProvider`:

```python
class MarketDataProvider(Protocol):
    def get_symbols(self) -> list[Symbol]: ...
    def get_candles(self, symbol: str, timeframe: str, limit: int): ...
    def get_quote(self, symbol: str): ...
```

Mantén `MockMarketDataProvider` y crea archivo `ctrader_provider.py` con TODOs seguros.

## Task 5

Implementa backtesting inicial con velas mock/importadas CSV.

## Task 6

Agrega auth básica:

- usuarios;
- sesiones;
- roles: USER, ADMIN;
- plan: FREE, PRO, ELITE.

## Task 7

Prepara producción:

- Dockerfile production para web;
- Nginx opcional;
- env validation;
- rate limiting;
- Sentry placeholder;
- docs de despliegue.
