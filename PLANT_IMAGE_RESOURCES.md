# Plant Image Resources - Public Domain Sources

**Purpose**: Curated list of public domain plant identification image sources for survival-essentials knowledge base.

---

## Best Public Domain Sources

### 1. Biodiversity Heritage Library (BHL) ⭐ BEST

**URL**: https://www.biodiversitylibrary.org/

**What**: 150,000+ high-resolution botanical illustrations (copyright-free)
- Archive of 55+ million pages about earth's flora/fauna
- High-quality historical botanical illustrations
- Search by species name

**License**: Public domain
**Format**: High-resolution images (JPEG, TIFF)
**Coverage**: Global, including North American species

**How to Use**:
1. Search for specific plant (e.g., "Taraxacum officinale" for dandelion)
2. Filter by "Images" in search results
3. Download high-resolution versions
4. Attribution optional but recommended

**Best For**: Detailed botanical illustrations for identification

---

### 2. USDA PLANTS Database

**URL**: https://plants.usda.gov/

**What**: Standardized information about vascular plants in U.S. and territories
- Plant characteristics, distribution data
- Photos submitted by public and researchers
- Searchable by common name or scientific name

**License**: U.S. Public Domain (government work)
**Format**: Photos (JPEG)
**Coverage**: North America (U.S. focus)

**How to Use**:
1. Search plant by common or scientific name
2. Click "Gallery" tab for images
3. Download images (credit USDA PLANTS Database)

**Best For**: Photos of North American plants in natural habitat

---

### 3. USDA Weed Images Database

**URL**: https://data.nal.usda.gov/dataset/weed-images-source-images-weeds-and-weed-management-agriculture

**What**: Joint USDA/APHIS project with extensive plant images
- Categories: Aquatics, herbs/forbs, grasses, shrubs, trees, vines
- Many "weeds" are edible wild plants

**License**: U.S. Public Domain
**Format**: Photos
**Coverage**: North America

**How to Use**:
1. Browse by category or search
2. Download images
3. No attribution required (but recommended)

**Best For**: Common "weedy" edible plants (dandelion, plantain, clover)

---

### 4. USDA Pomological Watercolor Collection

**URL**: https://agdatacommons.nal.usda.gov/articles/dataset/U_S_Department_of_Agriculture_USDA_Pomological_Watercolor_Collection/24660282

**What**: 7,584 watercolor paintings of fruit and nut varieties
- Historical artwork (1886-1942)
- Beautiful, detailed illustrations
- Includes wild fruits (berries, nuts)

**License**: U.S. Public Domain
**Format**: High-resolution watercolors
**Coverage**: North American fruits/nuts

**Best For**: Acorns, hickory nuts, berries, wild fruits

---

### 5. Internet Archive - Field Guide PDFs

**URL**: https://archive.org/details/fieldguidetoedib0000pete_h5c3

**What**: "A Field Guide to Edible Wild Plants of Eastern and Central North America" by Peterson
- Complete PDF field guide
- Illustrations and descriptions
- Classic reference work

**License**: Public domain (out of copyright)
**Format**: PDF with illustrations
**Coverage**: Eastern/Central North America

**How to Use**:
1. Download full PDF
2. Extract relevant pages/images
3. Reference in survival guide

**Best For**: Complete plant profiles with illustrations

---

### 6. Wikimedia Commons - Plant Categories

**URL**: https://commons.wikimedia.org/wiki/Category:Edible_plants

**What**: User-contributed photos of plants
- Filter by "Edible plants" category
- Many high-quality photos
- Creative Commons or public domain

**License**: Varies (check each image - look for CC0 or Public Domain)
**Format**: Photos (various quality)
**Coverage**: Global

**How to Use**:
1. Search specific plant
2. Filter by "Free to use" or "Public domain"
3. Download, check license requirements
4. Attribution if required by CC license

**Best For**: Modern photos of plants in various growth stages

---

## Recommended Integration Strategy

### Option 1: Image Directory in Repo (Small Curated Set)

**Create**: `survival-essentials/images/plants/`

**Approach**:
- Download 20-30 key images for plants in 05_food.md
- One image per plant (best identification view)
- Optimize for small file size (<200KB each)
- Total: ~3-5MB for entire image collection

**Plants to prioritize** (from 05_food.md):
1. Dandelion (flower, leaves)
2. Cattail (seedhead, shoots)
3. Acorns (with oak leaves)
4. Blackberries/raspberries (fruit, leaves)
5. Clover (flower, leaves)
6. Wild onion/garlic (bulbs, leaves)
7. Plantain (leaves, growth pattern)
8. Pine (needles, cones)
9. Death Camas (WARNING image)
10. Poison Hemlock (WARNING image)
11. Water Hemlock (WARNING image)

