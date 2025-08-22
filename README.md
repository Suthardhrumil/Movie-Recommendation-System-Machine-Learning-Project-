# 🎬 Movie Recommendation System (Machine Learning Project)

A Movie Recommendation System built using **Python** and **Machine Learning**.  
This project applies **data preprocessing**, **feature engineering**, and **metadata extraction** (genres, cast, crew, keywords, and overviews).  
It uses **text vectorization (CountVectorizer)** and **cosine similarity** to recommend the top 5 similar movies for any given input.

---

## 🚀 Features
- Movie metadata preprocessing (genres, cast, crew, keywords, overview).
- Similarity calculation using **Cosine Similarity**.
- Returns top 5 recommended movies based on user input.
- Interactive implementation with Python.

---

## 📂 Repository Structure
|- app.py                           # Main Python app file

|- Data Preprocessing & ML model building.ipynb   # Jupyter Notebook

|- tmdb-CSV-file.zip                # Sample dataset (zipped)

|- movies.pkl                       # Preprocessed movie metadata

|- similarity.pkl                   # Similarity matrix

|- movie_dict.pkl                   # Movie dictionary

|- README.md                        # Project documentation



---

## 📊 ML Model code Files
Due to GitHub’s **25MB limit**, large files are stored on **Google Drive**.  
You can download them here:  

🔗 [Download Dataset & Pickle Files](https://drive.google.com/drive/folders/1Ut-cunCetJhxDQOnRnOIk4luEinjWTGk?usp=sharing)
  

*(Make sure the Google Drive file is set to **Anyone with the link → Viewer** so users can access it.)*

---

## ⚡ Installation & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Movie-Recommendation-System-Machine-Learning-Project.git
   cd Movie-Recommendation-System-Machine-Learning-Project

2. Install dependencies:
    pip install -r requirements.txt
   
4. Download the Google Drive files and place them in the project root folder.
   
5. Run the app:
   python app.py

📈 Example Output
  Input:Avatar

  Output:
          1. Avatar: The Way of Water
          2. Guardians of the Galaxy
          3. John Carter
          4. Star Trek
          5. The Avengers

🛠️ Tech Stack
    -Python
    -Pandas, NumPy
    -Scikit-learn
    -Pickle
    -Cosine Similarity
