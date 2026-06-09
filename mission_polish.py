from pathlib import Path

path = Path("index.html")
html = path.read_text()

old = """          <h2 id="mission-title">A church family centered on Jesus Christ.</h2>
          <p>
            Our mission is to help people know Jesus, grow in God's Word,
            worship together, care for one another, and serve our community
            with the love of Christ.
          </p>"""

new = """          <h2 id="mission-title">A church family centered on Jesus Christ.</h2>
          <p style="max-width: 850px; margin: 24px auto; font-size: 1.15rem; line-height: 1.8;">
            Our mission is to help people know Jesus, grow in God's Word,
            worship together, care for one another, and share the hope of Christ
            with our community.
          </p>

          <p style="max-width: 900px; margin: 36px auto 0; font-style: italic; opacity: .85;">
            "Love the Lord your God with all your heart and with all your soul and with all your mind...
            and love your neighbor as yourself."
          </p>

          <p style="margin-top: 10px; font-weight: 600;">
            — Matthew 22:37–39
          </p>"""

html = html.replace(old, new)

path.write_text(html)

print("Mission section polished.")
