import pandas as pd
from pathlib import Path

# Set folder path
DATA_DIR = Path(__file__).parent

# Load CSVs
lessons = pd.read_csv(DATA_DIR / "lessons.csv")
reference_terms = pd.read_csv(DATA_DIR / "reference_terms.csv")
categories = pd.read_csv(DATA_DIR / "categories.csv")
courses = pd.read_csv(DATA_DIR / "courses.csv")

# Optional lookup for token-to-link mapping
lookup_path = DATA_DIR / "lookup.csv"
lookup = pd.read_csv(lookup_path) if lookup_path.exists() else pd.DataFrame()

# Print summaries
print("\n🧭 Lessons")
print(lessons[["title", "slug", "references", "related-lessons"]].head())

print("\n📚 Reference Terms")
print(reference_terms[["name", "slug", "category (single‑ref → Categories)", "related Lessons"]].head())

print("\n🎯 Categories")
print(categories[["name", "slug"]].head())

print("\n🎓 Courses")
print(courses[["name", "slug"]].head())

# Optional: validate slugs used in relationships
def validate_slugs():
    missing_refs = []
    known_refs = set(reference_terms["name"])
    for idx, row in lessons.iterrows():
        refs = str(row.get("references", "")).split(",")
        for ref in refs:
            ref = ref.strip()
            if ref and ref not in known_refs:
                missing_refs.append((row["slug"], ref))
    if missing_refs:
        print("\n🚨 Missing Reference Terms:")
        for lesson, ref in missing_refs:
            print(f" - {ref} (used in lesson: {lesson})")

validate_slugs()

# Optional: print lookup table (tokens → hyperlinks)
if not lookup.empty:
    print("\n🔗 Lookup table (token → link):")
    print(lookup.head())

# Future expansion: HTML generator, token replacement, auto-linking system...
