from dataclasses import dataclass
from typing import Optional
from .models import AccountType, TradingSignal, SignalStatus


@dataclass(frozen=True)
class ExecutionValidation:
    approved: bool
    message: str


class ExecutionGuard:
    def __init__(self, enable_live_trading: bool = False):
        self.enable_live_trading = enable_live_trading

    def validate_signal(self, signal: TradingSignal) -> ExecutionValidation:
        if signal.status != SignalStatus.ACTIVE:
            return ExecutionValidation(False, "La señal no está activa.")

        if signal.entry_price is None:
            return ExecutionValidation(False, "La señal no tiene precio de entrada.")

        if signal.stop_loss is None:
            return ExecutionValidation(False, "Toda operación debe tener Stop Loss.")

        if signal.take_profit_1 is None:
            return ExecutionValidation(False, "Toda operación debe tener Take Profit.")

        if signal.final_score < 70:
            return ExecutionValidation(False, "El score mínimo para preparar operación es 70.")

        if signal.risk_reward_ratio is None or signal.risk_reward_ratio < 1.5:
            return ExecutionValidation(False, "El ratio riesgo/beneficio mínimo es 1.5.")

        return ExecutionValidation(True, "La señal cumple condiciones base.")

    def validate_execution_request(
        self,
        signal: TradingSignal,
        account_type: AccountType,
        risk_percent: float,
        requires_confirmation: bool,
    ) -> ExecutionValidation:
        base = self.validate_signal(signal)
        if not base.approved:
            return base

        if account_type == AccountType.LIVE and not self.enable_live_trading:
            return ExecutionValidation(False, "La ejecución real está desactivada en esta fase.")

        if risk_percent > 1:
            return ExecutionValidation(False, "El riesgo máximo permitido por operación es 1%.")

        if not requires_confirmation:
            return ExecutionValidation(False, "Toda operación requiere confirmación manual.")

        return ExecutionValidation(True, "Solicitud aprobada para demo.")
