# Energy_predictor
A Machine Learning + Streamlit Application for Real-Time Energy Use Forecasting

This project predicts energy consumption using environmental factors, device usage, and occupancy data.
It also calculates actual device-wise consumption (HVAC, Lights, Fans) based on wattage and usage duration, giving users a realistic understanding of total power usage.

The application is built with:

Python
Machine Learning (Scikit-learn)
Streamlit
Pandas
Joblib

🎯 Project Highlights

✔ Predicts building energy consumption in Wh / kWh
✔ Device-wise energy calculation (HVAC, Lights, Fans)
✔ Handles custom wattage inputs
✔ Uses date + hour selection for accurate forecasting
✔ Real-time prediction using a trained ML model (Energy_Consumption.pkl)
✔ Clean, interactive UI using Streamlit
✔ Ready for deployment

🧠 How It Works
🔹 1. User Inputs

The app collects the following details :-
Date range
Hour of the day
Temperature
Humidity
Occupancy
HVAC usage & watt
Light usage & watt
Fan usage & wa
Day of week
Holiday flag

📌 Future Enhancements

1. Add MILP optimization for cost reduction
2. Add solar power integration
3. Add multi-day forecasting (LSTM / XGBoost)
4. Add anomaly detection for unusual power spikes
