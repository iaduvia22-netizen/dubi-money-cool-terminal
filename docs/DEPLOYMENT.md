# Deployment

## Local

```bash
cp .env.example .env
docker compose up --build
```

## Producción MVP recomendada

Opción simple:

- Frontend: Vercel
- API: Render/Fly.io/Railway/DigitalOcean App Platform
- PostgreSQL: Neon/Supabase/managed PostgreSQL
- Redis: Upstash/managed Redis
- Logs: Sentry

Opción más profesional:

- VPS/Cloud con Docker Compose o Kubernetes ligero
- Nginx reverse proxy
- PostgreSQL managed
- Redis managed
- GitHub Actions CI/CD
- Sentry + Grafana

## Variables críticas

- `ENABLE_LIVE_TRADING=false`
- `ENABLE_CTRADER_DEMO=false`
- `DATABASE_URL`
- `REDIS_URL`
- `JWT_SECRET`
- `CTRADER_CLIENT_ID`
- `CTRADER_CLIENT_SECRET`
- `CTRADER_REDIRECT_URI`

## Checklist antes de producción

- [ ] `.env` fuera del repo.
- [ ] HTTPS activo.
- [ ] CORS restringido.
- [ ] Rate limiting.
- [ ] Logs sin tokens.
- [ ] Tests passing.
- [ ] Live trading bloqueado.
- [ ] Disclaimers visibles.
- [ ] Backups DB.
- [ ] Monitoreo de errores.
