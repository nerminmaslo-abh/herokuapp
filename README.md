# Restful Booker API Testing

This project contains automated API tests for [Restful Booker](https://restful-booker.herokuapp.com/apidoc/) using **Python**, **PyTest**, and **Requests**.  
It includes token-based authentication, request utilities, dynamic payload support with `**kwargs`, and clean modular structure.

---

##  System Requirements

- Python 3.9+
- macOS or Linux terminal (tested on macOS)
- `git` installed

---

##  Project Structure

```
herokuappTests/
├── base/
│   └── Base.py
├── auth/
│   └── authenticator.py
├── utils/
│   ├── booking_api_utils.py
│   └── request_utils.py
├── tests/
│   └── test_booking.py
├── requirements.txt
└── README.md
```

Each folder contains `__init__.py` to support package imports.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2. Create & Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_booking.py -v
```

---

## ✅ Notes

- Token is handled via `authenticator.py` and injected into headers.
- All requests go through a shared `RequestUtils` class.
- Booking-related logic lives in `BookingApiUtils`.
- Test classes should **not define `__init__()`**. Use `setup_method(self)` in `Base.py` instead.

---

