# US CRE Loan Maturity & Risk Dataset — Data Quality Report

**Prepared by IT Altitudes Inc.**

**Dataset:** U.S. Commercial Real Estate Loan Maturity & Risk Dataset  
**Original Source:** U.S. Securities and Exchange Commission (SEC) — EDGAR CMBS Filings  
**Report Type:** Dataset Quality & Transparency Summary

---

## 1. Executive Summary

This report provides an overview of the US CRE Loan Maturity & Risk Dataset's documented coverage, curation approach, quality-review criteria, and known limitations.

The dataset is designed to support commercial real estate research, loan maturity analysis, credit risk studies, and non-production data engineering.

This is a publisher-issued transparency report, not an independent audit or SEC certification.

## 2. Dataset Coverage

| Metric | Documented Value |
|---|---:|
| Full curated loan entries | 554 |
| Free preview records | 50 |
| Geographic coverage | United States |
| Original source | SEC EDGAR |
| Source category | Commercial mortgage-backed securities (CMBS) |
| Full buyer kit | Excel and CSV versions |

These figures reflect existing IT Altitudes dataset documentation. They have not been independently recalculated for this report.

## 3. Data Preparation & Curation

The dataset was prepared using SEC EDGAR CMBS filing information.

The documented curation process included:

- Consolidating source records from multiple extraction stages
- Excluding non-U.S. records
- Reviewing duplicate candidates
- Excluding records outside the intended loan-level scope
- Organizing relevant loan information into a structured dataset
- Preparing buyer documentation and preview materials

These steps describe the documented preparation workflow. This report does not independently establish the outcome of each check.

## 4. Data Quality Review Framework

| Quality Dimension | Review Objective | Evidence Status |
|---|---|---|
| Record completeness | Identify missing and blank loan fields | Quantitative results pending |
| Duplicate detection | Identify repeated loan entries | Quantitative results pending |
| Geographic consistency | Check U.S. coverage | Detailed results pending |
| Loan identifiers | Review identifier availability and consistency | Detailed results pending |
| Maturity dates | Review date formats and missing values | Detailed results pending |
| Numeric fields | Review amounts, balances, and rates where present | Detailed results pending |
| Property relationships | Review loan-to-property associations | Detailed results pending |
| Source provenance | Document SEC filing origins | SEC EDGAR identified |
| Cross-format consistency | Compare corresponding Excel and CSV records | Detailed results pending |

The checks listed above should not be interpreted as passed tests without supporting measurements.

## 5. Missing-Value Assessment

SEC CMBS filings may contain different levels of detail depending on the filing, reporting period, and source disclosures.

Missing information does not necessarily indicate a processing error.

**Measurement status:**

- Total missing values: Pending validation
- Field-level completeness: Pending validation
- Missing-value percentage: Pending validation
- Required-field completeness: Pending validation

## 6. Duplicate-Record Assessment

Duplicate analysis should distinguish between:

- Exact duplicate records
- Repeated loan identifiers
- Multiple reporting periods for the same loan
- Related loan interests or participations
- Separate properties associated with a single loan

A repeated property or related loan interest should not automatically be classified as an erroneous duplicate.

**Measured duplicate count:** Pending validation.

## 7. Loan & Property Relationship Integrity

The buyer kit includes loan-level information and supporting property-related records.

Recommended integrity checks include:

- Identifying unmatched loan-to-property references
- Reviewing repeated property associations
- Checking identifier consistency
- Confirming that related records are not incorrectly counted as distinct whole mortgages

**Measured relationship-integrity results:** Pending validation.

## 8. Source Attribution & Provenance

**Original Source:** U.S. Securities and Exchange Commission — EDGAR.

The dataset references publicly available commercial mortgage-backed securities filing information.

SEC Regulation AB includes asset-level disclosure requirements for certain commercial mortgage-backed securities. Individual filing data may reflect different reporting periods and loan structures.

IT Altitudes Inc. independently curates and organizes the dataset and is not affiliated with or endorsed by the SEC.

## 9. Known Limitations

- The dataset is a static reference snapshot.
- Loan balances and maturity information may change.
- Some records may represent reported loan interests rather than distinct whole mortgages.
- Source filings may contain missing or amended information.
- Multiple filings may reference related loans or properties.
- The dataset does not independently predict defaults, losses, or refinancing outcomes.
- No independently measured overall quality score is claimed in this report.

## 10. Intended Buyer Applications

The dataset may support:

- Commercial real estate loan maturity research
- Historical CMBS market analysis
- Credit risk research
- Loan portfolio exploration
- Data visualization and dashboard development
- ETL and analytical workflow testing
- Academic and institutional research

These are potential applications, not guarantees of fitness for any specific financial decision.

## 11. Validation Status

**Current status:** Dataset quality and transparency documentation prepared.

**Pending:** Quantitative validation of missing values, duplicates, identifiers, loan-property relationships, and cross-format consistency.

No independently measured accuracy percentage or overall quality score is claimed.

## 12. License & Disclaimer

- [License & Usage Terms](LICENSE.md)
- [Source & Liability Disclaimer](DISCLAIMER.md)

The dataset is intended for research and analytical use.

It is not financial advice, a live credit monitoring service, or a substitute for independent underwriting and due diligence.

## 13. Free Preview & Complete Dataset

**[Explore the Free GitHub Preview](https://github.com/ITAltitudesDataset/us-cre-loan-maturity-risk-dataset-preview)**

**[Purchase the Complete US CRE Dataset](https://italtitudes.gumroad.com/l/cyvqx)**

## 14. Support

**IT Altitudes Inc.**

support@italtitudesdataset.zohodesk.in

---

*Publisher-Issued Data Quality & Transparency Report — 2026*
