import os
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = (
    "Egy erősen kockázattűrő befektető vagyok 3 hónapos időtávval. "
    "Sorolj fel 5 részvényt és 2 ETF-et, amiket most érdemes lehet megvenni a rövid távú növekedési lehetőség miatt, "
    "és indokold is meg röviden, miért!"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

content = response.choices[0].message.content
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

output_path = f"../web/reports/stock_etf_tips/{timestamp}.md"
with open(output_path, "w") as f:
    f.write(f"# Top részvény- és ETF-tippek ({timestamp})\n\n{content}\n")