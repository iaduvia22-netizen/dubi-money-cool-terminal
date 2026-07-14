from app.domain.models import TradingSignal, Direction, SignalStatus, AccountType
from app.domain.risk import ExecutionGuard


def make_signal(**overrides):
    data = dict(
        id="sig_test",
        symbol="EUR/USD",
        direction=Direction.BUY,
        timeframe="M15",
        entry_price=1.1,
        stop_loss=1.09,
        take_profit_1=1.12,
        technical_score=80,
        fundamental_score=70,
        risk_score=80,
        final_score=78,
        risk_reward_ratio=2.0,
        status=SignalStatus.ACTIVE,
        reason="test",
        invalidation_rule="test",
        ai_explanation="test",
    )
    data.update(overrides)
    return TradingSignal(**data)


def test_blocks_live_when_disabled():
    guard = ExecutionGuard(enable_live_trading=False)
    result = guard.validate_execution_request(make_signal(), AccountType.LIVE, 0.5, True)
    assert result.approved is False
    assert "real" in result.message.lower()


def test_blocks_missing_stop_loss():
    guard = ExecutionGuard(enable_live_trading=False)
    result = guard.validate_signal(make_signal(stop_loss=None))
    assert result.approved is False
    assert "Stop Loss" in result.message


def test_approves_valid_demo():
    guard = ExecutionGuard(enable_live_trading=False)
    result = guard.validate_execution_request(make_signal(), AccountType.DEMO, 0.5, True)
    assert result.approved is True
