export type Direction = 'BUY' | 'SELL' | 'WAIT';
export type SignalStatus =
  | 'DRAFT'
  | 'WATCHING'
  | 'ACTIVE'
  | 'BLOCKED_BY_RISK'
  | 'INVALIDATED'
  | 'COMPLETED'
  | 'FAILED'
  | 'EXPIRED';

export type TradingSignal = {
  id: string;
  symbol: string;
  direction: Direction;
  timeframe: string;
  entry_price: number | null;
  stop_loss: number | null;
  take_profit_1: number | null;
  take_profit_2?: number | null;
  break_even_trigger?: number | null;
  technical_score: number;
  fundamental_score: number;
  risk_score: number;
  final_score: number;
  risk_reward_ratio: number | null;
  status: SignalStatus;
  reason: string;
  invalidation_rule: string;
  ai_explanation: string;
};

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function getSignals(): Promise<TradingSignal[]> {
  const res = await fetch(`${API_URL}/signals`, { cache: 'no-store' });
  if (!res.ok) throw new Error('No se pudieron cargar las señales');
  return res.json();
}

export async function prepareDemo(signalId: string) {
  const res = await fetch(`${API_URL}/execution/prepare-demo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      signal_id: signalId,
      risk_percent: 0.5,
      requires_confirmation: true,
      account_type: 'DEMO',
    }),
  });
  if (!res.ok) throw new Error('No se pudo preparar la operación demo');
  return res.json();
}
