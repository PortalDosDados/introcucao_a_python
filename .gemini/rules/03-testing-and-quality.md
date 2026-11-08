# 03-testing-and-quality.md - Qualidade, Validação e Checklist

## Estrutura de Testes
- **Framework de Testes**: NÃO IDENTIFICADO [sem suite automatizada de testes].
- **Estratégia de Validação**: Teste manual interativo via console simulando os casos do enunciado [DIRETRIZ].

## Segurança e Gestão de Segredos
- **NUNCA** commitar ou introduzir senhas, chaves de API, credenciais ou arquivos `.env*` [DIRETRIZ / .gitignore].
- **SEMPRE** respeitar o `.gitignore` existente no repositório [.gitignore].

## Checklist Obrigatório para a IA (Antes de Finalizar Qualquer Tarefa)
1. **Escopo Estrito**:
   - Não alterar nenhum arquivo fora do escopo do exercício/capítulo solicitado.
   - Não adicionar dependências de terceiros sem permissão expressa.
2. **Validação de Sintaxe**:
   - Executar validação de compilação sem erros:
     ```bash
     python -m py_compile <caminho_do_arquivo>.py
     ```
3. **Aderência Didática**:
   - Confirmar que a solução não utiliza recursos que ultrapassem o capítulo alvo do livro [README.md].
4. **Formatação e Padrão**:
   - Garantir enunciado em aspas triplas no topo do arquivo.
   - Garantir uso de f-strings e identificadores estritamente em ASCII (sem acentos).
   - Formatar o código seguindo a convenção do `black` (PEP 8) [DIRETRIZ].
5. **Teste Interativo de Validação**:
   - Validar as entradas e saídas esperadas de acordo com as regras descritas no exercício.
