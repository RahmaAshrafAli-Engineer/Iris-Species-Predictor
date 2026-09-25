# 🪻 Iris Species Predictor

### Machine Learning Classification App | Logistic Regression | Streamlit

An interactive Machine Learning web application that predicts the species of an Iris flower from its physical measurements using a trained **Logistic Regression** model.

The project combines **Machine Learning model development** with **interactive web deployment using Streamlit**, turning a trained classification model into a user-friendly application.

---

## 🚀 Live Demo

🔗 **Try the App:** `YOUR_STREAMLIT_APP_URL`

🔗 **GitHub Repository:** `https://github.com/RahmaAshrafAli-Engineer/Iris-Species-Predictor/blob/main/README.md`

---

## 🎯 Project Objective

The goal of this project is to build a complete Machine Learning classification workflow — from preparing the dataset and training the model to integrating the trained model into an interactive web application.

Given four measurements of an Iris flower, the application predicts its species:

* 🌱 **Setosa**
* 🌸 **Versicolor**
* 🌺 **Virginica**

---

## 🧠 Machine Learning Model

### Logistic Regression

The application uses **Logistic Regression**, a supervised Machine Learning classification algorithm.

The model receives four numerical features:

| Feature      | Description                        |
| ------------ | ---------------------------------- |
| Sepal Length | Length of the sepal in centimeters |
| Sepal Width  | Width of the sepal in centimeters  |
| Petal Length | Length of the petal in centimeters |
| Petal Width  | Width of the petal in centimeters  |

The trained model then returns:

**Predicted Species + Prediction Probabilities**

---

## 📊 Model Performance

**Test Accuracy:** ~96.7%

The model was evaluated on a held-out test set to measure its classification performance.

> The reported accuracy depends on the train/test split and model configuration used during training.

---

## 🔄 Machine Learning Workflow

```text
Iris Dataset
     ↓
Data Preparation
     ↓
Train / Test Split
     ↓
Logistic Regression
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Serialization (.pkl)
     ↓
Streamlit Application
     ↓
Interactive Prediction
```

---

## ✨ Application Features

### 🌸 Interactive Prediction

Users can adjust the flower measurements using interactive sliders.

### 🤖 Real-Time Classification

The trained Logistic Regression model predicts the Iris species instantly.

### 📈 Prediction Probabilities

The application displays the probability associated with each predicted species.

### 🖼️ Visual Result

The predicted Iris species is displayed together with a representative flower image.

### 💻 Interactive Web Interface

The entire Machine Learning model is accessible through a simple Streamlit interface without requiring users to interact with Python code.

---

## 🛠️ Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| 🐍 Python           | Programming language |
| 🧮 NumPy            | Numerical operations |
| 🐼 Pandas           | Data manipulation    |
| 🤖 Scikit-learn     | Machine Learning     |
| 🎨 Streamlit        | Web application      |
| 📦 Pickle           | Model serialization  |
| 📓 Jupyter Notebook | Model development    |

---

## 📁 Project Structure

```text
Iris-Species-Predictor/
│
├── iris_species_predictor.py
├── iris_logistic_regression_model.pkl
├── requirements.txt
├── README.md
│
└── images/
    └── iris-app.png
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd Iris-Species-Predictor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run iris_species_predictor.py
```

The application will open locally in your browser.

---

## 🧪 Example Input

For example:

```text
Sepal Length: 5.4 cm
Sepal Width: 3.1 cm
Petal Length: 1.5 cm
Petal Width: 0.2 cm
```

The model can then classify the flower based on the learned patterns from the Iris dataset.

---

## 📚 Dataset

This project uses the classic **Iris Dataset**, a well-known dataset for introductory Machine Learning classification.

The dataset contains measurements of Iris flowers belonging to three species:

* Setosa
* Versicolor
* Virginica

Each sample contains four numerical features:

`Sepal Length`, `Sepal Width`, `Petal Length`, and `Petal Width`.

---

## 💡 What I Learned

Through this project, I practiced:

* Building a supervised Machine Learning classification model
* Understanding and applying Logistic Regression
* Preparing numerical input data for prediction
* Evaluating classification performance
* Saving a trained model using Pickle
* Loading a trained model into another Python application
* Building an interactive Machine Learning interface with Streamlit
* Connecting a Machine Learning model to a deployable web application

---

## 🔮 Future Improvements

Possible future improvements include:

* Adding additional classification algorithms
* Comparing model performance
* Adding a confusion matrix and classification report
* Improving the UI/UX
* Adding more visual analytics
* Deploying the application publicly
* Adding automated model retraining

---

## 👩‍💻 Author

**Rahma Ashraf Ali Faragallah**

Machine Learning & AI Enthusiast

---

⭐ If you find this project useful, feel free to explore the repository and try the application.

