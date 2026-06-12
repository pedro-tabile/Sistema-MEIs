# Instruções automáticas para revisão de pontos críticos

Objetivo: checklist conciso para revisar PRs e integrar ao CI.

1. Priorizar segurança e confidencialidade
- Autenticação e autorização: fluxos, roles, tokens, escopos.
- Validação de entrada: evitar SQL/NoSQL/command injection.
- Logs: não registrar dados sensíveis (PII, senhas, tokens).

2. Criptografia
- Tráfego/TLS obrigatório; armazenamento de segredos seguro; rotação de chaves.

3. Tratamento de erros
- Não vazar stack traces; retornar erros genéricos ao usuário; logar internamente.

4. Concorrência e recursos
- Verificar race conditions, locks, uso correto de async/await, fechamento de handles.

5. Dependências
- Escanear vulnerabilidades, travar versões, avaliar atualizações críticas.

6. Performance
- Identificar operações I/O pesadas, otimizar queries e adicionar índices quando necessário.

7. Testes
- Cobertura unitária e integração; testes de limites; testes de carga se aplicável.

8. Automação/CI
- Rodar linters, SAST, dependabot, scans de dependências e testes no pipeline; gerar relatório de severidade e bloquear merges para falhas críticas.

Como usar: anexar checklist a PRs e executar passos automaticamente no CI. Mantê-lo atualizado conforme o projeto evolui.
