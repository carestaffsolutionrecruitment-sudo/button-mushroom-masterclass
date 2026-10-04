# Deliverable Template: Raw Material C:N Ratio Calculator & Batch Sheet (Deliverable-202)

* **Template ID:** Deliverable-202
* **Version:** 2.0
* **Purpose:** A batch-calculation sheet to compute dry matter, carbon, nitrogen, C:N ratio, nitrogen %, gypsum, and water requirements for Phase I substrate preparation, using local Kenyan raw-material analyses or global reference values.
* **Linked Documents:** Module 2 · SOP-201 · KE-00 §2.1

---

## 1. Reference Analysis Library (dry-matter basis unless noted)

*Use lab results for your own suppliers whenever available. These are typical planning values.*

| Material | Dry matter (% of wet) | Carbon (% DM) | Nitrogen (% DM) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Wheat straw (Rift Valley) | 85–90 (use 88) | 42–45 (use 44) | 0.4–0.7 (use 0.6) | Primary carbon base |
| Barley straw | 85–90 | 42–45 | 0.5–0.8 | Faster breakdown |
| Rice straw (Mwea/Ahero) | 85–90 | 38–42 | 0.5–0.8 | High silica |
| Layer poultry manure | 50–75 (use 60) | 30–35 (use 32) | 2.5–4.0 (use 3.0) | Core nitrogen source |
| Broiler litter | 70–80 (use 75) | 33–38 (use 35) | 2.0–3.5 (use 2.8) | Bedding adds carbon |
| Kienyeji manure | 60–80 (use 70) | 25–30 (use 28) | 1.0–1.8 (use 1.5) | High ash/soil: **always lab-test** |
| Horse manure (straw-bedded) | 30–40 | 35–40 | 1.2–1.8 | Classic European base |
| Sugarcane bagasse | 45–55 (use 50) | 44–46 (use 45) | 0.2–0.4 (use 0.3) | Max 20–30% of the carbon base |
| Coffee husk | 85–90 (use 88) | 44–46 (use 45) | 1.0–1.8 (use 1.5) | Max 15–20% of the dry mix |
| Brewers' spent grain (fresh) | 20–25 | 45–50 | 3.5–4.5 | Use same day |
| Urea | ≈ 100 | 20 | 46 | N top-up |
| Ammonium sulphate | ≈ 100 | 0 | 21 | N top-up (also adds S) |
| Agricultural gypsum | ≈ 99 | 0 | 0 | 3–5% of total dry mass |

---

## 2. Formulas

For each ingredient i:

> **Dry matter (kg)** = Wet weight × DM%  ·  **Carbon (kg)** = Dry matter × C%  ·  **Nitrogen (kg)** = Dry matter × N%

> **C:N ratio** = Total carbon ÷ Total nitrogen  ·  **N% (DM)** = Total nitrogen ÷ Total dry matter × 100

**Water required to reach a target moisture M (e.g., 0.72):**

> **Target wet mass (kg)** = Total dry matter ÷ (1 − target moisture)  ·  **Water to add (L)** = Target wet mass − Total wet weight of ingredients

Add **+20–30%** in Kenyan hot/dry months (Jan–Feb, Sep–Oct) for evaporation.

**Targets:** C:N **25:1 – 30:1** at the start (falling to ≈ 17–20:1 by the end of Phase II) **and** N **1.5–1.8% DM**. Both must be met.

**Spreadsheet implementation** (one ingredient per row, columns A–H as in the batch sheet below):
* D (DM kg) `= B * C`  ·  G (C kg) `= D * E`  ·  H (N kg) `= D * F`
* C:N `= SUM(G:G) / SUM(H:H)`  ·  N% `= SUM(H:H) / SUM(D:D) * 100`
* Water `= SUM(D:D) / (1 - 0.72) - SUM(B:B)`

---

## 3. Worked Example 1 — Recipe KE-A "Rift Standard" (per 1,000 kg straw)

