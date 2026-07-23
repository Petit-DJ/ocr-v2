# OCR Backend

A production-oriented OCR backend built with **FastAPI** following clean architecture principles. The project focuses on building a scalable and maintainable document processing pipeline with clear separation of concerns.

## Overview

The backend accepts document uploads, stores document metadata, processes files through an OCR pipeline, and returns the extracted text as an API response.

The goal is to build the system incrementally while following production backend practices such as service layers, repositories, dependency separation, and modular architecture.

---

## Current Features

- Upload PDF documents
- Store uploaded files
- SQLAlchemy database integration
- Document metadata model
- Layered architecture (Router → Service → Storage)
- Modular project structure

---

## Planned Features

- PaddleOCR integration
- OCR text extraction
- Document repository layer
- Request validation
- Structured API responses
- Logging
- Exception handling
- Configuration management
- Unit & Integration testing
- Authentication
- PostgreSQL support
- Docker deployment

---

## Tech Stack

- Python 3.13+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- UV (Package Manager)

---

## Project Structure

```
app/
│
├── db/
│   ├── base.py
│   └── database.py
│
├── document/
│   ├── model.py
│   ├── repository.py
│   ├── router.py
│   └── service.py
│
├── storage/
│   └── service.py
│
├── core/
│
└── main.py
```

---

## Architecture

```
Client
   │
   ▼
FastAPI Route
   │
   ▼
Document Service
   │
   ├──────────────► Storage Service
   │                     │
   │                     ▼
   │                  File System
   │
   ├──────────────► Repository (Upcoming)
   │                     │
   │                     ▼
   │                  Database
   │
   └──────────────► OCR Service (Upcoming)
                         │
                         ▼
                  Extracted Text
```

---

## Request Flow

```
Client
   │
POST /upload
   │
   ▼
Route
   │
   ▼
DocumentService
   │
   ▼
StorageService
   │
   ▼
Save File
   │
   ▼
Repository (Upcoming)
   │
   ▼
Store Metadata
   │
   ▼
OCR Service (Upcoming)
   │
   ▼
Return OCR Response
```

---

## Design Principles

- Separation of Concerns
- SOLID Principles
- Thin Routes
- Business Logic inside Services
- Repository Pattern
- Modular and Maintainable Architecture
- Production-oriented Project Structure

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Petit-DJ/ocr-v2.git
cd ocr-v2
```

### Install dependencies

```bash
uv sync
```

### Run the application

```bash
uv run uvicorn app.main:app --reload
```

### API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Project Status

🚧 Under Development

Current milestone:
- ✅ File upload architecture
- ✅ Storage layer
- ✅ Database setup
- 🚧 Repository layer
- 🚧 OCR integration
- ⏳ Production enhancements

---

## Learning Goals

This project is being developed with a focus on learning production backend engineering concepts, including:

- Backend architecture
- Data flow design
- Service layer pattern
- Repository pattern
- SQLAlchemy ORM
- API design
- Clean code practices
- Scalable project structure
