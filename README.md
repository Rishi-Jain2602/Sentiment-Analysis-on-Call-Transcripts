# Sentiment-Analysis-on-Call-Transcripts
This project evaluate each transcript of phone call, providing sentiment scores to gauge emotions and attitudes in customer interactions.

****
[Sentiment Analysis.webm](https://github.com/user-attachments/assets/bdc7687e-1f92-478f-8ee2-1d8f20e61a8d)

*****
## Installation

1. Clone the Repository
   
``` bash
git clone https://github.com/Rishi-Jain2602/Sentiment-Analysis-on-Call-Transcripts.git
```

2. Create Virtual Environment

```bash
virtualenv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the Project dependencies

Install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit App

Start the Streamlit app with the following command:

```bash
streamlit run app.py
```

5. Run the Backend (Flask App)

Open a new terminal, navigate to the api directory, and run the backend:

```bash
cd api
python sentiment.py
```
****

## Jupyter Notebook Guide

A Jupyter notebook [fiXit.ipynb](https://github.com/Rishi-Jain2602/Sentiment-Analysis-on-Call-Transcripts/blob/main/Jupyter/fixit.ipynb) has been added to this repository, providing a step-by-step implementation guide for the sentiment analysis application. It covers:

1. Performing sentiment analysis
2. Visualizing results

You can open the notebook using Jupyter to follow along with the complete implementation process.

*****

### Tools & Models Used

**Sentiment Analysis Model:** We use the [HuggingFace Pretrained Model link](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student) for sentiment analysis.

### UI Structure

- **Login Credentials:**
  - **Username:** efgh
  - **Password:** 456
- **Input:** Upload a .txt file containing the transcript.

- **Action:** Click the **Sentiment Analysis** button to analyze the sentiment of the uploaded transcript.


******

## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. If the Jupyter notebook doesn't work locally, try running it on Kaggle.
4. For deep learning, a laptop with a powerful GPU, a high-performance CPU, at least 8GB of RAM, a fast SSD, and an efficient cooling system is recommended.
5. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
