import { getSignals } from '@/lib/api';

function directionLabel(direction: string) {
  if (direction === 'BUY') return 'Compra';
  if (direction === 'SELL') return 'Venta';
  return 'Esperar';
}

function statusLabel(status: string) {
  const labels: Record<string, string> = {
    ACTIVE: 'Activa',
    WATCHING: 'Vigilando',
    BLOCKED_BY_RISK: 'Bloqueada por riesgo',
    DRAFT: 'Borrador',
    INVALIDATED: 'Invalidada',
    COMPLETED: 'Completada',
    FAILED: 'Fallida',
    EXPIRED: 'Expirada',
  };
  return labels[status] ?? status;
}

export default async function Home() {
  const signals = await getSignals();

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <section className="mx-auto max-w-7xl px-6 py-8">
        <div className="mb-8 flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-cyan-300">Dubi Money Cool</p>
            <h1 className="mt-2 text-4xl font-bold tracking-tight md:text-6xl">Terminal de señales demo</h1>
            <p className="mt-3 max-w-3xl text-slate-300">
              Radar educativo de activos con entrada, SL, TP, BE, score y explicación. La ejecución real está bloqueada por diseño en este MVP.
            </p>
          </div>
          <div className="rounded-2xl border border-amber-400/30 bg-amber-400/10 px-4 py-3 text-sm text-amber-100">
            Live trading: <strong>desactivado</strong>
          </div>
        </div>

        <div className="grid gap-4 md:grid-cols-4">
          <Metric title="Señales" value={signals.length.toString()} />
          <Metric title="Activas" value={signals.filter((s) => s.status === 'ACTIVE').length.toString()} />
          <Metric title="Bloqueadas" value={signals.filter((s) => s.status === 'BLOCKED_BY_RISK').length.toString()} />
          <Metric title="Modo" value="Demo" />
        </div>

        <section className="mt-8 grid gap-5 lg:grid-cols-3">
          {signals.map((signal) => (
            <article key={signal.id} className="rounded-3xl border border-slate-800 bg-slate-900/70 p-5 shadow-2xl shadow-black/20">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <h2 className="text-2xl font-semibold">{signal.symbol}</h2>
                  <p className="text-sm text-slate-400">Temporalidad {signal.timeframe}</p>
                </div>
                <div className="rounded-full border border-cyan-300/40 px-3 py-1 text-sm text-cyan-200">
                  {signal.final_score}/100
                </div>
              </div>

              <div className="mt-5 grid grid-cols-2 gap-3 text-sm">
                <Info label="Dirección" value={directionLabel(signal.direction)} />
                <Info label="Estado" value={statusLabel(signal.status)} />
                <Info label="Entrada" value={signal.entry_price?.toString() ?? 'No definida'} />
                <Info label="SL" value={signal.stop_loss?.toString() ?? 'No definido'} />
                <Info label="TP1" value={signal.take_profit_1?.toString() ?? 'No definido'} />
                <Info label="BE" value={signal.break_even_trigger?.toString() ?? 'No definido'} />
              </div>

              <div className="mt-5 rounded-2xl bg-slate-950/80 p-4">
                <p className="text-sm font-semibold text-slate-200">Lectura IA</p>
                <p className="mt-2 text-sm leading-6 text-slate-300">{signal.ai_explanation}</p>
              </div>

              <div className="mt-5 space-y-2 text-sm text-slate-300">
                <p><strong>Motivo:</strong> {signal.reason}</p>
                <p><strong>Invalidación:</strong> {signal.invalidation_rule}</p>
                <p><strong>R:R:</strong> {signal.risk_reward_ratio ?? 'No aplica'}</p>
              </div>

              <form action={`/api/prepare?signal=${signal.id}`} className="mt-5">
                <button className="w-full rounded-2xl bg-cyan-300 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-200" type="submit">
                  Preparar demo
                </button>
              </form>
            </article>
          ))}
        </section>

        <section className="mt-8 rounded-3xl border border-slate-800 bg-slate-900/50 p-6">
          <h2 className="text-xl font-semibold">Política del MVP</h2>
          <p className="mt-2 text-slate-300">
            Esta versión es educativa, analítica y demo. No constituye asesoría financiera ni promete resultados. Toda ejecución real queda bloqueada hasta validación técnica, legal y controles de usuarios adultos.
          </p>
        </section>
      </section>
    </main>
  );
}

function Metric({ title, value }: { title: string; value: string }) {
  return (
    <div className="rounded-3xl border border-slate-800 bg-slate-900/70 p-5">
      <p className="text-sm text-slate-400">{title}</p>
      <p className="mt-2 text-3xl font-bold">{value}</p>
    </div>
  );
}

function Info({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl bg-slate-950/70 p-3">
      <p className="text-xs text-slate-500">{label}</p>
      <p className="mt-1 font-medium text-slate-100">{value}</p>
    </div>
  );
}
