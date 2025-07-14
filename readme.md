# EKOM Content System – Structured PDP Knowledge Architecture

Welcome to the EKOM Content System. This repository powers our educational infrastructure for teaching ecommerce teams how to build structured, discoverable product detail pages (PDPs) that work across Google, Meta, TikTok, and AI assistants.

---

## 🧠 Vision

We're building more than a blog. This system is an interlinked **knowledge graph** of ecommerce fundamentals:

* Every **Lesson** teaches a single, actionable concept.
* Every **Reference Term** defines a piece of PDP or metadata jargon.
* Lessons link out to Reference Terms.
* Reference Terms link back to Lessons that mention them.
* **Categories** group Reference Terms into digestible learning playlists.
* The result: a seamless curiosity loop where ecommerce teams learn what matters, why it matters, and how to fix it.

---

## 🎯 Outcomes

The goal is to create a **CMS-ready, auto-interlinked content system** that:

* Can be **imported into Webflow** via CSVs
* Powers **structured educational content** for EKOM.ai
* **Auto-generates hyperlinks** in canonical content using token replacement
* Ensures **metadata accuracy, content governance**, and platform readability
* Supports **scaling up** to hundreds of lessons and glossary terms
* Drives **AI readability** and modern SEO via structured HTML and internal link depth

---

## 📁 Folder Structure

Each file maps to a Webflow CMS Collection:

```
ekom-content/
├── lessons.csv                  # Educational modules (with links to reference terms)
├── reference-terms.csv          # Glossary entries (with related lesson back-links)
├── categories.csv               # Thematic groupings for glossary navigation
├── courses.csv                  # Course wrappers (e.g., “The PDP Field Guide”)
├── lookup.csv                   # Token → URL map for hyperlink replacement
├── read.py                      # Diagnostic script to load, inspect, and validate the system
└── README.md                    # This file
```

---

## 🔗 Auto-Linking System

Canonical HTML content (inside each lesson) uses placeholder tokens like:

```
[[SKU]]
[[JSON‑LD]]
[[Anatomy of a Healthy PDP]]
```

The `lookup.csv` maps each token to a URL, along with its type:

| token                          | url                                     | type      |
| ------------------------------ | --------------------------------------- | --------- |
| \[\[SKU]]                      | /resources/reference/sku                | reference |
| \[\[Anatomy of a Healthy PDP]] | /resources/lessons/pdp-health-checklist | lesson    |

Use this for search-and-replace or Apps Script automation to inject `<a>` tags during HTML post generation.

---

## 🧱 Data Model: Webflow Collections

### `Lessons` → `/resources/lessons/{slug}`

| Field               | Type                        |
| ------------------- | --------------------------- |
| title               | Text                        |
| slug                | Slug                        |
| excerpt             | Text                        |
| references          | Multi-ref → Reference Terms |
| related-lessons     | Multi-ref → Lessons         |
| canonical-html-body | Rich Text                   |
| course              | Ref → Courses               |

### `Reference Terms` → `/resources/reference/{slug}`

| Field           | Type                |
| --------------- | ------------------- |
| name            | Text                |
| slug            | Slug                |
| definition      | Short text          |
| more-details    | Long text           |
| category        | Ref → Categories    |
| related-lessons | Multi-ref → Lessons |

### `Categories` → `/resources/categories/{slug}`

| Field | Type              |
| ----- | ----------------- |
| name  | Text              |
| slug  | Slug              |
| blurb | Short description |

### `Courses` → `/resources/courses/{slug}`

| Field       | Type                      |
| ----------- | ------------------------- |
| name        | Text                      |
| slug        | Slug                      |
| description | Long text                 |
| status      | Option (Published, Draft) |

---

## ✅ Setup Checklist

1. Fill out each sheet: `lessons.csv`, `reference-terms.csv`, `categories.csv`, `courses.csv`
2. Export each as CSV from Google Sheets
3. Import into Webflow CMS collections **in this order**:

   * Categories
   * Reference Terms
   * Courses
   * Lessons
4. When generating canonical post content:

   * Use token-based writing (`[[JSON‑LD]]`, `[[SKU]]`)
   * Run token replacement using `lookup.csv` before final import

---

## 🔍 read.py Script

Use this to:

* Load and preview each dataset
* Validate missing references
* Print your lookup table
* Scaffold your automation for generating canonical content

---

## 📌 Scaling Later

* Add hundreds of Reference Terms without touching lesson bodies
* Add new Lessons that auto-link back to Reference Terms
* Drive SEO via internal linking and glossary coverage
* Power canonical HTML generation from structured tokens

---

## 🤖 Coming Soon

* `generate_html.py`: Replace tokens with anchor tags
* `webflow_import.py`: Push data into Webflow CMS via API
* `feed_checker.py`: Validate structured data formats for compliance

---

**EKOM is building a better content graph — not just for humans, but for machines too.**
