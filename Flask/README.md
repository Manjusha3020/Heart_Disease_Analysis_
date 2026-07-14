# PulseView — Heart Disease Analysis (Flask site)

A Flask front end that embeds a Tableau dashboard and a 4-scene story
(exported as PNGs) for a heart disease dataset.

## Pages

- `/` — Home / hero
- `/about` — Project overview + the three user scenarios
- `/dashboard` — Full Tableau dashboard embed
- `/story` — Interactive 4-scene story navigator (tabs + prev/next)
- `/contact` — Contact form (flash-messages on submit, no email backend wired up)

## Run it locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Swapping in your own exports

Drop new PNGs into `static/images/` and update the `STORY_SCENES` /
`DASHBOARD_PANELS` lists at the top of `app.py` — the templates render
everything from those two lists, so no HTML edits are needed for new
scenes or panel copy.

## Project structure

```
heart_disease_flask/
├── app.py
├── requirements.txt
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/            # dashboard.png + 4 story scene PNGs
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── dashboard.html
    ├── story.html
    └── contact.html
```
