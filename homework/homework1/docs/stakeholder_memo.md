# Stakeholder Memo  
**Stage 01: Problem Framing & Scoping**  

## Problem Overview  
Financial markets are highly dynamic, with short-term stock movements often appearing random. However, traders and investment managers still rely on timely signals to adjust their positions. This project focuses on predicting **hourly directional movements (up vs. down)** of BlackRock, Inc. (BLK) stock using supervised machine learning. The problem is framed as a **binary classification task**, where the output is the probability of an uptrend in the next hour.  

## Stakeholders & End Users  
- **Quantitative Traders**: Need intraday signals to inform buy/sell execution.  
- **Investment Managers**: Use short-term predictions to manage risk and optimize portfolio strategies.  
- **Researchers & Analysts**: Evaluate the effectiveness of machine learning and technical indicators in forecasting liquid equities.  

## Useful Answer  
The useful output is **predictive**. Specifically:  
- **Model Output**: Probability and class prediction for next-hour uptrend.  
- **Evaluation Metrics**: AUC, accuracy, F1-score.  
- **Artifact**: A machine learning model that can be retrained on new data and generate predictive signals.  

## Assumptions & Constraints  
- **Data**: Hourly BLK data (Oct 2020 – Jan 2025) is clean, reliable, and representative.  
- **Capacity**: Sufficient compute resources for feature engineering and model training.  
- **Latency**: Current focus is offline backtesting; real-time deployment would require additional infrastructure.  
- **Compliance**: Data sourced from a reputable provider; no regulatory restrictions in project context.  

## Known Risks  
- Predictive power at hourly frequency may be limited (risk of near-random accuracy).  
- Model may become biased due to class imbalance.  
- Feature effectiveness may degrade over time (concept drift).  
- Exclusion of market microstructure effects may reduce realism for trading use cases.  

## Decision Context  
- A “useful” model will demonstrate predictive power significantly better than random guessing.  
- If successful, the output can support intraday decision-making for trading and portfolio management.  
- If not, findings still provide valuable insights into the limits of machine learning at short horizons.  
