# Política de riesgo

## Principio rector

Primero proteger al usuario. Después buscar oportunidades.

## Restricciones del MVP

- No live trading.
- No ejecución sin confirmación humana.
- No señal activa con score menor a 70.
- No operación sin SL.
- No operación con R:R menor a 1.5.
- No operación con riesgo por trade mayor a 1%.
- No operación si la cuenta supera pérdida diaria máxima.
- No operación durante evento de alto impacto cuando el filtro macro esté activo.
- No prometer rentabilidad.

## Reglas del Risk Engine

```txt
IF stop_loss IS NULL -> BLOCK
IF take_profit_1 IS NULL -> BLOCK
IF final_score < 70 -> WATCH/BLOCK
IF risk_reward_ratio < 1.5 -> BLOCK
IF risk_percent > 1.0 -> BLOCK
IF account_type == LIVE AND ENABLE_LIVE_TRADING != true -> BLOCK
IF requires_confirmation != true -> BLOCK
```

## Clasificación de señales

- 0–59: No operar.
- 60–69: Vigilar.
- 70–79: Setup válido.
- 80–89: Señal fuerte.
- 90–100: Señal premium sin garantía.

## Advertencia para producto

Toda visualización debe incluir que los mercados financieros implican riesgo y que los resultados pasados o simulados no garantizan resultados futuros.
