# Production-Grade AI Medical Image Risk Prediction Platform with FastAPI, Docker, RAG Assistant, SQLite, Real-Time ML Inference, and MLOps-Oriented Cloud Deployment

---

## Overview

This project turns an ISIC 2024 skin cancer detection research workflow into a deployed, production-style machine learning API.

Users can upload a skin lesion image through a FastAPI backend and receive a malignant/benign risk prediction from a two-model vision ensemble using ConvNeXt and EVA-02. The API is containerized with Docker, deployed on Google Cloud Run, and includes interactive Swagger documentation, health checks, structured logging, clean backend architecture, and a retrieval-based RAG assistant for project/codebase Q&A.

The goal of this project is not only to build a model inference endpoint, but to demonstrate how machine learning research code can be transformed into a real backend system that is easier to deploy, document, monitor, and extend.

---

## 🚀 Live Demo

Live API: https://isic-api-918647643601.europe-west2.run.app  
Interactive Swagger Docs: https://isic-api-918647643601.europe-west2.run.app/docs  
OpenAPI Schema: https://isic-api-918647643601.europe-west2.run.app/openapi.json  
Health Check: https://isic-api-918647643601.europe-west2.run.app/api/v1/health

> Deployment note: this project is deployed with Docker on **Google Cloud Run**. The API was verified through Cloud Run logs showing successful `200 OK` responses for `/`, `/docs`, and `/openapi.json`.

---

## ✨ Project Highlights

- Built upon the 1st/2nd place winning solution concept of the ISIC 2024 Skin Cancer Detection Challenge
- Transformed a Kaggle / notebook-based workflow into a production-oriented backend system
- Deployed a working FastAPI API on Google Cloud Run with Docker
- Integrated a two-model production inference backend using **ConvNeXt + EVA-02**
- Added real image upload support for malignant/benign skin lesion risk prediction
- Built a retrieval-based RAG assistant for project/codebase technical Q&A
- Added clean architecture, structured logging, health checks, Pydantic schemas, and environment-based configuration
- Configured Cloud Run with warm instance support using `--min-instances 1` for live demo readiness

---

## 📁 Project Structure

```text
src/
├── api/                  # FastAPI routes & main app
├── core/                 # Config, logger, settings
├── db/                   # SQLAlchemy models
├── inference/            # Core ML inference engine
├── rag/                  # RAG Technical Assistant
├── repositories/         # Database repository layer
├── schemas/              # Pydantic request/response models
├── services/             # Business logic
└── __init__.py

notebooks/                # Development & refactoring notebooks
configs/                  # Configuration files
data/                     # Data artifacts / local data references
logs/                     # Application logs
docker/                   # Docker-related deployment assets
```

---

## 🏗️ Tech Stack

Backend: FastAPI, Uvicorn, Pydantic  
ML: PyTorch, TorchVision, Timm, scikit-learn  
Vision Models: ConvNeXt, EVA-02  
RAG: LangChain, FAISS, Sentence Transformers  
Database Layer: SQLAlchemy, SQLite-ready repository layer  
Deployment: Docker, Google Cloud Run, Google Cloud Build  
Logging & Config: structlog, Pydantic Settings  
Notebook Development: Google Colab

---

## 🚀 Key Features

### Core ML Capabilities

- **Two-Model Vision Ensemble**: Uses `convnext_small` and `eva02_small_patch14_336` through PyTorch + Timm for deployed image inference.
- **Model-Specific Image Transforms**: Uses model-specific resize/crop pipelines such as 384px preprocessing for ConvNeXt and 336px preprocessing for EVA-02.
- **Lazy Model Loading**: Models are loaded once and reused for inference through a `models_loaded` flag.
- **Device-Aware Inference**: Automatically selects CUDA when available and CPU otherwise.
- **Mean Ensemble Prediction**: Combines model probabilities through simple ensemble averaging.
- **Real Image Upload Inference Endpoint**: Upload a dermoscopy image and receive a malignant/benign lesion risk prediction.
- **Probability-Based Classification**: Converts malignant probability into benign/malignant prediction labels using the backend prediction flow.

---

### Prediction Logic
The API performs inference using a **two-model ensemble** (ConvNeXt Small + EVA-02 Small):

- Each model processes the uploaded dermoscopy image independently.
- Both models output a probability score for the **malignant** class (after softmax).
- The final probability is the **average** of the two model outputs.
- Classification rule:
  - Probability **< 0.5** → classified as **benign**
  - Probability **≥ 0.5** → classified as **malignant**

This ensemble approach provides a good balance between accuracy and inference speed while keeping the deployment lightweight.

---

### Production Backend

- **FastAPI with Clean Architecture**: Layered structure using API routes, services, repositories, schemas, models, inference, RAG, and core configuration.
- **Async Image Processing**: Handles image uploads with validation before inference.
- **Pydantic v2 Schemas**: Strong type validation and automatic OpenAPI documentation.
- **Structured Logging**: Application logging using structlog JSON rendering.
- **Application Lifespan Hooks**: Logs startup and shutdown events through FastAPI lifespan management.
- **CORS Middleware**: Enables cross-origin usage for web clients, demos, and frontend integration.
- **Image Upload Validation**: Rejects non-image uploads with a meaningful `400` response.
- **Typed Prediction Response**: Returns `isic_id`, probability, prediction, model version, and timestamp.
- **Config Caching**: Uses `@lru_cache()` for efficient settings loading.
- **Environment Configuration**: Uses `.env` with fields such as `APP_NAME`, `API_VERSION`, `MODEL_VERSION`, `DEBUG`, `DATABASE_URL`, and `SECRET_KEY`.

