# Deliverable Template: Flush Yield Tracking & Contamination Diagnostic Flowchart (Deliverable-404)

* **Template ID:** Deliverable-404
* **Version:** 2.0
* **Purpose:** Record harvest weights by room, flush, and grade; calculate yield KPIs (kg/m², kg/tonne of compost, biological efficiency) and revenue in KES; and diagnose pests, diseases, and physiological disorders.
* **Linked Documents:** SOP-401 · SOP-402 · SOP-403 · Module 4 · Module 5 · Deliverable-505

---

## Part 1: Flush Yield Tracking Sheet

### 1.1 Crop header

| Field | Entry |
| :--- | :--- |
| Room / crop ID | |
| Strain | |
| Bed area (m²) | |
| Spawned compost, wet (kg) | |
| Compost dry matter % (from Phase II release; typically 30–34%) | |
| Compost dry weight (kg) = wet × DM% | |
| Casing date / pinning shock date / first pick date | |
| Pin uniformity score (1 = poor … 5 = excellent) | |

### 1.2 Yield by flush and grade

| Flush | Harvest window (days from first pick) | Grade A Button (kg) | Grade B Cup (kg) | Grade C Flats (kg) | Rejects (kg, destroyed) | Total saleable (kg) | kg/m² | % of crop total |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Flush 1** | Days 1–5 | | | | | | | (≈ 45–50%) |
| **Flush 2** | Days 8–12 | | | | | | | (≈ 30–35%) |
| **Flush 3** | Days 15–20 | | | | | | | (≈ 15–20%) |
| **Flush 4** (optional) | Days 22+ | | | | | | | (rarely economic) |
| **TOTAL** | — | | | | | | | 100% |

### 1.3 KPI formulas (audit correction)

*Version 1.0 calculated "biological efficiency" on wet substrate weight. That figure is a **yield ratio**, not BE. Both are now defined:*

| KPI | Formula | Kenyan target | Global benchmark |
| :--- | :--- | :--- | :--- |
| **Yield per m²** | Total saleable kg ÷ bed area (m²) | **15–25 kg/m²** (break-even ≈ 11 kg/m²; Deliverable-505) | 30–35 kg/m² |
| **Yield per tonne of compost** | Total saleable kg ÷ (wet compost kg ÷ 1,000) | **170–270 kg/t** | 300–350 kg/t |
| **Biological efficiency (BE)** | (Total fresh mushroom kg ÷ compost **dry** weight kg) × 100 | **≈ 50–85%** | ≈ 90–110% |
| **Grade A share** | Grade A kg ÷ total saleable kg × 100 | ≥ 60% | ≥ 75% |
| **Reject rate** | Rejects kg ÷ (saleable + rejects) × 100 | < 5% | < 2% |

**Worked example:** 100 m² room, 9,000 kg wet compost at 32% DM (2,880 kg dry), 1,800 kg harvested →
yield = **18.0 kg/m²** · **200 kg/t** compost · BE = 1,800 ÷ 2,880 × 100 = **62.5%**.

### 1.4 Revenue per crop (KES)

| Grade / channel | kg | Net price (KES/kg) | Revenue (KES) |
| :--- | ---: | ---: | ---: |
| Grade A → supermarkets | | (base 580) | |
| Grade A/B → HoReCa | | (base 620) | |
| Grade B/C → wholesale | | (base 400) | |
| Grade C → processing | | (base 200) | |
| **Total** | | **Blended:** | |
| **OpEx for this crop** (Deliverable-505 §3) | | | |
| **Crop margin** | | | |
| **Cost per kg** = OpEx ÷ saleable kg | | | |

### 1.5 Daily harvest log (one row per picking round)

| Date | Room | Flush | Picker(s) | A (kg) | B (kg) | C (kg) | Reject (kg) | Cold room in (time) | Notes |
| :--- | :--- | :--- | :--- | ---: | ---: | ---: | ---: | :--- | :--- |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

### 1.6 Farm benchmark trend (one row per crop)

| Crop ID | Room | Spawning date | Season | Strain | kg/m² | kg/t | BE % | Grade A % | Cost/kg (KES) | Main issue |
| :--- | :--- | :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| | | | | | | | | | | |

*Plot kg/m² by spawning month for 12+ crops. The seasonal pattern (e.g., dips in crops cropped during the long rains) shows where IPM and climate investment will pay back.*

---

## Part 2: Contamination & Disorder Diagnostic Flowchart

### Step 1 — Where is the problem?

```text
START: What do you see?
│
├── A. Coloured growth on compost or casing (no mushrooms affected yet) ──► go to 2A
├── B. Spots, slime, or deformities ON mushrooms ─────────────────────────► go to 2B
├── C. Insects, larvae, tunnels, or "disappearing" mycelium ──────────────► go to 2C
└── D. Poor/uneven pinning or low yield with NO visible pest or disease ──► go to 2D
```

