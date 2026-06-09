from pathlib import Path

path = Path("index.html")
html = path.read_text()

html = html.replace(
'<section class="mission-section" id="mission" aria-labelledby="mission-title">',
'<section class="mission-section" id="mission" aria-labelledby="mission-title" style="text-align: center;">'
)

html = html.replace(
'<p class="eyebrow">Our Mission</p>',
'<p class="eyebrow" style="text-align: center;">Our Mission</p>'
)

path.write_text(html)
print("Mission section fully centered.")
