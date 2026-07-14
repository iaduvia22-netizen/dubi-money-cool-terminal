# API Contract

## GET /health

Respuesta:

```json
{"status":"ok","service":"dmc-api"}
```

## GET /signals

Lista señales.

## GET /signals/{signal_id}

Detalle de señal.

## GET /analysis/{symbol}

Análisis actual de un símbolo.

## POST /execution/prepare-demo

Prepara una operación demo simulada. No ejecuta real.

Request:

```json
{
  "signal_id": "sig_xau_001",
  "risk_percent": 0.5,
  "requires_confirmation": true,
  "account_type": "DEMO"
}
```

Response aprobada:

```json
{
  "approved": true,
  "message": "Solicitud aprobada para demo.",
  "prepared_order": {
    "symbol": "XAU/USD",
    "direction": "BUY",
    "entry_price": 2384.2,
    "stop_loss": 2378.8,
    "take_profit": 2392.0,
    "risk_percent": 0.5
  }
}
```

Response bloqueada:

```json
{
  "approved": false,
  "message": "La ejecución real está desactivada en esta fase.",
  "prepared_order": null
}
```
