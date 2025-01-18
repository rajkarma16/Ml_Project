# Crime Prediction Model

This project is a machine learning-based crime prediction system that uses historical data to forecast the frequency of crimes in various areas. The system processes time-series data and applies lagged features and regression models for forecasting future crime trends.

## Features

- **Time-Series Analysis**: Processes crime data over time to identify trends.
- **Lagged Features**: Utilizes past crime data as predictors for future events.
- **Machine Learning**: Implements Random Forest Regressor for forecasting.
- **Data Visualization**: Provides insights using plots for crime distribution and predictions.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

Install the dependencies using:
```bash
pip install -r requirements.txt
```

## Files in Repository

- `crime.ipynb`: Main Jupyter notebook containing the code for data preprocessing, modeling, and visualization.
- `requirements.txt`: List of dependencies required to run the project.
- `predictions.pkl`: Pickle file for saving model predictions.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crime-prediction.git
   cd crime-prediction
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook crime.ipynb
   ```

3. Follow the steps in the notebook to:
   - Load and preprocess the crime dataset.
   - Generate lagged features for time-series modeling.
   - Train the Random Forest Regressor.
   - Evaluate the model and visualize the results.

4. Save predictions:
   - The notebook automatically saves predictions as `predictions.pkl`.

## Visualization Examples

### Crime Distribution by Area

![Crime Distribution](images/crime_distribution.png)

### Predicted Crime Trends

![Crime Trends](images/predicted_trends.png)

## Evaluation Metrics

The model is evaluated using:

- **Mean Absolute Error (MAE)**: Average magnitude of errors.
- **Root Mean Squared Error (RMSE)**: Square root of the average squared errors.
- **Mean Absolute Percentage Error (MAPE)**: Percentage error relative to actual values.

## Future Enhancements

- Add support for additional machine learning models.
- Implement a Flask or Django API for real-time predictions.
- Expand dataset for better accuracy and broader geographic coverage.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute or raise issues for improvements!
