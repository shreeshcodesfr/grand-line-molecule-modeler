# Grand Line Molecular Modeler

An educational molecule explorer with a pirate-adventure anime-inspired Grand Line theme. The intro explains molecular structures; click the glowing molecule or launch button to open the interactive lab.

## Features
- Animated molecule viewer; drag to rotate, scroll or use buttons to zoom
- Water, carbon dioxide, methane, ammonia and oxygen models
- Atom inspector, bond guide, geometry, bond angle, polarity and everyday uses
- Pause/play and rotation speed control
- Responsive dark-ocean and treasure-gold interface

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deploy on Render
Create a Web Service from this repository.
Build: `pip install -r requirements.txt`
Start: `gunicorn app:app`
No API key required. Models are simplified educational illustrations, not quantum-chemical simulations; sizes and bond lengths are not to scale.
