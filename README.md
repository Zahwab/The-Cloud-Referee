# ⚡ The Tech Referee

![The Tech Referee](assets/tech_referee_banner.png)

**The Tech Referee** is an interactive decision support tool designed to help developers and architects choose the right technology stack for their projects. By comparing popular technologies side-by-side, it provides objective "referee" verdicts based on specific use cases, trade-offs, and developer experience scores.

## 📚 Documentation

*   [**User Guide**](USER_GUIDE.md) - Complete guide on how to usage the tool.
*   [**Architecture**](ARCHITECTURE.md) - Technical deep-dive with system diagrams.
*   [**Contributing**](CONTRIBUTING.md) - Guide for adding new technology matchups.

## 🚀 Features

- **Interactive Matchups**: Select from various categories such as Cloud Compute, Databases, and Frontend Frameworks.
- **Head-to-Head Comparisons**: Detailed comparisons on critical criteria like Cost, Scalability, Learning Curve, and Best Use Case.
- **The Final Verdict**: Automated, scenario-based recommendations helping you decide when to use which technology.
- **Developer Experience Scorecard**: Quantified scoring of each technology's ease of use and ecosystem support.

## 🥊 Battle Categories

Currently supported comparisons include:

### ☁️ Cloud Compute
- **AWS Lambda vs EC2**: Serverless vs. Traditional VMs.
- **AWS Fargate vs EKS**: Serverless Containers vs. Kubernetes Orchestration.

### 🗄️ Databases
- **DynamoDB vs RDS**: NoSQL vs. Relational (SQL).
- **MongoDB vs PostgreSQL**: Document Store vs. Advanced Object-Relational.

### ⚛️ Frontend Frameworks
- **React vs Vue**: The ecosystem giant vs. the progressive framework.
- **Angular vs Svelte**: The complete enterprise platform vs. the compiler-based lightweight.

## 🛠️ Installation

Ensure you have Python installed on your system.

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Install the required dependencies**:
    ```bash
    pip install streamlit pandas
    ```

## 🏃 Usage

Run the application using the Streamlit CLI:

```bash
streamlit run app.py
```

The application will open in your default web browser. Use the **sidebar** to configure the "Match"—select a **Category** and a **Matchup** to see the fighters enter the ring!

## 📂 Project Structure

- `app.py`: The main application file containing the Streamlit UI logic and comparison data.
- `README.md`: Project documentation.

