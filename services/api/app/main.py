from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.domain.models import (
    PrepareDemoExecutionRequest,
    PrepareDemoExecutionResponse,
    PreparedOrder,
)
from app.domain.risk import ExecutionGuard
from app.services.mock_data import MOCK_SIGNALS, MOCK_ANALYSES

settings = get_settings()

app = FastAPI(
    title="Dubi Money Cool API",
    version="0.1.0",
    description="API MVP para terminal educativa de señales, análisis y ejecución demo asistida.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok", "service": "dmc-api", "live_trading_enabled": settings.enable_live_trading}


@app.get("/signals")
def list_signals():
    return MOCK_SIGNALS


@app.get("/signals/{signal_id}")
def get_signal(signal_id: str):
    for signal in MOCK_SIGNALS:
        if signal.id == signal_id:
            return signal
    raise HTTPException(status_code=404, detail="Signal not found")


@app.get("/analysis/{symbol}")
def get_analysis(symbol: str):
    normalized = symbol.upper().replace("-", "/")
    analysis = MOCK_ANALYSES.get(normalized)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis


@app.post("/execution/prepare-demo", response_model=PrepareDemoExecutionResponse)
def prepare_demo_execution(request: PrepareDemoExecutionRequest):
    signal = next((item for item in MOCK_SIGNALS if item.id == request.signal_id), None)
    if signal is None:
        raise HTTPException(status_code=404, detail="Signal not found")

    guard = ExecutionGuard(enable_live_trading=settings.enable_live_trading)
    validation = guard.validate_execution_request(
        signal=signal,
        account_type=request.account_type,
        risk_percent=request.risk_percent,
        requires_confirmation=request.requires_confirmation,
    )

    if not validation.approved:
        return PrepareDemoExecutionResponse(approved=False, message=validation.message, prepared_order=None)

    return PrepareDemoExecutionResponse(
        approved=True,
        message=validation.message,
        prepared_order=PreparedOrder(
            symbol=signal.symbol,
            direction=signal.direction,
            entry_price=signal.entry_price,
            stop_loss=signal.stop_loss,
            take_profit=signal.take_profit_1,
            risk_percent=request.risk_percent,
        ),
    )
