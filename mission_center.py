from pathlib import Path

path = Path("index.html")
html = path.read_text()

html = html.replace(
'          <p style="max-width: 850px; margin: 24px auto; font-size: 1.15rem; line-height: 1.8;">',
'          <p style="max-width: 850px; margin: 24px auto; font-size: 1.15rem; line-height: 1.8; text-align: center;">'
)

html = html.replace(
'          <p style="max-width: 900px; margin: 36px auto 0; font-style: italic; opacity: .85;">',
'          <p style="max-width: 900px; margin: 36px auto 0; font-style: italic; opacity: .85; text-align: center;">'
)

path.write_text(html)

print("Mission content centered.")
