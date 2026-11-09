# Hebrew Date Converter

A small web service and page that converts a Gregorian date to a Hebrew date,
using the [Hebcal Hebrew Date Converter API](https://www.hebcal.com/home/219/hebrew-date-converter-rest-api).

## How it works

```
Browser (index.html)  ──GET /api/convert?date=YYYY-MM-DD──▶  Flask (app.py)  ──▶  Hebcal API
```

1. The user types a date or picks it from the calendar and clicks **Convert**.
2. The page calls the backend endpoint `/api/convert`.
3. The backend validates the date, calls Hebcal (`g2h=1`, `strict=1`, 5s timeout),
   and returns a small JSON response.
4. The page shows the Hebrew date, or an error message.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## API

`GET /api/convert?date=2026-11-09`

```json
{
  "gregorian": "2026-11-09",
  "hebrew": "כ״ט בְּחֶשְׁוָן תשפ״ז",
  "hebrew_english": "29 Cheshvan 5787"
}
```

Errors:
- `400`: the date is missing or invalid
- `502`: the Hebcal service failed or timed out

## Notes

- The Hebrew day begins at sunset. This app converts the calendar date as given
  (Hebcal also supports an after-sunset flag, `gs=on`, which isn't used here).
- Hebrew date data is provided by [Hebcal.com](https://www.hebcal.com) under CC BY 4.0.
