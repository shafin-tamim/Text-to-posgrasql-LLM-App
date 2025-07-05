# English to PostgreSQL Query Generator

A Streamlit-based application that converts natural language instructions into PostgreSQL queries using LangChain and Groq LLM.

## 🌟 Features

- Convert English instructions to PostgreSQL queries
- User-friendly web interface powered by Streamlit
- Uses Llama 3 70B model through Groq for accurate SQL generation
- Simple and intuitive text input area
- Instant SQL query generation

## 🚀 Use Cases

1. **Database Development**
   - Quickly generate SQL queries without memorizing syntax
   - Convert business requirements into SQL queries
   - Prototype database queries during development

2. **Learning PostgreSQL**
   - Help beginners understand SQL query structure
   - Learn PostgreSQL syntax through natural language
   - Compare your SQL knowledge with AI-generated queries

3. **Database Administration**
   - Generate complex queries for data analysis
   - Create queries for report generation
   - Quickly prototype data extraction queries

## 💡 Example Usage

You can input instructions like:
- "Get the names of all employees who joined after January 1, 2020"
- "Find the total sales for each product category in 2023"
- "List all customers who have made more than 5 purchases"
- "Show departments with average salary greater than company average"

## ⚙️ Requirements

- Python 3.8+
- Groq API key
- Required Python packages (see requirements.txt)

## 🔐 Setup

1. Clone the repository
2. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`

## ⚠️ Note

- Ensure your English instructions are clear and specific
- The generated SQL queries may need review before use in production
- The application requires an active internet connection

## 📝 License

MIT License
