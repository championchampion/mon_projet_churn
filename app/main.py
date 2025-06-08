from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

# Charger le modèle
model = joblib.load("model_xgb.joblib")

# Démarrer l'app FastAPI
app = FastAPI(title="API Prédiction Churn", version="1.0")

# Définir les entrées attendues
class ClientFeatures(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender_Male: int
    Partner_Yes: int
    Dependents_Yes: int
    PhoneService_Yes: int
    MultipleLines_No_phone_service: int
    MultipleLines_Yes: int
    InternetService_Fiber_optic: int
    InternetService_No: int
    OnlineSecurity_No_internet_service: int
    OnlineSecurity_Yes: int
    OnlineBackup_No_internet_service: int
    OnlineBackup_Yes: int
    DeviceProtection_No_internet_service: int
    DeviceProtection_Yes: int
    TechSupport_No_internet_service: int
    TechSupport_Yes: int
    StreamingTV_No_internet_service: int
    StreamingTV_Yes: int
    StreamingMovies_No_internet_service: int
    StreamingMovies_Yes: int
    Contract_One_year: int
    Contract_Two_year: int
    PaperlessBilling_Yes: int
    PaymentMethod_Credit_card_automatic: int
    PaymentMethod_Electronic_check: int
    PaymentMethod_Mailed_check: int

@app.post("/predict")
def predict_churn(data: ClientFeatures):
    input_data = np.array([list(data.dict().values())])
    proba = model.predict_proba(input_data)[0][1]
    prediction = int(proba >= 0.35)  # même seuil que dans ton notebook

    churn_proba = float(round(proba, 4))
    return {
        "churn_probability": churn_proba,
        "prediction": int(prediction),
        "interpretation": "Churn" if prediction == 1 else "No Churn"
    }

# Lancer le serveur uniquement si le script est exécuté directement
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
