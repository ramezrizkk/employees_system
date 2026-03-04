# 👨‍💼 Python Employee Management System

A clean, console-based employee management application built with Python, demonstrating object-oriented design principles, input validation, and clean architecture with separation of concerns.

## ✨ Features

- **Add Employees** — Create new employee records with name, age, and salary
- **List All Employees** — Display formatted employee directory with all details
- **Delete by Age Range** — Bulk remove employees within specified age brackets
- **Update Salary** — Modify employee compensation by name lookup
- **Robust Input Validation** — Comprehensive error handling for all user inputs

## 🏗️ Architecture

### Project Structure
FrontendManager    → Handles UI, menu display, and user interaction flow
EmployeesManager   → Business logic: CRUD operations and data processing
Employee           → Data model representing individual employee entities

### Technical Implementation
| Component | Purpose |
|-----------|---------|
| `input_valid_int()` | Universal input validator with range checking |
| `Employee` class | Encapsulates employee data with string representations |
| `EmployeesManager` | Core application logic and data manipulation |
| `FrontendManager` | Presentation layer and program loop control |

## 🔄 Core Workflows

### Adding Employees
1. Collect name (string), age (validated integer), and salary (validated integer)
2. Instantiate new `Employee` object
3. Append to employees list

### Deleting by Age Range
- Smart range handling: automatically swaps if `from > to`
- Reverse iteration prevents index shifting issues during deletion
- Real-time console feedback for each deleted employee

### Salary Updates
- Name-based employee lookup
- Direct salary modification on found object
- Error messaging for non-existent employees

## 🛡️ Validation Features

- **Type Safety** — `isdecimal()` check ensures only numeric inputs for integers
- **Range Enforcement** — Menu choices strictly bounded (1-5)
- **Age/Salary Validation** — Prevents negative or invalid numeric entries
- **Graceful Error Handling** — Invalid inputs trigger retry prompts without crashing
- **Smart Range Swapping** — Age range inputs automatically correct if reversed

## 📊 Code Highlights

- **Clean OOP Design** — Three-class separation: Model, Manager, Frontend
- **Dunder Methods** — `__str__` and `__repr__` for readable object representation
- **Reverse Deletion** — Index-safe removal using backward iteration
- **Modular Validation** — Reusable `input_valid_int()` function across all inputs
- **Menu Scaling** — Dynamic option counting for easy feature extension

## 🔮 Potential Enhancements

- Persistent storage (JSON/CSV file handling)
- Employee ID system for unique identification
- Search and filter capabilities
- Salary statistics and reporting
- Department/role categorization
- Data export functionality

Built with Python 🐍 | Clean code meets practical functionality
