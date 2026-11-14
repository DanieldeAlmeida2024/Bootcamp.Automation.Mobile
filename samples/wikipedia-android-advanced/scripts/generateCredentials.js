// Apenas dados falsos para preencher formulários Maestro. Nenhuma conta é criada.
// O domínio example.invalid é reservado e evita endereços reais de terceiros.
const suffix = Date.now().toString();

output.credentials = {
  username: `maestro_demo_${suffix}`,
  email: `maestro-demo-${suffix}@example.invalid`,
  password: `demo-not-for-login-${suffix}`,
};
