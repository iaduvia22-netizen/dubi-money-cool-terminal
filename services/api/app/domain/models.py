from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Direction(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    WAIT = "WAIT"


class SignalStatus(str, Enum):
    DRAFT = "DRAFT"
    WATCHING = "WATCHING"
    ACTIVE = "ACTIVE"
    BLOCKED_BY_RISK = "BLOCKED_BY_RISK"
    INVALIDATED = "INVALIDATED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"


class AccountType(str, Enum):
    DEMO = "DEMO"
    LIVE = "LIVE"


class TradingSignal(BaseModel):
    id: str
    symbol: str
    direction: Direction
    timeframe: str
    entry_price: Optional[float]
    stop_loss: Optional[float]
    take_profit_1: Optional[float]
    take_profit_2: Optional[float] = None
    break_even_trigger: Optional[float] = None
    technical_score: float = Field(ge=0, le=100)
    fundamental_score: float = Field(ge=0, le=100)
    risk_score: float = Field(ge=0, le=100)
    final_score: float = Field(ge=0, le=100)
    risk_reward_ratio: Optional[float] = None
    status: SignalStatus
    reason: str
    invalidation_rule: str
    ai_explanation: str


class MarketAnalysis(BaseModel):
    symbol: str
    timeframe: str
    trend: str
    market_structure: str
    liquidity_sweep: bool
    support_resistance_quality: float = Field(ge=0, le=100)
    price_action_quality: float = Field(ge=0, le=100)
    indicator_agreement: float = Field(ge=0, le=100)
    macro_risk: str
    summary: str
    confidence: float = Field(ge=0, le=100)


class PrepareDemoExecutionRequest(BaseModel):
    signal_id: str
    risk_percent: float = Field(gt=0, le=5)
    requires_confirmation: bool = True
    account_type: AccountType = AccountType.DEMO


class PreparedOrder(BaseModel):
    symbol: str
    direction: Direction
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_percent: float


class PrepareDemoExecutionResponse(BaseModel):
    approved: bool
    message: str
    prepared_order: Optional[PreparedOrder] = None
