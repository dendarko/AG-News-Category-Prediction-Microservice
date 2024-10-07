
# AG News Category Prediction Microservice

## Project Overview

This project involves building and deploying a microservice that classifies news articles into predefined categories (World, Sports, Business, and Sci/Tech) using the **AWD_LSTM ULMFiT** model. The microservice is deployed on **Google Cloud Run**, providing a scalable and low-latency solution for real-time news classification.

## Key Features

- **High Accuracy**: Achieved **88% accuracy** on the AG News dataset using transfer learning with ULMFiT.
- **Automated News Categorization**: Classifies news articles based on their content into predefined categories.
- **Deployed on Google Cloud Run**: Leveraging the scalability and flexibility of cloud infrastructure to handle varying loads.
- **Dockerized Application**: The service is containerized using Docker for easy deployment and portability.

## Project Components

- **AG News Dataset**: The dataset contains 96,000 news articles categorized into four classes: World, Sports, Business, and Sci/Tech. A subset (10%) was used for training and validation.
- **AWD_LSTM ULMFiT Model**: Transfer learning model fine-tuned for text classification.
- **API Endpoint**: The deployed microservice provides an API that accepts text input and returns the predicted category.
- **Google Cloud Run Deployment**: The service was deployed using Google Cloud Run with Docker, ensuring low latency and automatic scaling based on incoming requests.

## Dataset

- **AG News Dataset**: Available [here](https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/train.csv).

## Technical Implementation

1. **Model Training**:
   - **AWD_LSTM** architecture was fine-tuned using the **ULMFiT** method to achieve optimal performance on the AG News dataset.
   - A subset of the dataset (10%) was used for training to optimize resource usage while maintaining high accuracy.

2. **Service Deployment**:
   - The microservice was containerized using **Docker** and deployed on **Google Cloud Run**.
   - Google Cloud SDK was used for deployment, and a Cloud Storage bucket was created to store the model and related files.

3. **API Development**:
   - The microservice exposes an API endpoint that accepts text as input and returns the predicted news category.
   - API Endpoint: [AG News Category Prediction](https://agnews-category-prediction-5kvzr252lq-uc.a.run.app/)

## How to Run

### Prerequisites

- Python 3.8 or higher
- Docker installed
- Google Cloud SDK installed

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ag-news-category-prediction.git
   cd ag-news-category-prediction
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t agnews-microservice .
   ```

3. **Run the service locally**:
   ```bash
   docker run -p 8080:8080 agnews-microservice
   ```

4. **Deploy to Google Cloud Run**:
   ```bash
   gcloud run deploy agnews-category-prediction --source . --region us-central1 --allow-unauthenticated
   ```

## Challenges and Solutions

- **Deployment Issues on macOS**: The Google Cloud SDK had issues with installation due to Homebrew not being in the system’s PATH. This was resolved by manually configuring the environment.
- **Windows OS Deployment**: Encountered "Service Unavailable" errors during deployment, but the issues were resolved after multiple testing and configuration adjustments.

## Future Work

- Expand the model to include additional news categories.
- Implement sentiment analysis within each category for deeper insights.
- Further optimize the model and microservice for better performance and lower latency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
