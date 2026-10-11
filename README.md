# Eastland First Church of God Website

Static website for Eastland First Church of God in Mount Sterling, KY.

## Tech Stack

- HTML
- CSS
- Static assets

## Main Files

- `index.html`
- `styles.css`
- `site.webmanifest`
- `assets/`

## Maintenance Notes

- Update announcements directly in `index.html`.
- Replace images in `assets/images`.
- Online giving intentionally remains "coming soon" until board/provider information is finalized.

### Eastland Youth Parent Updates

Parent Updates use simple static pages under `parent-updates/`:

1. Add each newsletter as its own directory with an `index.html` file so it has a permanent URL.
2. Add the new article to `parent-updates/index.html`, keeping entries newest first.
3. Update the “Read Our Latest Parent Update” link in the Youth Night announcement in `index.html` so it points directly to the newest article.
4. Keep all previous article directories available with their original dates and content.

Do not add future articles until their copy is approved. No newsletter subscription, registration, or email collection is used.

## Deployment

This is a static site ready for standard hosting, Vercel, or Netlify.
