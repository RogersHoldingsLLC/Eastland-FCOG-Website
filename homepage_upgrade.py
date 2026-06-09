from pathlib import Path

path = Path("index.html")
html = path.read_text()

html = html.replace(
'''        <a href="#service-times">Services</a>
        <a href="#ministries">Ministries</a>
        <a href="#giving">Give</a>
        <a href="#announcements">Announcements</a>
        <a href="#connect">Connect</a>''',
'''        <a href="#service-times">Services</a>
        <a href="#visit">Visit</a>
        <a href="#mission">Mission</a>
        <a href="#ministries">Ministries</a>
        <a href="#messages">Messages</a>
        <a href="#giving">Give</a>
        <a href="#connect">Connect</a>'''
)

visit_mission = '''
      <section class="content-section visit-section" id="visit" aria-labelledby="visit-title">
        <div class="section-heading">
          <p class="eyebrow">Plan Your Visit</p>
          <h2 id="visit-title">You're welcome at Eastland.</h2>
          <p>
            Whether this is your first time in church or you're looking for a church family,
            we want you to feel comfortable, welcomed, and encouraged.
          </p>
        </div>

        <div class="info-grid four-column">
          <article class="info-card">
            <p class="label">What to Expect</p>
            <h3>Worship and the Word</h3>
            <p>
              You'll find a friendly church family, Christ-centered worship, prayer,
              and preaching from God's Word.
            </p>
          </article>
          <article class="info-card">
            <p class="label">Kids & Youth</p>
            <h3>Room to Grow</h3>
            <p>
              Children's Church and Youth Group help students learn about Jesus in
              age-appropriate ways.
            </p>
          </article>
          <article class="info-card">
            <p class="label">What to Wear</p>
            <h3>Come as You Are</h3>
            <p>
              You'll see everything from casual clothes to Sunday best. Wear what
              helps you feel comfortable coming to worship.
            </p>
          </article>
          <article class="info-card">
            <p class="label">When to Arrive</p>
            <h3>A Few Minutes Early</h3>
            <p>
              Arriving 10 to 15 minutes early gives you time to park, find a seat,
              and meet someone before service begins.
            </p>
          </article>
        </div>
      </section>

      <section class="mission-section" id="mission" aria-labelledby="mission-title">
        <div>
          <p class="eyebrow">Our Mission</p>
          <h2 id="mission-title">Worship. Grow. Love. Serve.</h2>
          <p>
            Eastland First Church of God exists to help people worship Jesus,
            grow in God's Word, love one another, and serve our community.
          </p>
        </div>
      </section>
'''

html = html.replace(
'''      <section class="content-section pastors" aria-labelledby="pastors-title">''',
visit_mission + '''
      <section class="content-section pastors" aria-labelledby="pastors-title">'''
)

html = html.replace(
'''              Pastor James serves Eastland as Senior Pastor, helping lead the
              church in worship, teaching, and care for the congregation. Donna
              serves alongside him in the life and ministry of the church.''',
'''              Pastor James and Donna serve Eastland with a heart for worship,
              biblical teaching, and caring for the church family. Their desire is
              to help people know Christ, grow in faith, and feel at home at Eastland.'''
)

html = html.replace(
'''              Pastor Stephen serves Eastland as Associate Pastor, supporting the
              ministries and life of the church. Keri serves alongside him in
              the life and ministry of the church.''',
'''              Pastor Stephen and Keri serve alongside the Eastland church family,
              supporting ministry, discipleship, and the everyday life of the church.
              A new photo and additional bio details will be added soon.'''
)

messages = '''
      <section class="content-section messages-section" id="messages" aria-labelledby="messages-title">
        <div class="section-heading">
          <p class="eyebrow">Messages</p>
          <h2 id="messages-title">Sermon archive coming soon.</h2>
          <p>
            We are preparing a place for recent messages and service videos.
            For now, visit our Facebook page for livestreams, past services,
            and church updates.
          </p>
        </div>
        <div class="center-actions">
          <a class="button primary" href="https://www.facebook.com/EastlandFirstChurchOfGod">
            Watch on Facebook
          </a>
        </div>
      </section>
'''

html = html.replace(
'''      <section class="giving-section" id="giving" aria-labelledby="giving-title">''',
messages + '''
      <section class="giving-section" id="giving" aria-labelledby="giving-title">'''
)

html = html.replace("Support the ministry of Eastland.", "Online Giving Coming Soon")

html = html.replace(
'''Online giving is coming soon. This section can connect to your
            church's preferred giving provider when the account is ready.''',
'''Online giving is not available yet, but it is being prepared. Please
            check back soon for updates from the church.'''
)

html = html.replace(
'''          <article class="announcement-card">
            <picture>
              <source
                srcset="assets/images/vbs-2026-slide.jpg"
                type="image/jpeg"
              />
              <img
                src="assets/images/vbs-2026-slide.jpg"
                alt="VBS 2026 Jesus Is The Light"
                width="1536"
                height="1024"
                loading="lazy"
                decoding="async"
              />
            </picture>
            <div>
              <h3>VBS 2026</h3>
              <p>Jesus Is The Light. More details are available from the church.</p>
            </div>
          </article>''',
''
)

path.write_text(html)
print("Homepage upgrade complete.")