# FastAPI Project Template

A ready-to-use **FastAPI backend development template** designed to help you start new projects without spending time configuring the development infrastructure from scratch.

The idea is simple:

> **Clone it, configure your environment variables, and start coding.**

This repository is not intended to be a specific application. It provides a reusable foundation where the common infrastructure and development environment are already configured, allowing you to focus on your application's business logic and code.

---

## 🚀 What is this?

Starting a new backend project usually requires setting up the same infrastructure repeatedly:

* Docker
* Docker Compose
* PostgreSQL
* Nginx
* pgAdmin
* Environment variables
* Python dependencies
* Networking between services
* FastAPI configuration
* Development tools

This template provides that initial setup so you don't have to repeat it for every new project.

Instead of starting from an empty directory, you can use this repository as a **starting point for your next FastAPI project**.

---

## 🎯 Main Goal

The main goal of this template is to separate **infrastructure setup** from **application development**.

The infrastructure is already configured.

You focus on:

* Business logic
* API endpoints
* Database models
* Services
* Authentication
* Integrations
* Tests
* Application-specific features

In other words:

> **Less time configuring infrastructure. More time building your application.**

---

## 🏗️ Included Stack

This template provides a development environment based on:

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| **FastAPI**        | Backend API framework         |
| **Python**         | Programming language          |
| **PostgreSQL**     | Relational database           |
| **Docker**         | Containerization              |
| **Docker Compose** | Service orchestration         |
| **Nginx**          | Reverse proxy                 |
| **pgAdmin**        | PostgreSQL administration     |
| **Swagger UI**     | Interactive API documentation |
| **ReDoc**          | API documentation             |

---

## 🐳 Architecture

The initial environment is organized around the following services:

```text
                    ┌─────────────────┐
                    │     Client      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      Nginx      │
                    │  Reverse Proxy  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │   Application   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │     Database    │
                    └─────────────────┘

                    ┌─────────────────┐
                    │     pgAdmin     │
                    │   DB Manager    │
                    └─────────────────┘
```

All services are managed through **Docker Compose**.

---

## 📁 Project Structure

The template provides an initial structure that can be adapted to the needs of each project.

```text
.
├── app/
├── nginx/
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

The structure is intentionally flexible so that each project can evolve according to its own architecture.

---

## ⚙️ Requirements

Before using the template, make sure you have:

* [Docker](https://www.docker.com/)
* Docker Compose
* Git

Python can also be installed locally when required, but the main development environment is designed to run through Docker.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harold2tg/MDT-para-fastapi.git my-new-project
```

Enter the project directory:

```bash
cd my-new-project
```

### 2. Configure environment variables

Create your `.env` file based on the environment configuration required by the project.

Example:

```bash
cp .env.example .env
```

Update the values according to your environment.

### 3. Build the containers

```bash
docker compose build
```

### 4. Start the environment

```bash
docker compose up -d
```

Your development environment is now ready.

You can start building your application immediately.

---

## 🌐 Services

Depending on your local configuration, the main services are available through:

| Service    | URL                           |
| ---------- | ----------------------------- |
| FastAPI    | `http://localhost:8000`       |
| Swagger UI | `http://localhost:8000/docs`  |
| ReDoc      | `http://localhost:8000/redoc` |
| Nginx      | `http://localhost`            |
| pgAdmin    | `http://localhost:16543`      |

> Ports can be changed through the Docker Compose configuration.

---

## 🛠️ Development

Once the environment is running, you can focus on developing your application.

You can add:

* API endpoints
* Database models
* Services
* Repositories
* Authentication and authorization
* External integrations
* Background tasks
* Automated tests
* Additional modules
* New services
* Application-specific infrastructure

The template does not impose a specific business domain.

It provides the **technical foundation** on which your application can be built.

---

## 📈 Designed to Grow

The template is designed to work as a starting point for both small and growing projects.

You can start with a single FastAPI application and progressively evolve the architecture as your project grows.

For example:

```text
Initial Project

FastAPI
   │
   └── PostgreSQL
```

And later evolve into:

```text
                     ┌───────────────┐
                     │    Nginx      │
                     └───────┬───────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
           API Service   Auth Service   Other Services
                │            │
                └──────┬─────┘
                       │
                       ▼
                  PostgreSQL
```

The template provides a starting point, not a rigid architecture.

---

## 🔧 Useful Commands

### Start the environment

```bash
docker compose up -d
```

### Stop the environment

```bash
docker compose down
```

### Rebuild containers

```bash
docker compose build
```

### Rebuild and start

```bash
docker compose up -d --build
```

### Check running containers

```bash
docker compose ps
```

### View logs

```bash
docker compose logs -f
```

### View logs for a specific service

```bash
docker compose logs -f api
```

---

## 🧠 Philosophy

This project follows a simple philosophy:

```text
Prepared Infrastructure
        ↓
     Clone
        ↓
Configure Environment
        ↓
   Start Services
        ↓
    Start Coding
```

The goal is to eliminate repetitive infrastructure configuration when starting a new project.

You should not need to spend hours configuring Docker, PostgreSQL, Nginx and the development environment before writing your first line of application code.

---

## 🎯 Use Cases

This template can be used as a starting point for:

* REST APIs
* Backend applications
* SaaS platforms
* Internal systems
* Microservices
* Enterprise applications
* MVPs and prototypes
* Personal projects
* Production-oriented applications

---

## 🔄 Reusing the Template

The recommended workflow is:

1. Clone the repository.
2. Rename the project.
3. Configure environment variables.
4. Customize the application structure.
5. Add your business logic.
6. Add project-specific dependencies.
7. Remove components you don't need.
8. Add additional infrastructure as the project grows.

The template is meant to be **adapted**, not followed rigidly.

---

## 🔐 Environment Configuration

Configuration should be handled through environment variables rather than hard-coded values.

Sensitive information such as:

* Database passwords
* Secret keys
* API credentials
* Authentication configuration
* Environment-specific settings

should be stored outside the source code.

Never commit sensitive credentials to the repository.

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

These tools allow you to test and explore your API during development.

---

## 🚧 Project Status

This project is continuously evolving.

The included infrastructure, configuration and development practices may change as new improvements, automation and best practices are introduced.

The goal is to progressively turn this repository into a reliable **starting point for new FastAPI projects**.

---

## 🤝 Contributing

Suggestions, improvements and contributions are welcome.

If you find a problem or have an idea that could improve the template, feel free to open an issue or submit a pull request.

---

## 📄 License

Add your preferred license here.

---

## ⭐ Why this project exists

Every new project should not require rebuilding the same development environment from scratch.

This template exists to provide a **reusable, ready-to-start FastAPI development environment** so developers can spend less time configuring infrastructure and more time building software.

> **Clone. Configure. Code. Build.**
