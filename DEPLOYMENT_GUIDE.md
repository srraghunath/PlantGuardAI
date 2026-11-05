# 🚀 PlantGuard AI — Deployment Guide

This guide provides step-by-step instructions to deploy the **PlantGuard AI Disease Diagnosis System** to free and production cloud platforms.

---

## 📋 Pre-Deployment Checklist
- [x] Web Application & UI enhanced (`main.py` + `disease_info.py`)
- [x] Optimized `requirements.txt` using `tensorflow-cpu` (fast builds, no CUDA bloatware)
- [x] Trained model `trained_model.keras` verified (31 MB — well within GitHub's 100MB limit)
- [x] `.gitignore` created to exclude `Plant_Disease_Dataset.zip` (1.48 GB cannot be pushed to GitHub)
- [x] `Dockerfile` and `.dockerignore` created for container deployments

---

## Option 1: Streamlit Community Cloud (Recommended — 100% Free & Easiest)

Streamlit Community Cloud is the fastest way to host Streamlit apps for free with a public URL (e.g., `https://plantguard.streamlit.app`).

### Step 1: Initialize Git and Push to GitHub
Open terminal/PowerShell in your project directory:
```bash
git init
git add .
git commit -m "Initial commit of PlantGuard AI"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/plant-disease-prediction.git
git push -u origin main
```
*(Make sure the 1.48 GB zip file is NOT included — `.gitignore` handles this automatically!)*

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **"New app"**.
3. Select your repository: `plant-disease-prediction`.
4. Branch: `main`.
5. Main file path: `Plant_Disease_Prediction/main.py`.
6. Click **"Deploy!"**.
Your app will be live and accessible to anyone worldwide within 2–3 minutes!

---

## Option 2: Hugging Face Spaces (Free Cloud Hosting)

Hugging Face Spaces provides free hosting with 16GB RAM for Machine Learning applications.

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces) and create a free account.
2. Click **"Create new Space"**.
3. Space name: `plant-disease-detection`.
4. Space SDK: Select **Streamlit**.
5. Hardware: **CPU Basic (Free)**.
6. Push your project repository using Git:
```bash
git remote add space https://huggingface.co/spaces/<YOUR_HF_USERNAME>/plant-disease-detection
git push space main
```
Your Space will build and deploy automatically!

---

## Option 3: Docker Deployment (Render, Railway, or Google Cloud Run)

### Local Docker Testing:
```bash
docker build -t plantguard-ai .
docker run -p 8501:8501 plantguard-ai
```
Then visit `http://localhost:8501`.

### Deploying to Render.com (Free Tier):
1. Create a free account on [render.com](https://render.com).
2. Click **"New +"** -> **"Web Service"**.
3. Connect your GitHub repository.
4. Environment: **Docker**.
5. Instance Type: **Free**.
6. Click **"Create Web Service"**.

---

## 💡 Troubleshooting Tips
- **Memory Limit / OOM (Out of Memory):** 
  Always use `tensorflow-cpu` instead of standard `tensorflow` in `requirements.txt`. It saves 400MB+ RAM and prevents cloud containers from running out of memory.
- **Model File Missing:**
  Ensure `trained_model.keras` (31 MB) is committed to GitHub. GitHub allows files up to 100 MB without Git LFS.

