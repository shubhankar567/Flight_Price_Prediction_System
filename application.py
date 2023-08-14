from flask import Flask, request, render_template
from src.pipelines.predict_pipeline import CustomData, PredictPipeline
from flask_cors import cross_origin
import pandas as pd
from src.pipelines.train_pipeline import TrainPipeline

application = Flask(__name__)


@cross_origin
@application.route('/')
def home_page():
    return render_template('index.html')

@application.route('/train')
def home_page1():
    train_obj = TrainPipeline()
    train_obj.training()
    return render_template('index_train.html')

@cross_origin
@application.route('/predict', methods = ['GET', 'POST'])  # type: ignore
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else: 
        duration = request.form.get('Duration').split(' ')
        if len(duration) == 2:
            hour = float(duration[0][:-1])
            min = float(duration[1][:-1])
        else:
            hour = 0
            min = float(duration[0][-1])
        data = CustomData(
            Airline = request.form.get('Airline'), # type: ignore 
            Week_Day = pd.to_datetime(request.form.get('Date_of_Journey'), format = '%d/%m/%Y').strftime('%A'), # type: ignore
            Total_Stops = request.form.get('Total_Stops'), # type: ignore
            Duration = hour*60 + min, # type: ignore
        )
        
        # Cnverting the random input data into a dataframe
        input_dataset = data.data_to_dataframe() # type: ignore

        #input_dataset.to_excel('artifacts/processed_data.xlsx', index = False)
        # Predicting
        predict_obj = PredictPipeline()
        output = predict_obj.prediction(input_dataset)

        # Rounding off the result 
        results = round(output[0],2)

        return render_template('form.html', final_result = results)
    
if __name__ == '__main__':
    application.run(host = '0.0.0.0', port = 5000, debug = True)