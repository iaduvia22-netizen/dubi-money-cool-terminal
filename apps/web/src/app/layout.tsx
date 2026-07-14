import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Dubi Money Cool Terminal',
  description: 'Terminal educativa de análisis, señales y ejecución demo asistida.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
