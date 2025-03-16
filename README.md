# Email Spam Classifier 

Machine learning-powered solution for detecting spam emails using Natural Language Processing (NLP) and classification algorithms.

## Features

**Real-Time Classification:** Instant spam/ham prediction through web interface  
**High Accuracy:** Pre-trained model with optimized performance  
**Easy Integration:** Serialized model and vectorizer for quick deployment  
**Web Interface:** User-friendly Flask-based application  
**Scalable:** Modular design for model updates and enhancements  

## Technologies Used

- **Machine Learning:** Naive Bayes Classifier (presumed from .pkl files)
- **NLP:** TF-IDF Vectorization
- **Web Framework:** Flask (app.py)
- **Persistent Storage:** Pickle serialization (.pkl files)
- **Python Libraries:** Scikit-learn, Pandas, Numpy

## Installation

1. **Clone repository**  
`git clone https://github.com/its308/Email-Spam-Classifier-Updated.git`

2. **Install requirements**  
`pip install -r requirements.txt`

3. **Run Flask application**  
`python app.py`

The application will start at `http://localhost:5000`

## Usage

1. Access the web interface at `http://localhost:5000`
2. Paste email text into the input field
3. Click "Classify" to get prediction
4. Results displayed as:
   - **Not Spam** (green)
   - **Spam** (red)

## File Structure
## Contributing

1. Fork the repository
2. Create feature branch:  
`git checkout -b feature/new-feature`
3. Commit changes:  
`git commit -m 'Add some feature'`
4. Push to branch:  
`git push origin feature/new-feature`
5. Open pull request

## License

[MIT License](LICENSE) (assumed - create LICENSE file if missing)
