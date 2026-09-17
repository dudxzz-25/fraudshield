from pathlib import Path
import json, sqlite3
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"transactions.csv"
OUT=ROOT/"data"/"output"
OUT.mkdir(parents=True,exist_ok=True)
FEATURES=["hour","amount","distance_km","attempts_10m","foreign_transaction","card_present"]


def evaluate(name, model, X_test, y_test):
    pred=model.predict(X_test)
    proba=model.predict_proba(X_test)[:,1]
    tn,fp,fn,tp=confusion_matrix(y_test,pred).ravel()
    return {
        "model":name,
        "precision":round(precision_score(y_test,pred,zero_division=0),4),
        "recall":round(recall_score(y_test,pred,zero_division=0),4),
        "f1":round(f1_score(y_test,pred,zero_division=0),4),
        "roc_auc":round(roc_auc_score(y_test,proba),4),
        "tn":int(tn),"fp":int(fp),"fn":int(fn),"tp":int(tp)
    }, pred, proba


def train(df: pd.DataFrame):
    X=df[FEATURES]; y=df["fraud"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    numeric=["hour","amount","distance_km","attempts_10m"]
    prep=ColumnTransformer([("num",StandardScaler(),numeric)],remainder="passthrough")
    models={
        "logistic_regression":Pipeline([("prep",prep),("model",LogisticRegression(class_weight="balanced",max_iter=1000,random_state=42))]),
        "random_forest":RandomForestClassifier(n_estimators=220,max_depth=10,min_samples_leaf=3,class_weight="balanced",random_state=42,n_jobs=-1)
    }
    results=[]; predictions={}
    for name,model in models.items():
        model.fit(X_train,y_train)
        metrics,pred,proba=evaluate(name,model,X_test,y_test)
        results.append(metrics)
        predictions[name]=(pred,proba)
    best=max(results,key=lambda x:x["f1"])["model"]
    pred,proba=predictions[best]
    scored=X_test.copy(); scored["actual_fraud"]=y_test.values; scored["predicted_fraud"]=pred; scored["fraud_probability"]=proba
    return results,best,scored


def main():
    df=pd.read_csv(RAW)
    results,best,scored=train(df)
    pd.DataFrame(results).to_csv(OUT/"metrics.csv",index=False)
    scored.to_csv(OUT/"scored_transactions.csv",index=False)
    with sqlite3.connect(OUT/"fraudshield.db") as conn:
        pd.DataFrame(results).to_sql("model_metrics",conn,if_exists="replace",index=False)
        scored.to_sql("scored_transactions",conn,if_exists="replace",index=False)
    (OUT/"best_model.txt").write_text(best,encoding="utf-8")
    print(pd.DataFrame(results).to_string(index=False)); print("Best by F1:",best)

if __name__=="__main__": main()