---

### Intelligent RAG Assistant

- **Project-Aware Retrieval Assistant**: Retrieves relevant project source-code context for technical Q&A.
- **Vector Search**: Uses FAISS with Sentence Transformers embeddings.
- **Codebase Indexing**: Indexes Python files from `src/**/*.py` plus a short project summary.
- **Chat Endpoint**: `/api/v1/chat` accepts a question and returns retrieved project context.

---

### Production & Observability

- **SQLite-Ready Persistence Layer**: SQLAlchemy model and repository structure are prepared for future prediction history storage.
- **Repository Pattern**: Encapsulates future database write logic in `PredictionRepository`.
- **Error Handling**: Includes validation and meaningful API errors for unsupported uploads and service-level failures.
- **Health Check Support**: Health endpoint is available for deployment checks and uptime monitoring.
- **Docker Support**: Fully containerized for cloud deployment.
- **Google Cloud Run Deployment**: Deployed with Docker on Google Cloud Run.
- **Google Cloud Build Source Deployment**: Uses `gcloud run deploy --source .` deployment workflow.
- **Warm Instance Setup**: Cloud Run configured with `--min-instances 1` for live demo readiness and reduced cold-start impact.
- **JSON Structured Logs**: structlog is configured with JSON rendering for production log aggregation.
- **Startup/Shutdown Logging**: Application lifecycle events are recorded for easier debugging.

---

### Developer Experience

- **Modular Codebase**: Separated API, service, inference, RAG, schema, config, and repository layers.
- **Notebook-to-Production Workflow**: Refactored setup, inference, backend, RAG, ensemble, and deployment work from notebooks into a deployable project.
- **Deployment Ready**: Containerized for Docker and Google Cloud Run.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Root endpoint confirming the API is running |
| `GET` | `/docs` | Interactive Swagger/OpenAPI documentation |
| `GET` | `/openapi.json` | OpenAPI schema |
| `GET` | `/api/v1/health` | Health check with API and model version |
| `POST` | `/api/v1/predict` | Upload a skin lesion image and receive prediction results |
| `POST` | `/api/v1/chat` | Ask the RAG assistant about the project/codebase |

---

## 🧠 Prediction Response Example

```json
{
  "isic_id": "uploaded_image.jpg",
  "probability": 0.7321,
  "prediction": "malignant",
  "model_version": "2024-ensemble-2models",
  "timestamp": "2026-01-01T12:00:00"
}
```

---

## 🤖 RAG Assistant Example

Request:

```json
{
  "question": "How does the ensemble inference engine work?"
}
```

Response:

```json
{
  "answer": "Context from project: ... Question: How does the ensemble inference engine work?"
}
```

---

## 🐳 Docker

The project is containerized with Docker and deployed successfully on Google Cloud Run. The Dockerfile runs the FastAPI app on port `8080`.

Reference Docker commands:

```bash
docker build -t isic-flagship .
docker run -p 8000:8080 isic-flagship
```

Container startup command:

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port ${PORT:-8080}
```

For Google Cloud Run, the container uses the platform-provided `PORT` environment variable. The deployment can be kept warm with `--min-instances 1` for live demo readiness.

---

## ☁️ Google Cloud Run Deployment

The API is deployed on Google Cloud Run using Docker and Google Cloud Build source deployment.

- **Cloud Platform**: Google Cloud Run
- **Build System**: Google Cloud Build via `gcloud run deploy --source .`
- **Runtime Port**: `8080`
- **Warm Instance Setup**: `--min-instances 1` for live demo readiness
- **Public Access**: `--allow-unauthenticated`
- **API Docs**: Available through FastAPI Swagger UI at `/docs`

Example deployment command from the notebook workflow:

```bash
gcloud run deploy isic-api \
  --source . \
  --region europe-west2 \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 1 \
  --min-instances 1 \
  --max-instances 3 \
  --timeout 300 \
  --port 8080 \
  --cpu-boost
```

Note: This project currently uses Cloud Run source deployment. A fully automated CI/CD pipeline, such as GitHub Actions or Cloud Build triggers on every Git push, is not claimed in this README.

---

## ⚙️ Environment Variables

Example `.env` / `.env.example`:

```env
APP_NAME=ISIC2024-Flagship
API_VERSION=v1
MODEL_VERSION=2024-ensemble-2models
DEBUG=False
DATABASE_URL=sqlite:///./isic.db
SECRET_KEY=change-this-in-google-cloud-run
```

---

## 🏆 Achievements

- Transformed an ISIC 2024-inspired notebook workflow into a deployed ML inference API
- Deployed a working FastAPI backend on Google Cloud Run with Docker
- Integrated ConvNeXt + EVA-02 as the implemented production model ensemble
- Added real image upload inference and interactive Swagger/OpenAPI documentation
- Added a retrieval-based RAG assistant using FAISS and Sentence Transformers
- Structured the project with modular API, service, inference, RAG, schema, config, logging, and SQLite-ready repository layers

---

## ⚠️ Medical Disclaimer

This project is for educational and research purposes only. It is intended only to demonstrate AI-assisted initial screening support. It is not a medical device and should not be used for diagnosis, treatment, or clinical decision-making. Please consult a qualified healthcare professional for further evaluation.