| Raw material | Wet weight (kg) | DM % | Dry weight (kg) | C % DM | N % DM | Total C (kg) | Total N (kg) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Wheat straw | 1,000 | 88% | 880.0 | 44% | 0.6% | 387.2 | 5.28 |
| Layer manure | 600 | 60% | 360.0 | 32% | 3.0% | 115.2 | 10.80 |
| Sugarcane bagasse | 200 | 50% | 100.0 | 45% | 0.3% | 45.0 | 0.30 |
| Urea | 10 | 100% | 10.0 | 20% | 46% | 2.0 | 4.60 |
| Agricultural gypsum | 40 | 99% | 39.6 | 0% | 0% | 0.0 | 0.00 |
| **TOTALS** | **1,850** | — | **1,389.6** | — | — | **549.4** | **20.98** |

* **C:N** = 549.4 ÷ 20.98 = **26.2 : 1** ✔
* **N% DM** = 20.98 ÷ 1,389.6 × 100 = **1.51%** ✔
* **Gypsum check:** 39.6 ÷ 1,389.6 = 2.8% of DM, at the low end. **Raise to 55–60 kg** if the compost turns greasy.
* **Water to 72% moisture:** 1,389.6 ÷ 0.28 = 4,963 kg target → 4,963 − 1,850 = **≈ 3,113 L** (≈ 3.1 m³ per tonne of straw).
* **Sensitivity:** without the 10 kg of urea, C:N = **33.4 : 1**, outside the target.

## 4. Worked Example 2 — Recipe KE-C "Kienyeji Cooperative" (per 1,000 kg straw)

| Raw material | Wet (kg) | DM % | DM (kg) | C % | N % | C (kg) | N (kg) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Wheat straw | 1,000 | 88% | 880.0 | 44% | 0.6% | 387.2 | 5.28 |
| Kienyeji manure | 900 | 70% | 630.0 | 28% | 1.5% | 176.4 | 9.45 |
| Urea | 20 | 100% | 20.0 | 20% | 46% | 4.0 | 9.20 |
| Gypsum | 45 | 99% | 44.6 | 0% | 0% | 0.0 | 0.00 |
| **TOTALS** | **1,965** | — | **1,574.6** | — | — | **567.6** | **23.93** |

* **C:N = 23.7 : 1**, **N = 1.52% DM** ✔
* **Lesson:** with only 10 kg of urea, C:N looks acceptable (≈ 29:1) but N falls to ≈ 1.24% DM, which is nitrogen-starved. Low-N, high-ash manures need **both** checks.

---

## 5. Blank Batch Sheet

* **Batch ID:** ______________ **Date stacked (Day 0):** ______________ **Yard manager:** ______________
* **Season / weather notes:** ______________

| Raw material (supplier) | Wet weight (kg) | DM % | Dry weight (kg) | C % DM | N % DM | Total C (kg) | Total N (kg) | Lab-verified? (Y/N) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :---: |
| Straw: ________ | | | | | | | | |
| Manure 1: ________ | | | | | | | | |
| Manure 2: ________ | | | | | | | | |
| Bagasse / husk: ________ | | | | | | | | |
| Urea / AS: ________ | | | | | | | | |
| Gypsum: ________ | | | | 0 | 0 | 0 | 0 | |
| **TOTALS** | | — | | — | — | | | |

| Result | Value | Target | OK? |
| :--- | :--- | :--- | :---: |
| C:N | | 25–30 : 1 | |
| N % DM | | 1.5–1.8% | |
| Gypsum % of DM | | 3–5% | |
| Water to add (L) | | Target moisture 70–75% | |
| Expected compost output (≈ 2.9 t per t straw) | | — | |

## 6. Phase I Daily Log (attach)

| Day | Date | Core temp (°C) at 3 points | Squeeze test | Water added (L) | Turn? | Smell / colour | Initials |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| 0 | | | | | Build | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | ✔ | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | ✔ + gypsum | | |
| 8 | | | | | | | |
| 9 | | | | | | | |
| 10 | | | | | ✔ | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | ✔ final | | |

## 7. Cost Line (feeds Deliverable-505)

| Material | Quantity | Unit price (KES) | Cost (KES) |
| :--- | ---: | ---: | ---: |
| Straw (kg) | | ≈ 10–18/kg | |
| Manure (kg) | | ≈ 3–7/kg | |
| Bagasse/husk (kg) | | ≈ 1–5/kg | |
| Urea (kg) | | ≈ 70–110/kg | |
| Gypsum (kg) | | ≈ 15–30/kg | |
| **Batch total** | | | |
| **Per tonne of compost produced** | | | |
