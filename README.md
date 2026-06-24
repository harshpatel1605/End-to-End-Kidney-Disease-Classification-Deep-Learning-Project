# 🩺 Kidney Disease Classification: End-to-End Deep Learning System

An end-to-end **Deep Learning system** that classifies kidney CT scan images as **Normal** or **Tumor**, enabling automated medical image analysis through a scalable and production-ready pipeline.

Built with **TensorFlow, VGG16/EfficientNet, FastAPI, DVC, MLflow, Docker**, and deployed on **AWS EC2 with ECR**, following modern **MLOps and Deep Learning Engineering** practices.

---

## 🚀 Project Highlights

* 🧠 **Medical Image Classification**: Detects kidney tumors from CT scan images.
* 🔬 **Transfer Learning**: Utilizes pretrained CNN architectures (VGG16/EfficientNet) for improved performance.
* 🧪 **MLOps Integration**: Experiment tracking with MLflow and reproducible pipelines with DVC.
* 🧱 **Modular Pipeline Architecture**: Separate stages for ingestion, preprocessing, training, and evaluation.
* ⚡ **FastAPI Inference Service**: Real-time image prediction through REST APIs.
* 📦 **Dockerized Deployment**: Containerized application for portability and scalability.
* 🔁 **CI/CD Pipeline**: Automated deployment using GitHub Actions, AWS ECR, and EC2.
* 📊 **Data Versioning**: Dataset and pipeline reproducibility using DVC.

---

## 📊 Dataset Overview

* **Dataset Type**: Kidney CT Scan Images
* **Classes**:

  * Normal
  * Tumor
* **Total Images**: ~7,000

  * Normal: ~5,000
  * Tumor: ~2,000
* **Image Size**: 224 × 224 × 3

---

## 🔬 Data Preprocessing

* Image resizing to 224×224 pixels
* Pixel normalization using ImageDataGenerator
* Training-validation split
* Data augmentation:

  * Rotation
  * Horizontal flipping
  * Width & height shifting
  * Zooming
  * Shearing
* Class imbalance handling using class weights

---

## 🧠 Deep Learning Model

| Model                   | Description                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| VGG16 Transfer Learning | Pretrained ImageNet weights with custom classification head               |
| EfficientNetB0          | Lightweight CNN architecture for improved performance and inference speed |

### Training Features

* Transfer Learning
* Fine-Tuning
* Early Stopping
* Model Checkpointing
* Learning Rate Scheduling
* Class Weight Balancing

### Evaluation Metrics

* Accuracy
* Loss
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Experiment Tracking

* MLflow Integration
* Parameter Logging
* Metric Tracking
* Model Artifact Storage

---

## ⚙️ Deep Learning Pipeline Stages (DVC)

| Stage                | Description                                |
| -------------------- | ------------------------------------------ |
| `data_ingestion`     | Downloads and extracts image dataset       |
| `prepare_base_model` | Loads pretrained CNN architecture          |
| `model_training`     | Trains transfer learning model             |
| `model_evaluation`   | Evaluates model and logs metrics to MLflow |

Run the complete pipeline:

```bash
dvc repro
```

---

## ⚙️ API Endpoints (FastAPI)

| Endpoint   | Method | Description                          |
| ---------- | ------ | ------------------------------------ |
| `/`        | GET    | Serves image upload interface        |
| `/predict` | POST   | Returns kidney classification result |
| `/train`   | GET    | Triggers model training pipeline     |

---

## 🖥️ Frontend

* User-friendly image upload interface
* Real-time prediction results
* Displays:

  * Predicted Class
  * Confidence Score
  * Uploaded CT Scan Image
* Responsive design for desktop and mobile devices

---

## 🚢 Deployment

### Docker

Containerized using Docker for consistent deployment across environments.

### CI/CD Pipeline

Implemented using GitHub Actions with three stages:

1. **Continuous Integration**

   * Code checkout
   * Dependency installation
   * Pipeline validation

2. **Continuous Delivery**

   * Docker image build
   * Push image to AWS ECR

3. **Continuous Deployment**

   * Pull latest image on EC2
   * Run updated container using self-hosted runner

### Cloud Infrastructure

* AWS EC2
* AWS Elastic Container Registry (ECR)
* GitHub Self-Hosted Runner

---

## 🛠 Tech Stack

| Layer                   | Tools                    |
| ----------------------- | ------------------------ |
| **Deep Learning**       | TensorFlow, Keras        |
| **Transfer Learning**   | VGG16, EfficientNetB0    |
| **Experiment Tracking** | MLflow                   |
| **Data Versioning**     | DVC                      |
| **Backend**             | Python, FastAPI, Uvicorn |
| **Frontend**            | HTML, CSS, JavaScript    |
| **Deployment**          | Docker, AWS EC2, AWS ECR |
| **CI/CD**               | GitHub Actions           |
| **Cloud Storage**       | AWS S3                   |
| **Version Control**     | Git, GitHub              |

---

## 📁 Project Structure

```text
End-to-End-Kidney-Disease-Classification-Deep-Learning-Project/
├── .github/
│   └── workflows/
│       └── main.yaml
├── artifacts/
│   ├── data_ingestion/
│   ├── prepare_base_model/
│   ├── training/
│   │   └── model.h5
│   └── model_evaluation/
├── config/
│   └── config.yaml
├── params.yaml
├── research/
│   └── trials.ipynb
├── src/
│   └── KidneyDiseaseClassification/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── prepare_base_model.py
│       │   ├── model_training.py
│       │   └── model_evaluation.py
│       ├── pipelines/
│       │   ├── stage_01_data_ingestion.py
│       │   ├── stage_02_prepare_base_model.py
│       │   ├── stage_03_model_training.py
│       │   ├── stage_04_model_evaluation.py
│       │   └── prediction_pipeline.py
│       ├── config/
│       │   └── configuration.py
│       ├── entity/
│       │   └── config_entity.py
│       ├── constants/
│       │   └── __init__.py
│       └── utils/
│           ├── common.py
│           ├── logger.py
│           └── exception.py
├── templates/
│   └── index.html
├── app.py
├── main.py
├── dvc.yaml
├── dvc.lock
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

## 📈 Future Improvements

* Multi-class kidney disease classification
* Model explainability using Grad-CAM
* Automated retraining pipeline
* Kubernetes deployment
* Model monitoring and drift detection
* Integration with cloud object storage

---

## 🤝 Contributing

Contributions are welcome! Feel free to improve the model architecture, optimize deployment, enhance the UI, or add new MLOps features by opening a pull request.

---

## 📬 Contact

* **Email**: [harshpatel16052005.email@gmail.com](mailto:harshpatel16052005.email@gmail.com)
* **LinkedIn**: https://linkedin.com/in/harsh-patel-581352358
* **GitHub**: https://github.com/harshpatel1605

---

## 📎 License

This project is licensed under the MIT License. See the LICENSE file for more details.
