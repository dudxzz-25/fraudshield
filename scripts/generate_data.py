from pathlib import Path
import random, math
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)
random.seed(42)
rows=[]
for i in range(1, 12001):
    hour=random.randint(0,23)
    amount=round(random.lognormvariate(4.3,0.9),2)
    distance=round(abs(random.gauss(18,30)),2)
    attempts=random.choices([1,2,3,4,5],[.77,.14,.055,.025,.01])[0]
    foreign=random.choices([0,1],[.94,.06])[0]
    card_present=random.choices([1,0],[.72,.28])[0]
    # Probability is generated from plausible risk signals.
    z=-6.2 + 0.004*amount + 0.018*distance + 0.8*(attempts-1) + 1.4*foreign + 0.8*(1-card_present) + (0.8 if hour < 5 else 0)
    p=1/(1+math.exp(-min(z,15)))
    fraud=1 if random.random() < p else 0
    rows.append([i,hour,amount,distance,attempts,foreign,card_present,fraud])
cols=["transaction_id","hour","amount","distance_km","attempts_10m","foreign_transaction","card_present","fraud"]
pd.DataFrame(rows,columns=cols).to_csv(OUT/"transactions.csv",index=False)
print("Fraud rate:", round(pd.DataFrame(rows,columns=cols).fraud.mean()*100,2), "%")
