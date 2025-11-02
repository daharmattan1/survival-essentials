# Survival Knowledge Repositories - Setup Guide

This guide contains instructions for cloning and setting up offline survival knowledge bases for apocalypse/end-of-technology scenarios.

## Best Repositories (Markdown-Based)

### 1. ligi/SurvivalManual (RECOMMENDED)
**Format**: Markdown files, offline-first design
**Content**: Comprehensive wilderness survival techniques

```bash
cd c:\Users\victor\claude-code-repos\
git clone https://github.com/ligi/SurvivalManual.git
```

### 2. GodHermit/survival-manual
**Format**: International survival manual with offline articles
**Content**: Multilingual survival knowledge

```bash
cd c:\Users\victor\claude-code-repos\
git clone https://github.com/GodHermit/survival-manual.git
```

### 3. PR0M3TH3AN/Survival-Data
**Format**: Offline survival database
**Content**: Structured survival information

```bash
cd c:\Users\victor\claude-code-repos\
git clone https://github.com/PR0M3TH3AN/Survival-Data.git
```

### 4. alx-xlx/awesome-survival
**Format**: Curated links + torrent/magnet links to massive collections
**Content**: Index to CD3WD (4,300+ PDFs), military manuals (22,000+), textbooks, encyclopedias

```bash
cd c:\Users\victor\claude-code-repos\
git clone https://github.com/alx-xlx/awesome-survival.git
```

## Major Collections Referenced in awesome-survival

### CD3WD Collection
- **Size**: 4,300+ PDF documents
- **Content**: Homesteading, agriculture, water systems, shelter, appropriate technology, rebuilding civilization
- **Access**: Available via torrent links in the awesome-survival repository
- **Format**: PDFs organized by topic

### Military Survival Manuals
- **Size**: 22,000+ documents
- **Content**: Military field manuals, survival techniques, emergency procedures
- **Access**: Torrent links in awesome-survival repo

### Medical & Science Textbooks
- **Content**: Medical procedures, anatomy, pharmacology, chemistry, physics
- **Format**: PDFs and ebooks
- **Access**: Links provided in awesome-survival repo

### Encyclopedia Collections
- **Content**: General knowledge, history, geography, technology
- **Format**: Various (PDF, HTML, offline databases)
- **Access**: Kiwix, Anna's Archive links in awesome-survival repo

## Setup Workflow

### Step 1: Clone All Markdown Repositories
```bash
# Create survival knowledge directory
mkdir c:\Users\victor\SurvivalKnowledge
cd c:\Users\victor\SurvivalKnowledge

# Clone all repos
git clone https://github.com/ligi/SurvivalManual.git
git clone https://github.com/GodHermit/survival-manual.git
git clone https://github.com/PR0M3TH3AN/Survival-Data.git
git clone https://github.com/alx-xlx/awesome-survival.git
```

### Step 2: Download PDF Collections (Optional)
After cloning awesome-survival, open the README.md and use the torrent/magnet links to download:
- CD3WD collection (homesteading/primitive skills)
- Military manuals collection
- Medical textbooks
- Encyclopedia collections

### Step 3: Organize Directory Structure
```
c:\Users\victor\SurvivalKnowledge\
├── SurvivalManual\           # Main markdown survival guide
├── survival-manual\           # International survival manual
├── Survival-Data\             # Offline database
├── awesome-survival\          # Index and links
└── PDFs\                      # Create this folder manually
    ├── CD3WD\                # Homesteading & appropriate tech
    ├── Military\             # Military manuals
    ├── Medical\              # Medical textbooks
    └── Encyclopedia\         # Reference materials
```

## Backup Strategy

1. **Local Hard Drive**: Store in `c:\Users\victor\SurvivalKnowledge\`
2. **External Drive**: Copy entire folder to external USB/SSD
3. **Network Backup**: Optional cloud backup for redundancy
4. **Physical Media**: Consider burning critical PDFs to DVD/Blu-ray

## Key Topics Covered

- **Primitive Skills**: Fire starting, shelter building, tool making
- **Agriculture**: Crop cultivation, seed saving, soil management
- **Homesteading**: Animal husbandry, food preservation, water systems
- **Medical**: Emergency medicine, herbal remedies, first aid
- **Navigation**: Maps, compass, celestial navigation
- **Foraging & Hunting**: Edible plants, trapping, fishing
- **Water**: Procurement, purification, well construction
- **Energy**: Solar, wind, hydroelectric, wood gasification
- **Communication**: Ham radio, mesh networks, signal protocols
- **Construction**: Building techniques, appropriate technology
- **Food Preservation**: Canning, smoking, drying, fermenting

## Additional Resources

### 667 Free Survival PDFs
Website: https://seasonedcitizenprepper.com/preparedness-downloads/
- Free downloadable survival manuals
- Topics: wilderness survival, homesteading, prepping

### Kiwix (Offline Wikipedia & More)
- Download entire Wikipedia offline
- Medical encyclopedias, textbooks, reference materials
- Links in awesome-survival repo

### OpenStreetMap Data
- Offline maps for navigation
- Can be downloaded regionally
- Links in awesome-survival repo

## Technologies for Offline Access

1. **Markdown Viewers**: Any text editor, VS Code, Obsidian
2. **PDF Readers**: Adobe Reader, Foxit, SumatraPDF
3. **Wiki Viewers**: Kiwix for offline encyclopedia access
4. **E-book Readers**: Calibre for managing ebook collections

## Notes

- All repositories are designed to work completely offline
- Markdown files are human-readable in any text editor
- Total storage needed: ~50-100GB for complete collections
- Regular updates recommended while internet is available
- Consider versioning: clone repos periodically to capture updates

## Priority Download Order

1. **SurvivalManual** (small, markdown, immediately useful)
2. **awesome-survival** (index to everything else)
3. **CD3WD PDFs** (4,300 comprehensive homesteading docs)
4. **Medical textbooks** (critical knowledge)
5. **Military manuals** (tactical survival info)
6. **Encyclopedias** (general reference)

## License & Legal

- Most content is open source or public domain
- CD3WD is specifically designed for knowledge preservation
- Check individual repository licenses before redistribution
- Personal use for survival preparation is generally permitted
