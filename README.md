#  Diamond Price Prediction Web App
## Project Video:-
[![Project Video](https://img.youtube.com/vi/JQsAD4AEKsY/maxresdefault.jpg)](https://youtu.be/JQsAD4AEKsY)


### Overview
The Diamond Price Prediction Web App is a user-friendly and interactive web application designed to predict the price of diamonds based on various attributes. This project demonstrates the integration of a machine learning model with a web interface to provide a seamless experience for users interested in estimating the value of their diamonds.

### **Features:**
- Input Form: Users can input various attributes of a diamond, including carat, depth, table, dimensions (x, y, z), cut, color, and clarity.
- Machine Learning Prediction: The application uses a trained machine learning model to predict the price of the diamond based on the provided attributes.
- User-Friendly Interface: The web app features an attractive and intuitive interface, making it easy for users to enter data and receive predictions.
- Background Image: The app uses a captivating background image to enhance the visual appeal and engagement of users.


###  **Dataset Information:**
The dataset used in the Diamond Price Prediction Web App project is a collection of diamond attributes and their corresponding prices. The dataset is utilized to train a machine learning model that can predict the price of a diamond based on its various characteristics. The dataset provides a valuable resource for understanding the relationships between diamond attributes and their market values.

### **Attributes in the Dataset:**
- `carat`: Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
- `cut`: Quality of Diamond Cut.
- `color`: Color of Diamond.
- `clarity`: Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
- `depth`: The depth of the diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface).
- `table`: A diamond's table is the facet which can be seen when the stone is viewed face up.
- `x`: Diamond X dimension.
- `y`: Diamond Y dimension.
- `z`: Diamond Z dimension.
  
### **Technologies Used:**
- Front-End: HTML, CSS
- Back-End: Python (Flask framework)
- MachineLearning: Linear Regression, Lasso Regression, Ridge Regression, Decision Tree

## **How to run?:**
### Step 1: Clone the repository
git clone https://github.com/saksham-bhardwaj1/Diamond_Price_Prediction

### Step 2- Create a conda environment after opening the repository
conda create -p venv python==3.8
conda activate venv/

### Step 3 - Install the requirements
pip install -r requirements.txt

### Step 4 - Run the application server
python application.py

### Step 5-
1. Visit the web app. :- http://127.0.0.1:5000/
2. Enter the attributes of the diamond in the input form.
3. Click the "Predict" button.
4. Receive the predicted price of the diamond.

## **Contributions:**
Contributions to this project are welcome! If you have ideas for improvement, bug fixes, or additional features, feel free to create a pull request or open an issue.


