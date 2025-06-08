# 🔮 API de Prédiction de Churn Client

Ce projet est une API REST construite avec **FastAPI**. Elle permet de prédire si un client va se désabonner (churn) en fonction de ses caractéristiques. Le modèle utilisé est un **XGBoost** entraîné et sauvegardé sous forme de fichier `.joblib`.

## 📁 Structure du projet

mon_projet_churn/
├── app/
│   ├── main.py                # Code FastAPI
│   ├── model_xgb.joblib       # Modèle entraîné
├── requirements.txt           # Fichier des dépendances
├── README.md                  # Fichier d'explication (à la racine)

---

## ⚙️ Installation

1. Cloner le dépôt ou télécharger les fichiers :
   ```bash
   git clone 
   cd mon_projet_churn

2.   Installer les dépendances :
        pip install -r requirements.txt

3.  Lancer l’API
        python -m uvicorn main:app --reload

Une fois lancée, accédez à la documentation interactive :

👉 http://127.0.0.1:8000/docs

 clic sur POST/predict

Exemple de requête JSON

{
  "SeniorCitizen": 1,
  "tenure": 1,
  "MonthlyCharges": 95.0,
  "TotalCharges": 95.0,
  "gender_Male": 1,
  "Partner_Yes": 0,
  "Dependents_Yes": 0,
  "PhoneService_Yes": 1,
  "MultipleLines_No_phone_service": 0,
  "MultipleLines_Yes": 1,
  "InternetService_Fiber_optic": 1,
  "InternetService_No": 0,
  "OnlineSecurity_No_internet_service": 0,
  "OnlineSecurity_Yes": 0,
  "OnlineBackup_No_internet_service": 0,
  "OnlineBackup_Yes": 0,
  "DeviceProtection_No_internet_service": 0,
  "DeviceProtection_Yes": 0,
  "TechSupport_No_internet_service": 0,
  "TechSupport_Yes": 0,
  "StreamingTV_No_internet_service": 0,
  "StreamingTV_Yes": 1,
  "StreamingMovies_No_internet_service": 0,
  "StreamingMovies_Yes": 1,
  "Contract_One_year": 0,
  "Contract_Two_year": 0,
  "PaperlessBilling_Yes": 1,
  "PaymentMethod_Credit_card_automatic": 0,
  "PaymentMethod_Electronic_check": 1,
  "PaymentMethod_Mailed_check": 0
}

✍️ Auteur

    Champion YEBOUE

    Projet réalisé dans le cadre de la Certification en datascience chez Gomycode

