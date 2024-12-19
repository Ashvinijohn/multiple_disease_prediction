# from flask import Flask, render_template, request, jsonify
# import joblib
# import numpy as np


# app=Flask(__name__)
# # instantiate object

# #loading the different saved model for different disease
# model = joblib.load('diabetes_model.sav')
# model = joblib.load('heart_disease_model.sav')
# model = joblib.load('parkinssons_model.sav')
# model = joblib.load('breast_Cancer_Classifier.sav')
# model = joblib.load('oasis_model.sav')


# @app.route('/') # instancing one page (homepage)
# def home():
#     return render_template("home.html")
# # ^^ open home.html, then see that it extends layout.
# # render home page.

# @app.route('/diabetes') # instancing child page
# def diabetes():
#     return render_template("diabetes.html")


# @app.route('/parkinsons/') # instancing child page
# def parkinsons():
#     return render_template("parkinsons.html") 

# @app.route('/heartdisease/') # instancing child page
# def heartdisease():
#     return render_template("heartdisease.html")

# @app.route('/breastcancer/') # instancing child page
# def heartdisease():
#     return render_template("breastcancer.html")

# @app.route('/oasislongitudinal/') # instancing child page
# def heartdisease():
#     return render_template("oasislongitudinal.html")



# @app.route('/predictdiabetes/',methods=['POST']) 
# def predictdiabetes():      #function to predict diabetes
#     int_features=[x for x in request.form.values()]
#     processed_feature_diabetes=[np.array(int_features,dtype=float)]
#     prediction=diabetes_predict.predict(processed_feature_diabetes)
#     if prediction[0]==1:
#         display_text="This person has Diabetes"
#     else:
#         display_text="This person doesn't have Diabetes"
#     return render_template('diabetes.html',output_text="Result: {}".format(display_text))

# @app.route('/predictparkinson/',methods=['POST']) 
# def predictparkinsons():      #function to predict parkinsons disease
#     int_features=[x for x in request.form.values()]
#     processed_feature_parkinsons=[np.array(int_features,dtype=float)]
#     prediction=parkinsons_predict.predict(processed_feature_parkinsons)
#     if prediction[0]==1:
#         display_text="This person has Parkinson's"
#     else:
#         display_text="This person doesn't have Parkinson's"
#     return render_template('parkinsons.html',output_text="Result: {}".format(display_text))

# @app.route('/predictheartdisease/',methods=['POST']) 
# def predictheartdisease():      #function to predict heart disease
#     int_features=[x for x in request.form.values()]
#     processed_feature_heart=[np.array(int_features,dtype=float)]
#     prediction=heart_predict.predict(processed_feature_heart)
#     if prediction[0]==1: 
#         display_text="This person has Heart Disease"
#     else:
#         display_text="This person doesn't have Heart Disease"
#     return render_template('heartdisease.html',output_text="Result: {}".format(display_text))

# @app.route('/predictbreastcancer/',methods=['POST']) 
# def predictbreastcancer():      #function to predict heart disease
#     int_features=[x for x in request.form.values()]
#     processed_feature_cancer=[np.array(int_features,dtype=float)]
#     prediction=breast_cancer_predict.predict(processed_feature_cancer)
#     if prediction[0]==1: 
#         display_text="This person has Breast Cancer"
#     else:
#         display_text="This person doesn't have Breast Cancer"
#     return render_template('breastcancer.html',output_text="Result: {}".format(display_text))

# @app.route('/predictoasislongitudinal/',methods=['POST']) 
# def predictoasislongitudinal():      #function to predict heart disease
#     int_features=[x for x in request.form.values()]
#     processed_feature_oasis=[np.array(int_features,dtype=float)]
#     prediction=oasis_longitudinal_predict.predict(processed_feature_oasis)
#     if prediction[0]==1: 
#         display_text="This person has Alheimers Disease"
#     else:
#         display_text="This person doesn't have Alheimers Disease"
#     return render_template('oasislongitudinal.html',output_text="Result: {}".format(display_text))



# if __name__=="__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib

app = Flask(__name__)

# Load the different saved models for different diseases
diabetes_predict = joblib.load('diabetes_model.sav')
heart_predict = joblib.load('heart_disease_model.sav')
parkinsons_predict = joblib.load('parkinssons_model.sav')
breast_cancer_predict = joblib.load('Breast_Cancer_Classifier.sav')
oasis_longitudinal_predict = joblib.load('oasis_model.sav')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/parkinsons/')
def parkinsons():
    return render_template("parkinsons.html")

@app.route('/heartdisease/')
def heartdisease():
    return render_template("heartdisease.html")

@app.route('/breastcancer/')
def breastcancer():
    return render_template("breastcancer.html")

@app.route('/oasislongitudinal/')
def oasislongitudinal():
    return render_template("oasislongitudinal.html")

# Prediction routes for each disease
@app.route('/predictdiabetes/', methods=['POST'])
def predictdiabetes():
    int_features = [float(x) for x in request.form.values()]
    processed_feature_diabetes = [np.array(int_features)]
    prediction = diabetes_predict.predict(processed_feature_diabetes)
    if prediction[0] == 1:
        display_text = "This person has Diabetes" 
    else:
         "This person doesn't have Diabetes"
    return render_template('diabetes.html', output_text="Result: {}".format(display_text))

@app.route('/predictparkinson/', methods=['POST'])
def predictparkinsons():
    int_features = [float(x) for x in request.form.values()]
    processed_feature_parkinsons = [np.array(int_features)]
    prediction = parkinsons_predict.predict(processed_feature_parkinsons)
    if prediction[0] == 1:
        display_text = "This person has Parkinson's"  
    else:
        "This person doesn't have Parkinson's"
    return render_template('parkinsons.html', output_text="Result: {}".format(display_text))

@app.route('/predictheartdisease/', methods=['POST'])
def predictheartdisease():
    int_features = [float(x) for x in request.form.values()]
    processed_feature_heart = [np.array(int_features)]
    prediction = heart_predict.predict(processed_feature_heart)
    if prediction[0] == 1:
        display_text = "This person has Heart Disease" 
    else :
        "This person doesn't have Heart Disease"
    return render_template('heartdisease.html', output_text="Result: {}".format(display_text))

@app.route('/predictbreastcancer/', methods=['POST'])
def predictbreastcancer():
    int_features = [float(x) for x in request.form.values()]
    processed_feature_cancer = [np.array(int_features)]
    prediction = breast_cancer_predict.predict(processed_feature_cancer)
    if prediction[0] == 1:
        display_text = "This person has Breast Cancer"  
    else:
         "This person doesn't have Breast Cancer"
    return render_template('breastcancer.html', output_text="Result: {}".format(display_text))

@app.route('/predictoasislongitudinal/', methods=['POST'])
def predictoasislongitudinal():
    int_features = [float(x) for x in request.form.values()]
    processed_feature_oasis = [np.array(int_features)]
    prediction = oasis_longitudinal_predict.predict(processed_feature_oasis)
    if prediction[0] == 1:
        display_text = "This person has Alzheimer's Disease" 
    else :
        "This person doesn't have Alzheimer's Disease"
    return render_template('oasislongitudinal.html', output_text="Result: {}".format(display_text))

if __name__ == "__main__":
    app.run(debug=True)
