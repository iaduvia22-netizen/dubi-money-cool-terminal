# Prompt maestro para Codex

Actúa como senior full-stack engineer, quant platform engineer y product architect. Vas a desarrollar **Dubi Money Cool Terminal**, una terminal SaaS de análisis, señales educativas, paper trading y ejecución asistida para cTrader.

## Objetivo principal

Convertir este starter en un producto MVP funcional, seguro y desplegable:

- web dashboard profesional;
- API robusta;
- motor de señales determinístico;
- risk engine obligatorio;
- datos mock reemplazables por cTrader demo;
- historial de señales;
- paper trading;
- preparación de integración cTrader Open API;
- live trading bloqueado por defecto.

## Restricciones obligatorias

1. No habilites ejecución real en producción inicial.
2. Todo endpoint de ejecución debe pasar por `ExecutionGuard`.
3. Toda señal debe tener `entry_price`, `stop_loss`, `take_profit_1`, `risk_reward_ratio`, `final_score` y `status`.
4. Si `final_score < 70`, la señal no puede ser `ACTIVE`.
5. Si no hay SL, bloquear.
6. Si el R:R es menor a 1.5, bloquear.
7. Si `ACCOUNT_TYPE=LIVE`, bloquear salvo feature flag explícita y validaciones legales/adulto/KYC ya implementadas.
8. La IA no decide operaciones; solo explica decisiones generadas por el motor.
9. No escribas copy prometiendo rentabilidad.
10. Mantén el código tipado, testeado y con separación por dominios.

## Prioridad de trabajo

### PR 1 — Base estable
- Revisar estructura.
- Ejecutar tests.
- Arreglar lint/type errors.
- Mejorar manejo de errores.
- Agregar logging estructurado.

### PR 2 — Frontend MVP
- Dashboard con radar de activos.
- Vista de señal.
- Cards de score.
- Estado de riesgo.
- Tabla de historial.
- Botón “Preparar demo” sin ejecución real.

### PR 3 — API y dominio
- Endpoints `/signals`, `/signals/{id}`, `/analysis/{symbol}`, `/execution/prepare-demo`.
- Persistencia con PostgreSQL.
- Migraciones Alembic.
- Tests unitarios del scoring y guard.

### PR 4 — Market data adapter
- Interfaz `MarketDataProvider`.
- Implementar `MockMarketDataProvider`.
- Preparar `CTraderOpenApiProvider` con métodos claros y TODOs.
- No almacenar credenciales en código.

### PR 5 — Backtesting inicial
- Endpoint para backtesting simple.
- Métricas: win rate, profit factor, max drawdown, avg R.
- Reporte por símbolo y timeframe.

### PR 6 — Producción
- Dockerfile por servicio.
- Health checks.
- Variables env.
- CI GitHub Actions.
- Deploy docs.

## Definición de terminado MVP

- `docker compose up --build` levanta web + api + postgres + redis.
- La web muestra señales mock provenientes de la API.
- El usuario puede abrir una señal y ver explicación, SL/TP/BE y score.
- La preparación de demo valida el riesgo y devuelve una orden simulada.
- Live trading permanece bloqueado.
- Tests de API pasan.
- README actualizado.

## Mensaje del producto

Dubi Money Cool Terminal es una herramienta educativa y analítica para entender escenarios de mercado, gestionar riesgo y practicar decisiones con datos. No ofrece asesoría financiera personalizada ni garantiza resultados.
