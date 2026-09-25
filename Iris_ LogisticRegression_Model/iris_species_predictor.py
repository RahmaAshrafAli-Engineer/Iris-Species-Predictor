import pickle
import numpy as np
import pandas as pd
import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🪻",
    layout="centered",
)

MODEL_PATH = "iris_logistic_regression_model.pkl"

SPECIES_NAMES = ["Setosa", "Versicolor", "Virginica"]
SPECIES_IMAGES = {
    "Setosa": "https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg",
    "Versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "Virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
}


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model


def main():
    st.title("🪻 Iris Flower Species Predictor")
    st.write(
        "Enter the flower's measurements below and the model will predict "
        "which Iris species it most likely belongs to, using a "
        "**Logistic Regression** model trained on the classic Iris dataset."
    )

    try:
        model = load_model()
    except FileNotFoundError:
        st.error(
            f"Model file `{MODEL_PATH}` not found. Make sure it's in the "
            "same folder as this app."
        )
        st.stop()

    st.divider()
    st.subheader("Flower measurements (cm)")

    # Sliders with ranges matching the real Iris dataset
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.4, 0.1)
        petal_length = st.slider("Petal Length", 1.0, 7.0, 3.8, 0.1)
    with col2:
        sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.1, 0.1)
        petal_width = st.slider("Petal Width", 0.1, 2.5, 1.2, 0.1)

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    st.divider()

    if st.button("Predict Species", type="primary", use_container_width=True):
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        predicted_species = SPECIES_NAMES[prediction]

        st.success(f"### Predicted Species: **{predicted_species}**")

        img_col, prob_col = st.columns([1, 1.3])

        with img_col:
            st.image(
                SPECIES_IMAGES[predicted_species],
                caption=f"Iris {predicted_species}",
                use_container_width=True,
            )

        with prob_col:
            st.write("**Prediction confidence:**")
            prob_df = pd.DataFrame(
                {"Species": SPECIES_NAMES, "Probability": probabilities}
            ).set_index("Species")
            st.bar_chart(prob_df)
            for name, prob in zip(SPECIES_NAMES, probabilities):
                st.write(f"- {name}: {prob * 100:.1f}%")

    st.divider()
    with st.expander("ℹ️ About this app"):
        st.write(
            """
            - **Model:** Logistic Regression (scikit-learn)
            - **Dataset:** Iris (150 samples, 3 species, 4 features)
            - **Test accuracy:** ~96.7%
            - Built with Streamlit
            """
        )


if __name__ == "__main__":
    main()
