import { NextRequest, NextResponse } from 'next/server';

export async function GET(req: NextRequest) {
  const signal = req.nextUrl.searchParams.get('signal');
  const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

  if (!signal) {
    return NextResponse.json({ error: 'Missing signal' }, { status: 400 });
  }

  const response = await fetch(`${apiUrl}/execution/prepare-demo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      signal_id: signal,
      risk_percent: 0.5,
      requires_confirmation: true,
      account_type: 'DEMO',
    }),
  });

  const data = await response.json();
  const html = `
    <html>
      <body style="font-family: system-ui; background:#020617; color:white; padding:32px;">
        <h1>Preparación demo</h1>
        <pre style="background:#0f172a; padding:24px; border-radius:16px; white-space:pre-wrap;">${JSON.stringify(data, null, 2)}</pre>
        <a style="color:#67e8f9" href="/">Volver al dashboard</a>
      </body>
    </html>
  `;

  return new NextResponse(html, { headers: { 'Content-Type': 'text/html' } });
}