### Step 2A — Growth on compost or casing

| Observation | Likely cause | Root cause to check | Action |
| :--- | :--- | :--- | :--- |
| **Green** powdery/patchy growth | Green mould (*Trichoderma*) | Phase II conditioning incomplete; spawning hygiene; spawn run > 27 °C; rainy-season spore load | Isolate and remove in sealed bags; damp paper over the spot before moving it; review the SOP-202 log; raise the spawn rate in the rains |
| **Olive-green** in compost | Olive mould (*Chaetomium*) | Phase II too hot / insufficient fresh air (anaerobic) | Correct Phase II aeration and peak temperature |
| **Pink/orange** fluffy growth | *Neurospora* or similar | Spawn contamination; poor hygiene | Check the spawn lot; tighten spawning hygiene |
| **White cobweb** over the casing that greys with age | Cobweb (*Cladobotryum*) | High RH, poor airflow | Cover with damp paper + salt; improve airflow |
| **Cream "brain-like" lumps** in compost | False truffle (*Diehliomyces*) | Compost > 26–27 °C in spawn run or case run | Temperature control; thorough cook-out |
| **Grey/black ink caps** | *Coprinus* | Ammonia in the compost | Release compost only at NH₃ ≤ 5–10 ppm |

### Step 2B — Symptoms on mushrooms

| Observation | Likely cause | Root cause to check | Action |
| :--- | :--- | :--- | :--- |
| **Yellow-brown sunken spots** on caps, sometimes slimy | Bacterial blotch (*Pseudomonas tolaasii*) | Water films on caps > 4 h; condensation; rainy/misty season | Faster drying (air movement, RH 82–88% on harvest days); water after picking; chlorinated water (SOP-402) |
| **Distorted, onion-like** mushrooms; grey spotting | Dry bubble (*Lecanicillium/Verticillium*) | Flies as vector; staff movement; poor cook-out | Salt/cover spots; pick last; fly control; cook-out |
| **Soft, swollen masses with amber droplets**, foul smell | Wet bubble (*Mycogone*) | **Soil casing not pasteurised** | Verify casing pasteurisation at 60–65 °C for 4–6 h; change the soil source |
| **Brown discolouration** after packing | Bruising / temperature abuse | Handling; slow cooling | SOP-403 pick-to-pack; cool within 2–4 h |
| **Long stems, small caps** | High CO₂ / low fresh air | Ventilation; uncorrected CO₂ meter at altitude | Increase fresh air; apply the altitude correction |
| **Scaly/cracked caps** | Low RH, dry air on caps | Dry season; strong direct airflow | Raise RH; redirect airflow |
| **Hollow core / brown pith** | Water stress; watering too heavy late in the flush | Watering pattern | Water between flushes, not at harvest |

### Step 2C — Pest damage

| Observation | Likely cause | Root cause to check | Action |
| :--- | :--- | :--- | :--- |
| **Holes/tunnels in stems**, white larvae with black heads | Sciarid larvae | Screens, doors, compost/casing pasteurisation, trap counts | Exclusion; registered biological/chemical control above threshold (SOP-402 §5) |
| **Mycelium eaten away**, small humpbacked flies running | Phorids | Spawn-run room not sealed | Seal; screens; traps |
| **Orange/white tiny larvae** on stems and gills | Cecid flies | Soil casing; cook-out | Casing pasteurisation; cook-out |
| **Reddish "dust"** on casing; pitted caps | Mites | Poor Phase II; contaminated straw | Phase II temperatures; cook-out; raw-material QC |
| **Sunken casing, mycelium disappearing, sour smell** | Nematodes | Unpasteurised casing; earth floors | Pasteurise; sealed floors; cook-out |
| **Grain spawn carried off; columns of ants** | Ants / siafu | Broken moats; vegetation contact | Moats, sticky barriers, perimeter clearance |

### Step 2D — Physiological / environmental problems

| Observation | Likely cause | Action |
| :--- | :--- | :--- |
| No pins after 10–12 days | CO₂ > 1,500 ppm (corrected); air never ≤ 18 °C; casing dry | SOP-401 troubleshooting |
| Overpinning (dense tiny clusters) | Abrupt shock; wet casing surface | Slower ramp; less surface water |
| Low yield, no disease | Compost quality (C:N/N%, Phase II), low spawn rate, casing pH | Review Deliverable-202 and SOP-202 logs; casing jar test |
| Yield drops sharply in rainy-season crops | Blotch/Trichoderma pressure; slow drying | Seasonal IPM calendar (SOP-402 §6) |
| Yield drops in Jan–Feb crops (passive rooms) | Afternoon overheating in fruiting | SOP-101 seasonal vent schedule; earth tubes; crop scheduling |

### Step 3 — Record the incident

| Date | Room / flush | Symptom (code from Step 2) | Area affected (m² or % of units) | Action taken | Root cause found | Follow-up date | Initials |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | | | |
