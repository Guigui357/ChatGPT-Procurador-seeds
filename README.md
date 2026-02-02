# ChatGPT-Procurador-seeds

Procurador de seeds com busca exaustiva (sem heurística) para encontrar seeds
que tenham 3+ ferreiros. Este repositório exige um avaliador real de worldgen
para contar ferreiros — não existe *stub* embutido.

## Como usar

Você precisa fornecer um comando real que receba a seed e imprima a contagem
inteira de ferreiros em `stdout`. Use `{seed}` na linha de comando.

```bash
python main.py --cmd "./meu_avaliador_real --seed {seed}"
```

## Estrutura

- `procurador_seeds/searcher.py`: pipeline de busca exaustiva.
- `procurador_seeds/command_evaluator.py`: integra com avaliador real externo.
- `main.py`: CLI que executa a busca usando o avaliador real.
