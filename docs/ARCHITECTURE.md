# Arquitectura

## Diagrama lógico

```txt
Frontend Next.js
  ↓ REST/WebSocket
Backend FastAPI
  ├── Signals API
  ├── Analysis API
  ├── Execution API
  ├── Auth/Billing futura
  ↓
Domain Services
  ├── Market Data Provider
  ├── Strategy Engine
  ├── Risk Engine
  ├── AI Explanation Layer
  └── Execution Adapter
  ↓
Infrastructure
  ├── PostgreSQL
  ├── Redis
  ├── cTrader Open API futura
  ├── cTrader Plugin SDK futura
  └── cTrader MCP futura
```

## Principios

1. Separar señal de ejecución.
2. Separar IA de lógica de trading.
3. La IA explica; no autoriza.
4. El Risk Engine bloquea.
5. Toda acción se audita.
6. Demo antes que live.
7. Multiusuario desde diseño inicial.
8. Credenciales fuera del repo.

## Servicios

### Web

Responsable de interfaz, gráficos, radar, fichas de señal, historial y acciones de usuario.

### API

Responsable de dominio, usuarios, señales, análisis, preparación de ejecución, auditoría y futuro billing.

### Strategy Engine

Responsable de convertir datos de mercado en hipótesis cuantificadas.

### Risk Engine

Responsable de bloquear señales u operaciones que no cumplan política.

### Market Data Provider

Interfaz común para datos. Permite cambiar mock por cTrader sin romper dominio.

### Execution Adapter

Prepara y ejecuta operaciones demo. Live queda bloqueado hasta una fase futura.

## Integración cTrader futura

### Open API

Uso previsto:

- símbolos;
- velas históricas;
- quotes live;
- cuentas demo;
- posiciones;
- órdenes demo;
- órdenes live solo en fase regulada.

### Plugin SDK

Uso previsto:

- panel lateral dentro de cTrader;
- orden preparada;
- modificación SL/TP;
- mover a BE;
- UX premium.

### MCP

Uso previsto:

- copiloto local;
- abrir gráficos;
- revisar cuenta;
- crear alertas;
- analizar desempeño;
- siempre con confirmación para trading.

## Entornos

- local
- staging
- production-demo
- production-live-gated futura

## Feature flags críticas

- `ENABLE_LIVE_TRADING=false`
- `ENABLE_CTRADER_DEMO=false` inicialmente
- `ENABLE_AI_EXPLANATIONS=false` hasta conectar proveedor
- `ENABLE_BILLING=false` hasta activar SaaS
