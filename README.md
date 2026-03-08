# 💳 Payments Tracker

A web application to track purchases made in installments: credit cards, bank loans, shared expenses with friends, and more.

## What is this?

In Argentina (and many other places), it's very common to pay for things in multiple installments — 3, 6, 9, 12 or more. Keeping track of what you owe, when each payment is due and how much you'll be spending next month can get complicated fast.

**Payments Tracker** solves this by letting you register any purchase and automatically breaking it down into its installments, so you always know:

- What you're paying **this month**
- What's coming up in **future months**
- How much of a shared expense **each person owes**

## Key Features

- **Purchases tracking** — Register purchases with a description, total amount, number of installments, and start date.
- **Automatic installment generation** — When you create a purchase, the app automatically generates each installment with its due date and amount.
- **Shared expenses** — Split purchases among multiple people (friends, family, etc.). Each installment generates individual shares so everyone knows exactly what they owe.
- **Multiple payment methods** — Associate purchases with different payment methods (credit cards, bank loans, cash, etc.).
- **Monthly expense overview** — See your current and upcoming monthly expenses across all active installment plans.

## Use Cases

- Buying a phone in 12 installments with your credit card
- Splitting a trip or a big purchase with friends
- Tracking a bank loan with fixed monthly payments
- Tracking how much an acquaintance ows you if you made the purchase for them
- Keeping record of informal debts between people

## Tech Stack

- **Frontend:** 
- **Backend:** Python, SQLAlchemy, FastAPI, Pydantic
- **Database:** PostgreSQL
- **Deployment:** Docker

## Project Structure

```
backend/
├── models/          # Database models (User, Purchase, Installment, Person, etc.)
├── schemas/         # Pydantic schemas for request/response validation
├── repositories/    # Data access layer
├── services/        # Business logic
└── routers/         # API endpoints
```

## API Overview

| Resource | Description |
|---|---|
| `/user` | User registration and lookup |
| `/person` | People associated with shared expenses |
| `/payment_method` | Payment methods per user |
| `/purchase` | Create and retrieve purchases (auto-generates installments) |

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your database** by setting up `backend/database/config.py` with your PostgreSQL credentials.

3. **Run the app**
   ```bash
   fastapi dev backend/main.py
   ```

4. **Explore the API** at `http://localhost:8000/docs`

## Resources to learn from
- [FastAPI docs](https://fastapi.tiangolo.com/)
- [restfulapi.net](https://restfulapi.net/)
- [repo for best practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)


