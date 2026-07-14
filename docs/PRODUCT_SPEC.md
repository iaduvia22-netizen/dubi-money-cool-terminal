# Product Spec — Dubi Money Cool Terminal

## Visión

Crear una terminal inteligente de trading asistido que convierta datos de mercado en escenarios operativos explicados, medibles y controlados por riesgo.

## Usuarios objetivo

1. Estudiantes de trading que necesitan entender setups con contexto.
2. Traders demo/intermedios que necesitan disciplina, filtros y bitácora.
3. Comunidades o academias que necesitan una terminal educativa de señales.
4. En fases futuras, usuarios adultos que cumplan requisitos legales y quieran ejecución asistida.

## Propuesta de valor

- Menos ruido: solo señales que pasan filtros.
- Más claridad: entrada, SL, TP, BE, invalidación y explicación.
- Más disciplina: risk engine antes de cualquier operación.
- Más trazabilidad: historial, resultado y métricas.
- Más seguridad: demo primero, live bloqueado por defecto.

## MVP v0.1

### Incluye

- Dashboard web.
- Radar de activos.
- Señales mock desde API.
- Ficha de señal.
- Motor de score inicial.
- Motor de riesgo inicial.
- Preparación de operación demo simulada.
- Historial mock/persistible.
- Documentación para Codex.

### No incluye

- Ejecución real.
- Recomendación financiera personalizada.
- Broker propio.
- Administración de cuentas de terceros.
- Promesa de rentabilidad.

## Activos iniciales

- EUR/USD
- GBP/USD
- USD/JPY
- XAU/USD
- NAS100/US100 si el broker lo soporta en demo

## Señal estándar

Campos mínimos:

- símbolo;
- dirección: BUY, SELL, WAIT;
- temporalidad;
- entrada;
- SL;
- TP1;
- TP2 opcional;
- BE trigger;
- score técnico;
- score fundamental;
- score de riesgo;
- score final;
- ratio R:R;
- explicación;
- invalidación;
- estado;
- timestamps.

## Estados

- DRAFT
- WATCHING
- ACTIVE
- BLOCKED_BY_RISK
- INVALIDATED
- COMPLETED
- FAILED
- EXPIRED

## Flujos

### Flujo de señal

1. Market Data Service recibe/consulta datos.
2. Strategy Engine calcula análisis.
3. Risk Engine valida.
4. Se genera o bloquea señal.
5. AI Layer explica.
6. WebSocket/API envía al frontend.
7. Usuario revisa.
8. Usuario simula o prepara demo.
9. Sistema registra resultado.

### Flujo de ejecución demo

1. Usuario hace clic en “Preparar demo”.
2. API recibe signal_id y account context.
3. ExecutionGuard valida.
4. Se crea orden simulada.
5. Se registra audit log.
6. Frontend muestra confirmación.

## Copy permitido

- “Análisis educativo.”
- “Escenario operativo.”
- “Señal con riesgo definido.”
- “Setup condicionado a confirmación.”

## Copy prohibido

- “Ganancia segura.”
- “Rentabilidad garantizada.”
- “Señales infalibles.”
- “Haz dinero automático.”
- “Opera sin perder.”
