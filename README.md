# Flight Fare Prediction System

The Flight Fare Prediction System is a project designed to predict the fare of flights based on various input features, including airline, date of journey, source, destination, duration, time of arrival, total stops, route, and price. The system employs a range of machine learning models, such as Linear Regression, Ridge, Lasso, ElasticNet, Decision Tree Regressor, Random Forest Regressor, and Naive Bayes Regressor, to estimate flight fares. After extensive evaluation, the Naive Bayes Regressor has been identified as the most effective model for predicting flight fares.

## Project Structure

The project is organized into the following key components:

### 1. src Folder

This directory houses the core source code for the Flight Fare Prediction System.

- **exceptions.py:** Manages custom exceptions specific to the project.
- **logger.py:** Offers logging functionality to record events during system execution.
- **utils.py:** Contains utility functions used throughout the project.
- **components Folder:**

  - **data_ingestion.py:** Handles the loading of input data from the "flight_data.csv" file.
  - **data_transformation.py:** Performs data preprocessing and transformation tasks.
  - **model_training.py:** Implements the training of the Gradient Boosting Regressor model.

- **pipelines Folder:**

  - **train_pipeline.py:** Initiates the complete training process, including data ingestion, preprocessing, and model training. The trained model is then saved in the artifacts folder.
  - **predict_pipeline.py:** Loads the trained model and generates fare predictions based on new inputs.

### 2. setup.py

The `setup.py` file contains configuration details pertinent to the Flight Fare Prediction System.

### 3. requirements.txt

The `requirements.txt` file enumerates all necessary libraries and dependencies required for executing the project. Prior to running the system, ensure that these dependencies are installed.

### 4. artifacts Folder

The `artifacts` directory is employed to store pickle files and datasets, including the trained Gradient Boosting Regressor model.

### 5. notebooks Folder

The `notebooks` directory accommodates Jupyter notebooks utilized for exploratory data analysis and experimentation during the project's development.

### 6. application.py

The `application.py` file serves as a Flask web application that provides users with an intuitive interface to input flight details and obtain fare predictions derived from the trained model.

### Dependencies

The Flight Fare Prediction System relies on the following libraries:

- Flask
- seaborn
- scikit-learn
- pandas
- numpy
- flask-cors

## Getting Started

To run the Flight Fare Prediction System, adhere to these steps:

1. Install the necessary dependencies outlined in `requirements.txt`.

2. Run the `application.py` file to launch the Flask web application.

3. It consists different routes for training as well as predicting data

4. Access the application via your preferred web browser and input flight details to acquire fare predictions.

## Contribution

Contributions to the Flight Fare Prediction System are highly encouraged. If you encounter any issues or possess suggestions for enhancement, don't hesitate to submit pull requests or open issues.

Happy fare predicting!