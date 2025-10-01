# 🎬 Movie Recommendation System

A personalized Movie Recommendation System that suggests movies based on user preferences using Collaborative Filtering and SVD (Matrix Factorization). The system also integrates movie posters for better user experience and is deployed on Hugging Face Spaces for real-time interaction.

# 🚀 Features

✅ Collaborative Filtering-based recommendations

✅ SVD (Matrix Factorization) for handling sparse data

✅ Integration with OMDb API to fetch movie posters

✅ Performance evaluation with Precision@K, Recall@K, and NDCG

✅ Live demo deployed on Hugging Face Spaces

👉 Try it here: https://huggingface.co/spaces/Ripon2/DataSynthis_Job_task

# 📂 Project Structure

<img width="550" height="251" alt="image" src="https://github.com/user-attachments/assets/0a122a8f-0813-4193-8192-aea7f982c2fc" />


⚙️ Installation

Clone the repo and install dependencies:

## ⚙️ Installation  

Clone the repository and install the required dependencies:  

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
```


# ▶️ Usage
```bash
python app.py
```
Run the system locally:

Or open the Hugging Face Spaces demo:
👉 Movie Recommendation System : https://huggingface.co/spaces/Ripon2/DataSynthis_Job_task

<img width="1867" height="952" alt="image" src="https://github.com/user-attachments/assets/f060f145-8fdb-4e8e-95d7-c73223916eaf" />

<img width="1864" height="947" alt="image" src="https://github.com/user-attachments/assets/67bf5a18-e1f4-4534-8553-1c5100cdfe2e" />

# 📊 Evaluation Metrics

The model was evaluated using:

Precision@K

Recall@K

Normalized Discounted Cumulative Gain (NDCG)

# 🛠️ Tech Stack

Python

Pandas, NumPy, Scikit-learn

SVD (Matrix Factorization)

OMDb API (for posters)

Gradio / Streamlit (for deployment)

Hugging Face Spaces

# 💡 Learnings

SVD performs better than vanilla collaborative filtering on sparse data.

Movie metadata (like posters) greatly improves user engagement.

Deployment makes ML projects accessible and interactive.

📜 License

This project is licensed under the MIT License.
