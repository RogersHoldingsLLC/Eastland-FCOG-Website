from pathlib import Path

html = Path("index.html").read_text()

html = html.replace(
"Church trip planned for June 13. Sign up at church for details.",
"Leaving the church this Saturday at 8:00 AM. Please arrive early enough to load and be ready to depart on time."
)

Path("index.html").write_text(html)

print("Eastland homepage updated.")