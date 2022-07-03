from flask import Flask, render_template, request
import pickle
import pandas as pd
import typeconv as tp
import newdata

model = pickle.load(open('traffic_model.pkl','rb'))

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/pred',methods=["POST"])
def pred():
      a = request.form['hour']
      b = request.form['min']
      c = request.form['day']
      new_data=[[a,b,c]]
      newdf = newdata.new_dataframe(new_data)
      dataframe_after_typeconv=tp.typeconvo(newdf)
      dataframe_after_typeconv['hour'] = dataframe_after_typeconv['hour'].astype(int)
      dataframe_after_typeconv['min'] = dataframe_after_typeconv['min'].astype(int)
      predict_value = model.predict(newdf)

      return render_template('index.html', data = predict_value)
     
if __name__ == "__main__":
    app.run(debug=True)
