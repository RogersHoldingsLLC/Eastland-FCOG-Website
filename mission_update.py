from pathlib import Path

path = Path("index.html")
html = path.read_text()

html = html.replace(
'''          <h2 id="mission-title">Worship. Grow. Love. Serve.</h2>
          <p>
            Eastland First Church of God exists to help people worship Jesus,
            grow in God's Word, love one another, and serve our community.
          </p>''',
'''          <h2 id="mission-title">A church family centered on Jesus Christ.</h2>
          <p>
            Our mission is to help people know Jesus, grow in God's Word,
            worship together, care for one another, and serve our community
            with the love of Christ.
          </p>'''
)

path.write_text(html)
print("Mission section updated.")
