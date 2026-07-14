from app.domain.scoring import DMCScoringEngine, AnalysisInput
from app.domain.models import Direction, SignalStatus


def test_score_range_and_decision():
    engine = DMCScoringEngine()
    data = AnalysisInput(
        trend_score=80,
        structure_score=80,
        liquidity_score=70,
        price_action_score=75,
        indicators_score=65,
        fundamental_score=60,
        risk_score=80,
    )
    decision = engine.decide(data, Direction.BUY)
    assert decision.final_score >= 70
    assert decision.status == SignalStatus.ACTIVE
