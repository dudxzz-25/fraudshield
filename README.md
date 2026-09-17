# FraudShield

Pipeline de Machine Learning para **detecção de fraude em transações financeiras**, com foco em dados desbalanceados, comparação de modelos e métricas adequadas ao problema.

## Stack
Python, Pandas, scikit-learn, SQLite e SQL.

## Execução
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python src/train.py
```

Saídas em `data/output/`: métricas, previsões e banco de experimentos.

## Testes
```bash
python -m unittest discover -s tests -v
```
