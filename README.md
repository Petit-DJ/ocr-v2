# OCR Backend

A production-oriented OCR backend built with **FastAPI** following Clean Architecture principles. The project focuses on building a scalable, maintainable document processing pipeline with clear separation of concerns.

The backend accepts document uploads, stores metadata, extracts text using **PaddleOCR**, persists OCR results in the database, and exposes the processed document through a REST API.

---

# Features

## Document Upload

* Upload PDF and image documents
* Store uploaded files on disk
* Generate unique filenames
* Track file metadata

## OCR Pipeline

* Convert PDFs into images using **PyMuPDF**
* Extract text using **PaddleOCR**
* Normalize extracted text
* Store OCR output in the database
* Return extracted text through the API

## Database

* SQLAlchemy ORM
* Alembic migrations
* PostgreSQL support
* UUID-based document IDs

## Architecture

* Clean Architecture
* Repository Pattern
* Service Layer
* Dependency Injection
* Modular package structure
* Pydantic response models

# Tech Stack

* Python 3.12+
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* PaddleOCR
* PaddlePaddle
* PyMuPDF
* Pydantic
* Uvicorn
* UV

---

# Project Structure

```
app/
│
├── core/
│
├── db/
│
├── docs/
│   ├── models.py
│   ├── repository.py
│   ├── router.py
│   ├── schemas.py
│   └── service.py
│
├── processing/
│   ├── pipeline.py
│   └── stages/
│       ├── pdf.py
│       └── ocr.py
│
├── storage/
│   └── service.py
│
├── uploads/
│
└── main.py
```

---

# Architecture

```
                Client
                   │
                   ▼
            FastAPI Router
                   │
                   ▼
           Document Service
        ┌──────────┼───────────┐
        │          │           │
        ▼          ▼           ▼
 StorageService Repository  OCR Pipeline
        │          │           │
        ▼          ▼           ▼
   File System PostgreSQL PaddleOCR
                               │
                               ▼
                       Extracted Text
```

---

# Request Flow

```
Client
   │
POST /docs/upload
   │
   ▼
Router
   │
   ▼
DocumentService
   │
   ├────────► StorageService
   │              │
   │              ▼
   │         Save uploaded file
   │
   ├────────► OCR Pipeline
   │              │
   │              ▼
   │     PDF → Images → PaddleOCR
   │              │
   │              ▼
   │      Extract & Normalize Text
   │
   └────────► Repository
                  │
                  ▼
         Store metadata + OCR text
                  │
                  ▼
          Return API Response
```

---

# Design Principles

* Clean Architecture
* SOLID Principles
* Repository Pattern
* Thin Routers
* Business Logic inside Services
* Separation of Concerns
* Dependency Injection
* Modular & Maintainable Design

---

# Getting Started

### Clone

```bash
git clone https://github.com/Petit-DJ/ocr-v2.git
cd ocr-v2
```

### Install dependencies

```bash
uv sync
```

### Configure

Create a `.env`

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/ocr_v2

UPLOAD_DIR=app/uploads
```

### Run

```bash
uv run uvicorn app.main:app --reload
```

---

# API Documentation

```
http://127.0.0.1:8000/docs
```

---

# Example Response

```json
{
  "id": "886c66fc-90e4-4347-98fb-d91268ea3686",
  "original_filename": "Test.pdf",
  "status": "UPLOADED",
  "file_size": 8509198,
  "extracted_text": "Dummy Text 123"
}
```


# Current Status

* Document upload
* File storage
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic migrations
* Repository layer
* Service layer
* PaddleOCR integration
* PDF → Image conversion
* OCR text extraction
* Persist OCR results
* API response models
