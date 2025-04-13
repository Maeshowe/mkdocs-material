import os
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = (
    "Kérlek, foglald össze a globális piaci helyzetet az elmúlt egy hét hírei alapján. "
    "Mely szektorok vagy eszközosztályok mutatnak erőt, és melyek gyengélkednek? "
    "Milyen főbb események mozgatják most a piacot?"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

content = response.choices[0].message.content
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

# Abszolút elérési út használata:
base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.abspath(os.path.join(base_dir, "../docs/reports/market_overview"))
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, f"{timestamp}.md")

print(f"Mentés ide: {output_path}")

with open(output_path, "w") as f:
    f.write(f"# Piaci helyzetkép ({timestamp})\n\n{content}\n")