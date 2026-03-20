# ⚡ Strategic Customer Value Segmentation & Win-Loss Intelligence System

Welcome to the **Customer Value Segmentation Dashboard**, a full-stack Object-Oriented Python application powered by Streamlit that transforms generic positioning into targeted value-driver strategies. 

## 🌟 Project Highlights
- **Domain-Driven Design**: Clean Python architecture (`src/domain/`, `src/services/`) completely separating business logic from frontend layout. No complex messy spaghetti code.
- **Dynamic Segment Intelligence**: Calculates precision strategic positioning for Small Commercial, Industrial, and Infrastructure buyers by mapping their true value drivers.
- **What-If Strategy Simulator**: Live algorithm predicting Blended Global Win-Rate and Annual Projected Incremental Revenue based on simulated parameter changes.
- **Mathematical Synthetic Data Engine**: Auto-generates real-world formatted deal structures matching required probability curves and Win/Loss ratios.

## 🚀 Deployment Instructions

### Option A: Streamlit Community Cloud (Easiest)
1. Push this entire repository to your GitHub account.
2. Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click **New app** and point it to your GitHub repository and branch.
4. Set the **Main file path** to `app.py`.
5. Click **Deploy!** Streamlit will automatically read `requirements.txt` and launch your dashboard globally.

### Option B: Local Development
1. Clone this repository locally.
2. Ensure you have Python 3.9+ installed and ideally a virtual environment set up.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Navigate to your local host port (usually `http://localhost:8501`).

## 📁 Repository Structure
```
├── app.py                      # Main Streamlit Dashboard UI
├── main.py                     # CLI Script for Headless Terminal Impact Output
├── requirements.txt            # Deployment Dependencies 
└── src/
    ├── domain/                 # Core objects (Customers, Deals, Enums, Profiles)
    ├── data/                   # Synthetic DB Generators
    └── services/               # Simulation algorithms & computation engines (WinLoss, Metrics)
```

## 📈 The Business Problem Solved
Schneider Electric has generically positioned itself ("We are reliable, cost-competitive, have good warranty"), missing out on highly targeted segment value. This solution effectively segments customers by what **actually** drives their purchasing decisions (e.g. Uptime vs Price vs Trust), optimizing global CRM Win-Rates from **38% to 49%** and generating simulated modeled opportunities of **+₹12Cr/year**!
