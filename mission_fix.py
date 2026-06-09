from pathlib import Path

path = Path("index.html")
html = path.read_text()

html = html.replace(
'''          <p style="margin-top: 10px; font-weight: 600;">
            — Matthew 22:37–39
          </p>''',
'''          <p style="margin-top: 12px; font-weight: 600; text-align: center;">
            — Matthew 22:37–39
          </p>'''
)

html = html.replace(
'''<h2 id="mission-title">A church family centered on Jesus Christ.</h2>''',
'''<h2 id="mission-title" style="font-size: clamp(2.75rem, 5vw, 4.5rem);">
            A church family centered on Jesus Christ.
          </h2>'''
)

path.write_text(html)

print("Mission section refined.")