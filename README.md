# VAN PATTEN-ALASTOR — VERSION 3.0
## The Lifestyle Catalogue · Multi-page website prototype

### Preview
Because the catalogue uses `fetch()` to load JSON files, run the site through a local server:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

### Separate pages
- `index.html` — Home
- `house.html` — The House
- `person.html` — Lifestyle archetypes
- `collections.html` — Product catalogue, filters, brand directory and price comparison
- `lifestyle.html` — Automotive, residences, offices, travel, culture, grooming and media
- `transformations.html` — Expandable programme details
- `journal.html` — Editorial preview
- `private-office.html` — Private-client enquiry brief
- `privacy.html` and `terms.html` — Draft policy pages

### Product pricing
- `products.json` contains curated sample products (including watches, tailoring, outerwear, footwear, formal accessories, eyewear, leather goods, fragrance and luggage), brand references, image URLs, brand prices, proposed house prices and original listing URLs.
- Brand prices were checked against brand or retailer product pages during preparation (November 8, 2026). They can change and should be rechecked before publication.
- House prices are set to brand-price parity as a provisional reference because Van Patten-Alastor has not supplied verified wholesale terms, supplier discounts, service fees or a final pricing policy. These are not confirmed retail offers.
- Where an exact brand price was not verified, the catalogue says “Request price”.
- Product availability, authorized supply, partnership status and stock are not confirmed.
- `brands.json` contains the wider brand universe from the supplied buying plan. Brands listed there are sourcing references only, not claims of affiliation or authorization.

### Photography
The site uses subject-specific remote product images and editorial images from brand, retailer and editorial image hosts. Confirm usage rights, hotlink permissions and licensing before public/commercial use. Replace remote images with approved local assets or licensed image feeds for production.

### Important limitations
- The enquiry form only prepares and copies a local brief; it does not send, store or transmit client information.
- No checkout, payments, inventory database, account system, booking engine or CRM is connected.
- Packages are service frameworks, not fixed-price promises.
- No counterfeit branded replicas are represented or offered.
- Privacy and terms pages are drafts, not legal advice or final policies.
- Test the website through a local web server. Some browser restrictions prevent `fetch()` from loading JSON when opening the HTML directly from the file system.

### Main files
- `app.js` — navigation, catalogue filtering, form behavior
- `styles.css` — responsive design
- `products.json` — selected product cards and prices
- `brands.json` — brand directory
- `assets/` — supplied logo and heraldic crest
