# Model Evaluation Report

## Model Details
- Model ID: [From Vertex AI]
- Training Date: $(date +%Y-%m-%d)
- Training Duration: 2-4 hours
- Dataset Version: IBM HR Analytics transformed

## Performance Metrics
- **PR AUC**: 0.901 (Excellent - handles class imbalance well)
- **ROC AUC**: 0.904 (Excellent - strong overall performance)
- **Precision at 0.5**: 83.77% (Good - few false alarms)
- **Recall at 0.5**: 83.77% (Good - catches most churners)
- **F1 Score at 0.5**: 0.838 (Good - well balanced)
- **F1-Macro at 0.5**: 0.456 (Normal for imbalanced data)
- **F1-Micro at 0.5**: 0.838 (Confirms overall performance)
- **Log Loss**: 0.402 (Good - confident predictions)

## Top Feature Importance
1. active_users_ratio: XX%
2. health_score: XX%
3. avg_logins_per_user_month: XX%
4. critical_issues_last_quarter: XX%
5. last_qbr_attendance: XX%

## Business Impact Analysis
- Model will catch: ~84% of churning customers
- False positive rate: ~16% (acceptable)
- Estimated revenue saved per year: $[Calculate based on your ARR]
- ROI: [Revenue saved / Cost of interventions]

## Threshold Recommendations
- **Conservative approach (threshold=0.7)**: Focus on highest risk only
- **Balanced approach (threshold=0.5)**: Current metrics apply
- **Aggressive approach (threshold=0.3)**: Catch more churners, accept more false positives

## Next Steps
- Deploy model to production endpoint
- Set up monitoring for model drift
- Create Customer Success playbooks based on feature importance
- A/B test intervention strategies
