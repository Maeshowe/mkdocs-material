import os
import openai
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

portfolio_df = pd.read_csv("portfolio.csv")
portfolio_str = portfolio_df.to_string(index=False)

prompt = (
    f"Ez a portfólióm:\n{portfolio_str}\n\n"
    "Van bármi olyan közelgő esemény vagy rizikó a láthatáron, ami jelentősen befolyásolhatja a portfóliómat? "
    "(Pl. fontos makroadat, jegybanki döntés, politikai esemény, cég-specifikus hír.) "
    "Kérlek sorold fel a legfontosabbakat és írd le, hogyan érinthetik a befektetéseimet."
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

content = response.choices[0].message.content
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

output_path = f"../web/reports/portfolio_alerts/{timestamp}.md"
with open(output_path, "w") as f:
    f.write(f"# Portfólió riasztások és kockázatok ({timestamp})\n\n{content}\n")