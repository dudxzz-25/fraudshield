# FraudShield

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-ML-3776AB?logo=python&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-Fraud-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="SQL" src="https://img.shields.io/badge/SQL-Investigation-4479A1">
  <a href="https://github.com/dudxzz-25/fraudshield/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/dudxzz-25/fraudshield/actions/workflows/ci.yml/badge.svg"></a>
</p>


[![CI](https://github.com/dudxzz-25/fraudshield/actions/workflows/ci.yml/badge.svg)](https://github.com/dudxzz-25/fraudshield/actions/workflows/ci.yml)

Pipeline de Machine Learning para **detecção de fraude em transações financeiras**, com foco em dados desbalanceados, comparação de modelos e métricas mais adequadas do que accuracy isolada.

## 🎯 Objetivo

Simular um problema de classificação de classe rara e avaliar modelos considerando o custo de falsos negativos e falsos positivos.

## 🛠️ Stack

**Python · Pandas · scikit-learn · SQLite · SQL**

## 🔎 Modelagem

O projeto compara:

- Regressão Logística com `class_weight="balanced"`;
- Random Forest com balanceamento de classe.

Features utilizadas:

- hora da transação;
- valor;
- distância;
- tentativas recentes;
- transação internacional;
- presença física do cartão.

## 📊 Resultados atuais

| Modelo | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression | 0,0717 | **0,7385** | **0,1308** | **0,8417** |
| Random Forest | **0,1200** | 0,0462 | 0,0667 | 0,7253 |

A Regressão Logística é selecionada por **F1-score**, refletindo um melhor equilíbrio entre cobertura de fraudes e precisão dentro deste conjunto sintético.

> Os dados são sintéticos e os resultados têm finalidade educacional e de portfólio.

## 📂 Estrutura

```text
fraudshield/
├── data/
│   ├── raw/
│   └── output/
├── scripts/generate_data.py
├── sql/investigation.sql
├── src/train.py
├── tests/test_train.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python src/train.py
```

Saídas em `data/output/`:

- `metrics.csv`
- `scored_transactions.csv`
- `fraudshield.db`
- `best_model.txt`

### Testes

```bash
python -m unittest discover -s tests -v
```

## 🧠 O que este projeto demonstra

- classificação com dados desbalanceados;
- comparação de modelos;
- Precision, Recall, F1 e ROC-AUC;
- pipelines e pré-processamento;
- persistência dos resultados em SQLite;
- investigação analítica via SQL.

## ⚠️ Limitações

O projeto não representa um sistema antifraude de produção. Não há dados reais, calibração de custo financeiro, detecção em tempo real, monitoramento de drift ou investigação humana dos alertas.

---

Desenvolvido por **Eduardo de Toledo Dias**.

[Portfólio](https://dudxzz-25.github.io/portfolio-web/) · [GitHub](https://github.com/dudxzz-25) · [LinkedIn](https://www.linkedin.com/in/eduardo-de-toledo-dias-880b9834b/)