# E-Commerce Backend API

A robust Django REST Framework backend for e-commerce with JWT authentication, product/category management, filtering, pagination, and Swagger documentation. Built with PostgreSQL and optimized for performance.

## 🚀 Features

- **JWT Authentication** – Secure token-based authentication for users.
- **Product Management** – Full CRUD operations with filtering and sorting.
- **Category System** – Organize products by categories.
- **Filtering & Sorting** – Filter products by category, price range, stock, or active status.
- **Pagination** – Efficient handling of large datasets.
- **Swagger Documentation** – Interactive API documentation for frontend integration.
- **Database Optimization** – Indexed fields for high-performance queries.
- **Dockerized Deployment** – Easy setup with Docker and Docker Compose.

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.8, Django REST Framework
- **Database**: PostgreSQL 15
- **Authentication**: JWT (Simple JWT)
- **Documentation**: Swagger / ReDoc (drf-yasg)
- **Containerization**: Docker & Docker Compose
- **Utilities**: django-filter, django-cors-headers, python-decouple

---

## 📦 Installation

### Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/M-Wonder/E-Commerce-Backend.git
cd E-Commerce-Backend

# Copy environment variables
cp .env.example .env

# Build and start containers
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

📚 API Documentation

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

#Register a new user
POST /api/users/register/
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123",
  "password2": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}

#Login (Get JWT Token)
POST /api/token/
{
  "username": "johndoe",
  "password": "securepass123"
}

