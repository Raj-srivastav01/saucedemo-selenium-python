# 🧪 SauceDemo Professional Automation Framework

![Tests](https://github.com/YOUR_USERNAME/saucedemo-selenium-python/actions/workflows/main.yml/badge.svg)

A production-ready Selenium Python testing framework featuring **Page Object Model (POM)** and **GitHub Actions CI/CD**.

## ✨ Features

- Page Object Model (POM) architecture
- Explicit waits for stability
- GitHub Actions CI/CD integration
- HTML test reports
- Comprehensive logging
- Multi-user persona testing

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/saucedemo-selenium-python.git
cd saucedemo-selenium-python
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all tests
python -m pytest -v

# Run with HTML report
python -m pytest -v --html=report.html --self-contained-html

# Run specific test
python -m pytest tests/test_login_scenarios.py -v
```

## 📁 Project Structure
```
saucedemo-selenium-python/
├── pages/          # Page Object Model classes
├── tests/          # Test scenarios
├── utils/          # Utilities (driver, logger)
├── config.py       # Configuration
└── requirements.txt
```

##  Test Scenarios

- **Login Scenarios**: Standard, locked, performance users
- **E2E Flow**: Complete shopping cart to checkout flow

## CI/CD

Tests run automatically on push via GitHub Actions. View results in the Actions tab.

##  Author

**Raj Srivastav**
- GitHub: [@Raj-srivastav01](https://github.com/Raj-srivastav01)