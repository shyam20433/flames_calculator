# FLAMES Relationship Calculator

A beautiful web application that calculates the relationship compatibility between two people using the FLAMES algorithm. Built with Flask and featuring a love-themed UI.

## What is FLAMES?

FLAMES is a popular relationship compatibility game that stands for:
- **F** - Friends
- **L** - Love  
- **A** - Affection
- **M** - Marriage
- **E** - Enemy
- **S** - Sibling

## Features

- ✨ Beautiful love-themed UI with animated hearts
- 🌸 Pink gradient design with romantic styling
- 📱 Responsive design that works on all devices
- ⚡ Fast and accurate FLAMES calculation
- 🎯 Simple and intuitive user interface

## Installation

1. Clone or download this repository
2. Make sure you have Python installed (Python 3.6 or higher)
3. Install Flask:
   ```bash
   pip install flask
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Enter two names and click "Calculate" to see the relationship result!

## How FLAMES Works

1. **Remove Common Letters**: Take both names and remove all common letters
2. **Count Remaining Letters**: Count the total remaining letters
3. **FLAMES Elimination**: Starting from F, count the remaining letters and eliminate letters from FLAMES
4. **Final Result**: The last remaining letter determines the relationship type

### Example:
- Name 1: "JOHN"
- Name 2: "JANE"
- Common letters: J, A, N
- Remaining: O, H, E
- Count: 3
- FLAMES elimination: F, L, A, M, E, S → F, L, M, E, S → F, L, M, S → F, L, S → F, S → F
- Result: **Friends**

## Project Structure

```
flames/
├── app.py              # Flask application entry point
├── flames.py           # FLAMES algorithm logic
├── templates/
│   └── index.html      # Web interface template
└── README.md           # This file
```

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Algorithm**: FLAMES relationship calculator

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Fixing bugs
- Adding more relationship algorithms

## License

This project is open source and available under the MIT License.

---

Made with ❤️ for love and relationships! 