**Pros**: Offline access, controlled quality, small storage footprint
**Cons**: Manual curation work

---

### Option 2: External Resource Links Only

**Approach**:
- Document best sources in this file
- Link to external resources from 05_food.md
- No images stored in repo

**Pros**: Zero storage footprint, always up-to-date sources
**Cons**: Requires internet to view images

---

### Option 3: Hybrid Approach ⭐ RECOMMENDED

**Approach**:
- Store 10-15 critical images in repo (deadly plants + most common edibles)
- Link to external sources for comprehensive identification
- Best of both worlds

**Critical images to store locally**:
1. Death Camas (DEADLY)
2. Poison Hemlock (DEADLY)
3. Water Hemlock (DEADLY - most important)
4. Dandelion (most common edible)
5. Cattail (high-calorie edible)
6. Wild onion vs Death Camas comparison
7. Plantain (common edible)
8. Acorns (high-calorie)

**Total storage**: ~1-2MB

---

## Download Instructions

### From Biodiversity Heritage Library

```bash
# Example: Download dandelion illustration
1. Go to https://www.biodiversitylibrary.org/
2. Search "Taraxacum officinale"
3. Click "Images" filter
4. Select high-quality botanical illustration
5. Click "Download" → Choose size → Save to survival-essentials/images/plants/
6. Rename: dandelion_taraxacum_officinale.jpg
```

### From USDA PLANTS Database

```bash
# Example: Download cattail photo
1. Go to https://plants.usda.gov/
2. Search "cattail" or "Typha latifolia"
3. Click "Gallery" tab
4. Right-click image → "Save image as"
5. Save to survival-essentials/images/plants/
6. Rename: cattail_typha_latifolia.jpg
```

### Batch Download Script (Optional)

If we want to automate downloads, we can create a Python script:

```python
# download_plant_images.py (for future use)
import requests
from pathlib import Path

PLANT_IMAGES = {
    "dandelion": "https://...",  # URLs from USDA/BHL
    "cattail": "https://...",
    # etc.
}

for plant_name, url in PLANT_IMAGES.items():
    response = requests.get(url)
    if response.status_code == 200:
        Path(f"images/plants/{plant_name}.jpg").write_bytes(response.content)
        print(f"Downloaded {plant_name}")
```

---

## Image Attribution Template

When using public domain images, include attribution file:

**File**: `survival-essentials/images/plants/ATTRIBUTIONS.md`

```markdown
# Plant Image Attributions

## Dandelion (dandelion_taraxacum_officinale.jpg)
- Source: Biodiversity Heritage Library
- Original: [Title of original work]
- Public Domain

## Cattail (cattail_typha_latifolia.jpg)
- Source: USDA PLANTS Database
- Photographer: [Name if available]
- U.S. Public Domain

[etc.]
```

---

## Image Formatting Guidelines

**For repo storage**:
- Format: JPEG (smaller file size than PNG)
- Resolution: 1200-1600px wide (sufficient for identification)
- Compression: 70-80% quality (balance size vs. clarity)
- Naming: `common-name_scientific-name.jpg` (e.g., `dandelion_taraxacum-officinale.jpg`)
- Target size: <200KB per image

**Optimization tools**:
- ImageOptim (Mac)
- TinyPNG (web-based)
- `jpegoptim` (command line)

---

## Next Steps

### This Week
1. **Decide integration approach** (Hybrid recommended)
2. **Download 8 critical images** (3 deadly plants + 5 common edibles)
3. **Create images/plants/ directory**
4. **Create ATTRIBUTIONS.md**

### This Month
1. **Expand to 20-30 images** (all plants in 05_food.md)
2. **Update 05_food.md** with image links
3. **Test offline viewing** (ensure images display)

### Optional
1. **Create plant identification visual guide** (comparison sheet)
2. **Add seasonal identification photos** (same plant in different seasons)
3. **Build lookalike comparison images** (wild onion vs Death Camas)

---

## Key Takeaways

1. **Biodiversity Heritage Library = best quality** (150,000+ botanical illustrations)
2. **USDA PLANTS = best for North American habitat photos**
3. **Hybrid approach recommended** (critical images in repo, link to external for comprehensive)
4. **Prioritize deadly plants** (Death Camas, Poison Hemlock, Water Hemlock)
5. **Store ~1-2MB of images** (8-10 critical plants)
6. **All sources are truly public domain** (no licensing issues)

---

**Last Updated**: 2025-11-02
**Status**: Research complete, ready for image integration
