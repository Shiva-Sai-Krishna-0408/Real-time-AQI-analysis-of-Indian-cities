## Climate-Risk-Intelligence
AI-powered climate risk scoring system for Indian cities

## Project Overview
This project Climate Risk Intelligence measures the data of the Air Quality across the cities in India and gives a visual representation on it's map. The project involves pulling real-time data from a website's external server using an API key and uses python libraries like NumPy and Pandas for cleaning and filtration.

It also uses Machine Learning - Random Forest Regressor model to train and test the model. Finally, it uses folium to visualize the cleaned data and to represent in a very readable manner. This data visualization is made public for easy access in the Streamlit website.

## Live Demo
[Climate Risk Intelligence System](https://climate-risk-india-intelligence.streamlit.app/)

## Tech Stack
- **Data Collection**: Python, Requests, OpenAQ API
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (Random Forest Regressor)
- **Visualization**: Folium, Streamlit
- **Environment**: Jupyter Notebook, VS Code

## Project Structure 
```
climate-risk-intelligence/
├── data/
│   ├── india_aqi_locations.csv
│   ├── india_aqi_final.csv
│   ├── india_features.csv
│   └── india_features_v2.csv
├── notebooks/
│   ├── 01_data_collection.ipynb
│   └── 02_visualization.ipynb
├── outputs/
│   └── india_risk_map.html
├── app.py
├── requirements.txt
└── README.md
```

## How It Works
1. The real-time data is sourced from OpenAQ using a unique API key.
2. The data is then filtered using Python libraries - NumPy and Pandas.
3. Using the filtered data, data exploration is done and numerous new columns are created and added to the existing dataframe.
4. Using Machine Learning - Random Forest Regressor, the model is trained with the data in hand.
5. Model prediction is performed and absolute error is calculated.
6. Using Folium, the data is visualized and is being presented in a website using Streamlit

## Results
1. The final dataset has about 13 Indian cities whose real-time data is visualized on an Indian map.
2. The Mean Absolute Error - MAE is found to be 4.7.
3. The pattern we can observe here is that North Indian cities like Delhi, Gurgoan and Rohtak have a slightly bad Air Quality when compared to South Indian cities like Hyderabad and Eastern cities like Kolkata.

## How to Run

1. Clone the repository
   git clone https://github.com/Shiva-Sai-Krishna-0408/Climate-Risk-Intelligence.git

2. Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\Activate.ps1

3. Install dependencies
   pip install -r requirements.txt

4. Run the Streamlit app
   streamlit run app.py
