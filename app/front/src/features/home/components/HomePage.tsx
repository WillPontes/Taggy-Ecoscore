import { Link } from "@tanstack/react-router";

export function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 p-8">
      <h1 className="text-4xl font-bold tracking-tight">Taggy EcoScore</h1>
      <p className="text-muted-foreground text-lg">
        Pagamento automatizado de pedágios e estacionamentos com métricas ESG
      </p>
      <Link
        to="/users"
        className="text-primary text-sm font-medium underline underline-offset-4 hover:opacity-90"
      >
        Ver usuários (exemplo API)
      </Link>
    </main>
  );
}
