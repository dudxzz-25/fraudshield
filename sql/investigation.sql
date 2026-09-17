.headers on
.mode column
SELECT predicted_fraud, COUNT(*) AS transactions, ROUND(AVG(amount),2) AS avg_amount
FROM scored_transactions GROUP BY predicted_fraud;

SELECT hour, COUNT(*) AS suspicious
FROM scored_transactions
WHERE predicted_fraud=1
GROUP BY hour ORDER BY suspicious DESC;

SELECT foreign_transaction, card_present, COUNT(*) AS suspicious
FROM scored_transactions
WHERE predicted_fraud=1
GROUP BY foreign_transaction, card_present
ORDER BY suspicious DESC;
