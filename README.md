# Black-Scholes Option Pricing Tool

This project is a web-based tool that allows users to generate heatmaps for European call and put options using the Black-Scholes model. The tool is built using Flask and is hosted on Heroku.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive Sliders:** Users can adjust the strike price, risk-free rate, and volatility using sliders to see how these parameters affect the option prices.
- **Real-time Heatmaps:** Generates heatmaps for both call and put options using the Black-Scholes model.
- **Responsive Design:** The user interface is designed to be responsive and user-friendly.

## Installation

### Prerequisites

- Python
- Flask
- Matplotlib
- Gunicorn (for production deployment)

### Clone the Repository

```bash
git clone https://github.com/emilwestling/Black-Scholes.git
cd Black-Scholes
```

### Set up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
flask run
```

The application will start on http://127.0.0.1:5000/. You can access it from your web browser.

## Usage

- Visit the web application at https://black-scholes-heatmap-7785d38551b8.herokuapp.com.
- Use the sliders to adjust the Strike Price (K), Risk-free Rate (r), and Volatility (σ).
- Click "Generate Heatmaps" to see the updated heatmaps for the European call and put options.

## Contributing

Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License

This project is licensed under the MIT License.
