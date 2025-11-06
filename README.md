# 🧪 Potion Crafter

A gamified full-stack project where you act as an alchemist and craft magical potions using **real-world data**.

You mix:
- 🌦️ Weather (OpenWeather API)
- 🐈 Cat wisdom (CatFacts API)
- 🔢 Number magic (Numbers API)

and the system generates:
- 🧙 Potion Name
- ⭐ Rarity (Common → Mythic)
- 🪄 Magical Effects
- 🪙 Gold + XP rewards
- 📜 Potion history & discoveries

---

## 🎮 Gameplay Concept

1. Enter a **city** and a **number**
2. Backend fetches real data
3. Data turns into mystical “essences”
4. Essences combine into a **potion**
5. Earn XP, Gold, and unlock rare combos

_Think fantasy alchemy + API engineering + little RPG vibes._

---

## 🧠 Tech Stack

**Frontend:**  
- HTML, CSS, JavaScript (no framework — clean & simple)

**Backend:**  
- Python, FastAPI, httpx
- SQLAlchemy or Beanie (Mongo) for persistence

**APIs Used:**
- 🌤️ OpenWeatherMap API
- 🐱 CatFacts API
- 🔢 NumbersAPI

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/Potion-Crafter.git
cd Potion-Crafter
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy httpx python-dotenv
```

### 4️⃣ Set up environment variables
Create a .env file in the backend directory:
```ini
OWM_API_KEY=your_openweathermap_api_key
```

### 5️⃣ Run the development server
```bash
uvicorn backend.app:app --reload
```
Then visit http://localhost:8000

### 💫 Example Potion Craft
Input:
```makefile
City: London
Number: 73
```

### APIs return:
```
Weather → “Light rain, 11°C”
Cat Fact → “Cats were considered sacred in ancient Egypt.”
Number → “73 is the 21st prime number.”
```
### Generated Potion:
```vbnet
Name: Prime Sphinx Elixir of Tempest
Rarity: RARE
Effects: ["Luck +2", "Focus +1"]
Gold Awarded: 20
XP Gained: 15
```

## 🧩 Gamification System
```yaml
Rarity	XP	Gold	Example Name
Common	+5	+5	“Whisker Draught of Mist”
Uncommon	+8	+10	“Purr Tonic of Zephyr”
Rare	+15	+20	“Prime Sphinx Elixir of Tempest”
Epic	+25	+35	“Triska Arc Infusion of Solaris”
Mythic	+40	+60	“Eternal Sphinx Elixir of Thunder”

💡 **First-time discoveries earn a 50% gold bonus!**
---

