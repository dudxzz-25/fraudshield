import sys, unittest
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.train import train

class TestTraining(unittest.TestCase):
    def test_pipeline_returns_metrics(self):
        rows=[]
        for i in range(120):
            fraud=1 if i%10==0 else 0
            rows.append([i%24,500 if fraud else 50,100 if fraud else 5,4 if fraud else 1,fraud,0 if fraud else 1,fraud])
        df=pd.DataFrame(rows,columns=["hour","amount","distance_km","attempts_10m","foreign_transaction","card_present","fraud"])
        results,best,scored=train(df)
        self.assertEqual(len(results),2)
        self.assertIn(best,{"logistic_regression","random_forest"})
        self.assertIn("fraud_probability",scored.columns)

if __name__=="__main__": unittest.main()
