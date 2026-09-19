# 🔐 Oasis Infobyte SIP - Task 3: Random Password Generator

A robust and secure command-line utility developed in Python. This application allows users to quickly generate highly randomized, customisable passwords tailored to modern digital security standards.

---

## 🚀 Project Overview
This project was built during my Python Programming internship at Oasis Infobyte. The application addresses the issue of weak credentials by generating safe, unpredictable combinations of strings based on direct user preferences.

### 🌟 Key Features
- **Length Constraint:** Enforces a secure minimum threshold of 8 characters to meet modern security compliance.
- **Granular Complexity Toggles:** Users can selectively include or exclude:
  - Lowercase characters (`a-z`)
  - Uppercase characters (`A-Z`)
  - Numerical digits (`0-9`)
  - Special symbols/punctuation (`!@#$...`)
- **Smart Validation Rules:** Built-in safeguards that check inputs and require a minimum of two character pools to prevent weak structures.
- **Enhanced Randomization:** Pulls mandatory character choices first to satisfy the user's rules, appends remaining characters, and shuffles the final array completely to prevent predictable pattern sequences.

---

## 🛠️ Core Tech Stack & Modules Used
- **Language:** Python 3.x
- **Standard Library Modules:** 
  - `random`: For handling distribution and shuffling of characters.
  - `string`: To safely query verified ASCII constant character pools.

---

## 💻 How It Works
1. **Length Input:** The program prompts you to define how long the password should be (Minimum 8).
2. **Character Choices:** You toggle character rules via simple `y/n` prompts.
3. **Generation & Verification:** The backend confirms your preferences, grabs compliant characters, randomly shuffles them, and outputs the highly secure combination string immediately on screen.
