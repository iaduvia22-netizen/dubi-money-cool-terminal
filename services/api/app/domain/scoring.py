from dataclasses import dataclass
from .models import Direction, SignalStatus


@dataclass(frozen=True)
class AnalysisInput:
    trend_score: float
    structure_score: float
    liquidity_score: float
    price_action_score: float
    indicators_score: float
    fundamental_score: float
    risk_score: float


@dataclass(frozen=True)
class SignalDecision:
    direction: Direction
    final_score: float
    status: SignalStatus
    reason: str


class DMCScoringEngine:
    WEIGHTS = {
        "trend": 0.20,
        "structure": 0.20,
        "liquidity": 0.15,
        "price_action": 0.15,
        "indicators": 0.10,
        "fundamental": 0.10,
        "risk": 0.10,
    }

    def calculate_score(self, data: AnalysisInput) -> float:
        for value in data.__dict__.values():
            if value < 0 or value > 100:
                raise ValueError("All scoring inputs must be between 0 and 100")

        score = (
            data.trend_score * self.WEIGHTS["trend"]
            + data.structure_score * self.WEIGHTS["structure"]
            + data.liquidity_score * self.WEIGHTS["liquidity"]
            + data.price_action_score * self.WEIGHTS["price_action"]
            + data.indicators_score * self.WEIGHTS["indicators"]
            + data.fundamental_score * self.WEIGHTS["fundamental"]
            + data.risk_score * self.WEIGHTS["risk"]
        )
        return round(score, 2)

    def decide(self, data: AnalysisInput, suggested_direction: Direction) -> SignalDecision:
        final_score = self.calculate_score(data)

        if data.risk_score < 50:
            return SignalDecision(
                direction=Direction.WAIT,
                final_score=final_score,
                status=SignalStatus.BLOCKED_BY_RISK,
                reason="La señal fue bloqueada por condiciones de riesgo.",
            )

        if final_score < 60:
            return SignalDecision(
                direction=Direction.WAIT,
                final_score=final_score,
                status=SignalStatus.WATCHING,
                reason="El setup no tiene suficiente calidad.",
            )

        if final_score < 70:
            return SignalDecision(
                direction=Direction.WAIT,
                final_score=final_score,
                status=SignalStatus.WATCHING,
                reason="El setup existe, pero necesita confirmación.",
            )

        if final_score < 80:
            return SignalDecision(
                direction=suggested_direction,
                final_score=final_score,
                status=SignalStatus.ACTIVE,
                reason="Setup válido, condicionado a confirmación.",
            )

        return SignalDecision(
            direction=suggested_direction,
            final_score=final_score,
            status=SignalStatus.ACTIVE,
            reason="Setup fuerte, con riesgo controlado y confirmación suficiente.",
        )
