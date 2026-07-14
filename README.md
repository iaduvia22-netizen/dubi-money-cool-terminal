# Dubi Money Cool Terminal

Terminal SaaS de análisis, señales educativas, paper trading y ejecución asistida para cTrader.

> Estado: MVP starter para desarrollo con Codex. Por defecto **NO ejecuta operaciones reales**. La capa live debe permanecer bloqueada hasta cumplir validación técnica, legal y control de usuarios adultos.

## Objetivo del MVP

Construir una plataforma web donde el usuario pueda:

- ver un radar de activos;
- visualizar señales con entrada, SL, TP, BE y score;
- leer explicación asistida por IA;
- revisar historial y riesgo;
- simular operaciones;
- preparar integración con cTrader demo;
- dejar listo el camino a Plugin/MCP, sin habilitar trading real en esta fase.

## Stack

- Web: Next.js + TypeScript + TailwindCSS
- API: FastAPI + Pydantic
- DB: PostgreSQL
- Cache/Realtime: Redis
- Contenedores: Docker Compose
- Integración futura: cTrader Open API, Plugin SDK, Local MCP

## Inicio rápido

```bash
cp .env.example .env

docker compose up --build
```

Servicios:

- Web: http://localhost:3000
- API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Comandos sin Docker

API:

```bash
cd services/api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Web:

```bash
cd apps/web
npm install
npm run dev
```

## Para Codex

Lee primero:

1. `CODEX_PROMPT.md`
2. `docs/PRODUCT_SPEC.md`
3. `docs/ARCHITECTURE.md`
4. `docs/RISK_POLICY.md`
5. `docs/DEPLOYMENT.md`

Luego implementa por PRs pequeños:

1. endurecer API y modelos;
2. conectar datos reales en demo;
3. construir gráficos reales;
4. agregar backtesting;
5. agregar auth/suscripciones;
6. preparar despliegue.

## Política de riesgo

- No live trading en MVP.
- No señales sin SL.
- No ejecución sin confirmación humana.
- No usuarios menores para cuentas reales.
- No promesas de rentabilidad.
- No captación de dinero de terceros.
