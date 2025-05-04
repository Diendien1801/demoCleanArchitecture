# 🧼 Clean Architecture Demo - FastAPI

Đây là một ví dụ đơn giản về ứng dụng FastAPI áp dụng kiến trúc **Clean Architecture**, nhằm mục tiêu trình bày cách tổ chức mã nguồn rõ ràng, tách biệt các tầng nghiệp vụ, giúp dễ bảo trì, kiểm thử và mở rộng.

## 📌 Mục tiêu

Ứng dụng REST API cung cấp các chức năng:
- Lấy danh sách người dùng (`GET /users`)
- Lấy thông tin người dùng theo ID (`GET /users/{id}`)

## 🧱 Kiến trúc tổng thể

Áp dụng Clean Architecture với các tầng:



````markdown
```text
app/
├── domain/         # Entities & repository interfaces
├── use_cases/      # Business logic (application layer)
├── infrastructure/ # Implementations (e.g., in-memory repository)
├── interfaces/     # HTTP controller (FastAPI routes)
└── main.py         # Entry point
````
### 🔁 Dòng chảy xử lý
Request → Controller (interfaces) → Use Case → Repository (interface) → Implementation (infrastructure) → Response


## 🚀 Cách chạy ứng dụng

1. Cài đặt Python ≥ 3.8  
2. Tạo virtualenv:

    ```bash
    python -m venv venv
    source venv/bin/activate     # Hoặc venv\Scripts\activate.bat trên Windows
    ```

3. Cài đặt thư viện:

    ```bash
    pip install -r requirements.txt
    ```

4. Chạy server:

    ```bash
    uvicorn app.main:app --reload
    ```

5. Truy cập:
    - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
    - API endpoint: [http://localhost:8000/users](http://localhost:8000/users)



## 📚 Tham khảo

- [Clean Architecture - Uncle Bob](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
