"""Database course topics and quizzes seed data."""

DATABASE_TOPICS = [
    ("SQL basics", "sql-basics", "Relational database concepts, DDL/DML, JOINs, and aggregates", """# Relational Databases & SQL Basics

Structured Query Language (SQL) is the standard language for managing relational databases (RDBMS).

## Core SQL Queries

```sql
-- Create table (DDL)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data (DML)
INSERT INTO users (username, email)
VALUES ('selvam', 'selvam@example.com');

-- Query data with JOIN and Filter
SELECT u.username, p.title
FROM users u
INNER JOIN posts p ON u.id = p.user_id
WHERE u.created_at >= '2026-01-01'
ORDER BY p.title ASC;
```

## JOIN Types

- `INNER JOIN`: Returns records that have matching values in both tables.
- `LEFT JOIN`: Returns all records from left table, and matched records from right.
- `RIGHT JOIN`: Returns all records from right table, and matched records from left.
- `FULL OUTER JOIN`: Returns all records when there is a match in either table.
"""),

    ("PostgreSQL", "postgresql", "Advanced JSONB, GIN indexing, ACID guarantees, and schemas", """# PostgreSQL Fundamentals

PostgreSQL is an advanced, enterprise-grade open-source relational database.

## Key Features

- **JSONB Data Type**: Store and index semi-structured JSON documents natively with high query performance using GIN indexes.
- **Full ACID Compliance**: Strict transactional guarantees for financial and mission-critical applications.
- **Custom Types & Schemas**: Support for Enum types, custom domain constraints, and schema partitioning.

```sql
-- Querying JSONB in PostgreSQL
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  attributes JSONB
);

-- Search inside JSONB field
SELECT name FROM products
WHERE attributes->>'color' = 'blue';
```
"""),

    ("MySQL", "mysql", "Storage engines (InnoDB vs MyISAM), auto-increment, and foreign key constraints", """# MySQL Fundamentals

MySQL is one of the world's most popular open-source relational database systems.

## Storage Engines

- **InnoDB**: Default engine. Supports ACID transactions, foreign key constraints, and row-level locking.
- **MyISAM**: Older engine. Fast for read-heavy workloads, but lacks transaction support and foreign keys.

```sql
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;
```
"""),

    ("MongoDB", "mongodb", "NoSQL document model, BSON, Collections, and Aggregation Pipeline", """# MongoDB & NoSQL Databases

MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like BSON documents.

## Document Structure

```json
{
  "_id": "60d5ecb8b5c9f22340e4f1a2",
  "title": "MongoDB Basics",
  "tags": ["database", "nosql"],
  "comments": [
    { "user": "Alice", "text": "Great guide!" }
  ]
}
```

## Aggregation Pipeline Example

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customerId", totalSpent: { $sum: "$amount" } } },
  { $sort: { totalSpent: -1 } }
]);
```
"""),

    ("ORM (Prisma or Sequelize)", "orm", "Object-Relational Mapping benefits, migrations, and SQL injection defense", """# Object-Relational Mapping (ORM)

An ORM translates between database tables and object-oriented code in your programming language.

## Benefits of Using an ORM

1. **Abstraction**: Write database queries using JavaScript/Python methods instead of raw SQL strings.
2. **Security**: Automatically parameterizes inputs, rendering applications immune to **SQL Injection** attacks.
3. **Migrations**: Track database schema changes in code files versioned with Git.

## Example with Prisma ORM

```prisma
// schema.prisma
model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  posts     Post[]
}
```

```javascript
// Querying with Prisma Client
const user = await prisma.user.findUnique({
  where: { email: 'alice@example.com' },
  include: { posts: true }
});
```
""")
]

DATABASE_QUIZZES = {
    "database-sql-basics": [
        {
            "level": "medium",
            "title": "SQL Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which JOIN type returns all records from the left table and matched records from the right table?",
                    "explanation": "LEFT JOIN returns all rows from the left table regardless of whether there is a match in the right table.",
                    "options": [("INNER JOIN", False), ("LEFT JOIN", True), ("RIGHT JOIN", False), ("FULL JOIN", False)],
                },
            ],
        }
    ],
    "sql-sql-basics": [
        {
            "level": "medium",
            "title": "SQL Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which JOIN type returns all records from the left table and matched records from the right table?",
                    "explanation": "LEFT JOIN returns all rows from the left table regardless of whether there is a match in the right table.",
                    "options": [("INNER JOIN", False), ("LEFT JOIN", True), ("RIGHT JOIN", False), ("FULL JOIN", False)],
                },
            ],
        }
    ],
    "database-postgresql": [
        {
            "level": "medium",
            "title": "PostgreSQL Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which data type in PostgreSQL allows storing and indexing binary JSON efficiently?",
                    "explanation": "JSONB stores JSON in a decomposed binary format supporting fast query indexing.",
                    "options": [("VARCHAR", False), ("JSONB", True), ("BLOB", False), ("TEXT", False)],
                },
            ],
        }
    ],
    "database-mysql": [
        {
            "level": "medium",
            "title": "MySQL Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which storage engine in MySQL provides full transaction support and foreign key constraints?",
                    "explanation": "InnoDB is the default MySQL engine supporting transactions and foreign key constraints.",
                    "options": [("MyISAM", False), ("InnoDB", True), ("MEMORY", False), ("CSV", False)],
                },
            ],
        }
    ],
    "database-mongodb": [
        {
            "level": "medium",
            "title": "MongoDB Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What format does MongoDB use internally to store documents?",
                    "explanation": "MongoDB stores data in BSON (Binary JSON) format.",
                    "options": [("XML", False), ("BSON", True), ("YAML", False), ("CSV", False)],
                },
            ],
        }
    ],
    "database-orm": [
        {
            "level": "medium",
            "title": "ORM Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What critical security vulnerability do ORMs protect against by default?",
                    "explanation": "ORMs automatically parameterize query inputs, protecting against SQL Injection attacks.",
                    "options": [("Cross-Site Scripting (XSS)", False), ("SQL Injection", True), ("CSRF", False), ("DDoS", False)],
                },
            ],
        }
    ],
}
