# 🧠 AI Agent Content Generator

An AI microservice that generates:
- 📝 Blogs & Reports (PDF)
- 📊 Presentations with scraped images (PPTX)

## 🔗 Tech stack
- FastAPI + Uvicorn
- OpenAI API
- ReportLab (PDF)
- python-pptx + BeautifulSoup (PPTX)
- .env for API key

## 🚀 How to run

```bash
python -m venv venv
# Activate venv
pip install -r requirements.txt

uvicorn main:app --reload
