# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage

### Purpose
The purpose of this stage is to design and implement a storage solution for data used in our predictive modeling project.  
A robust data storage strategy ensures **reproducibility, traceability, and scalability** as the project evolves.  

---

### Data Sources
- **Scraped Data**: Constituents of the S&P 500 index scraped from an external source (e.g., Slickcharts, Wikipedia).  
- **API Data**: Historical price and return data retrieved from Yahoo Finance using the `yfinance` library.  
- **Inline Demo Data (fallback)**: Small static table embedded in the notebook for validation and testing.  

---

### Storage Design
We organize data under the `/data/` directory with clear subfolders:  
- `/data/raw/` → unprocessed API or scraped files (CSV/JSON).  
- `/data/processed/` → cleaned and validated datasets ready for modeling.  
- `/data/external/` → any third-party datasets added manually.  

**File naming conventions**:  
- `sp500_companies_<date>.csv` for scraped lists.  
- `prices_<SYMBOL>_<start>-<end>.csv` for time series data.  

---

### Implementation
- Used **pandas** `to_csv` and `read_csv` for file-based persistence.  
- Applied **validation functions** (`validate(df, cols)`) before saving, ensuring schema consistency.  

**Example workflow**:  
1. Scrape or download data → `df_scrape` or `df_api`.  
2. Validate → ensure required columns exist and datatypes are correct.  
3. Save → `df.to_csv("data/raw/filename.csv", index=False)`.  
4. Reload → use in downstream notebooks with `pd.read_csv`.  

---

### Benefits
- **Reproducibility**: All team members can use the same saved datasets.  
- **Versioning**: Dated filenames allow comparison across runs.  
- **Separation of Concerns**: Raw vs. processed folders clarify lifecycle stage.  
- **Resilience**: If API or website is down, stored CSVs preserve work continuity.  

---

### Risks & Mitigation
- **Schema drift** (column names change on source websites): mitigated by validation layer.  
- **Stale data**: mitigated by re-running scrape jobs regularly and timestamping saved files.  
- **Storage limits**: large datasets may exceed local repo; consider external storage (S3, GCS) for scaling.  

---
