from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import logging
import uvicorn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

demo_data = pd.DataFrame({
    "Make": ["Toyota", "Ford", "BMW"],
    "Model": ["Corolla", "Focus", "X5"],
    "Year": [2015, 2017, 2019],
    "Style": ["Sedan", "Hatchback", "SUV"],
    "Distance": [80000, 60000, 40000],
    "Engine_capacity": [1600, 1800, 3000],
    "Fuel_type": ["Petrol", "Diesel", "Petrol"],
    "Transmission": ["Manual", "Automatic", "Automatic"],
    "Price(euro)": [8000, 9000, 25000]
})

cat_columns = ['Make', 'Model', 'Style', 'Fuel_type', 'Transmission']
num_columns = ['Year', 'Distance', 'Engine_capacity', 'Price(euro)']
ordinal = OrdinalEncoder()
demo_data[cat_columns] = ordinal.fit_transform(demo_data[cat_columns])

X = demo_data.drop(columns=["Price(euro)"])
y = demo_data["Price(euro)"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
model.fit(X_scaled, y)

app = FastAPI(title="Car Price UTF-8")


def clear_data(df):
    df[cat_columns] = ordinal.transform(df[cat_columns])
    return df


def featurize(dframe):
    dframe['Distance_by_year'] = dframe['Distance'] / (2022 - dframe['Year'])
    dframe['age'] = 2024 - dframe['Year']
    mean_engine_cap = dframe.groupby('Style')['Engine_capacity'].transform('mean')
    dframe['eng_cap_diff'] = abs(dframe['Engine_capacity'] - mean_engine_cap)

    max_engine_cap = dframe.groupby('Style')['Engine_capacity'].transform('max')
    dframe['eng_cap_diff_max'] = abs(dframe['Engine_capacity'] - max_engine_cap)

    return dframe


class CarFeatures(BaseModel):
    make: str
    model: str
    year: int
    style: str
    distance: float
    engine_capacity: float
    fuel_type: str
    transmission: str


@app.post("/predict", summary="Predict car price")
async def predict(car: CarFeatures):
    try:
        input_data = pd.DataFrame([car.dict()])
        input_data.columns = ["Make", "Model", "Year", "Style", "Distance", "Engine_capacity", "Fuel_type", "Transmission"]
        input_data = clear_data(input_data)
        input_data = featurize(input_data)

        features = scaler.transform(input_data)
        prediction = model.predict(features)[0]
        return {"predicted_price": round(float(prediction), 2)}

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
