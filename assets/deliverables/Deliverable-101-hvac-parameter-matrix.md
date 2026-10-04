# Deliverable Template: HVAC & Environmental Parameter Matrix (Deliverable-101)

* **Template ID:** Deliverable-101
* **Version:** 2.0
* **Purpose:** The master reference for environmental setpoints, alarm thresholds, and control actions across every production stage. It covers industrial climate-controlled rooms (global / Track K2) and passive highland rooms (Kenya Track K1), with Kenyan seasonal overrides and altitude corrections.
* **Linked Documents:** Module 1 · SOP-101 · SOP-202 · SOP-301 · SOP-401 · SOP-403 · KE-00 §1

---

## 1. Master Environmental Control Matrix

| Growth stage | Air temp | Compost/bed temp | RH | CO₂ target (ppm) | Fresh air / air changes | Duration |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase II: Levelling** | — | 48–51 °C | Saturated | N/A (high O₂) | Recirculation, minimal fresh air | 12–24 h |
| **Phase II: Pasteurisation** | — | 58–62 °C (never > 63 °C) | Saturated | N/A | Recirculation + steam | 8–12 h at temp |
| **Phase II: Conditioning** | — | 45–50 °C | Saturated | N/A; NH₃ < 150 ppm milestone → **≤ 5–10 ppm release** | Fresh air for O₂ and NH₃ removal | 3–6 days |
| **Phase II: Cool-down** | — | → 24–26 °C | — | — | High filtered fresh air | 12–24 h |
| **Spawn run (incubation)** | 20–23 °C | 24–25 °C (max 27 °C) | 90–95% | 5,000 – 10,000 | Minimal / intermittent | 14–18 days |
| **Case run** | 22–24 °C | 23–25 °C | 90–95% | 3,000 – 5,000 | Low | 7–10 days |
| **Pinning (induction)** | 16–18 °C | 17–19 °C | 85–90% | < 1,000 | 4 – 6 (high flow) | Ramp 24–48 h; pins in 7–10 days |
| **Fruiting / flushes** | 16–18 °C | 17–19 °C | 85–90% (82–88% on harvest days) | < 1,000 (≤ 1,200 between flushes) | 4 – 6 (high flow) | 3 flushes, ≈ 21–28 days |
| **Cook-out** | — | 65–70 °C | — | — | Closed, steam | 8–12 h |
| **Casing pasteurisation** | — | 60–65 °C | — | — | Steam | 4–6 h |
| **Cold storage** | 2–4 °C | Product core 2–4 °C | ≈ 90% | N/A | Closed refrigeration | ≤ 48 h before dispatch |

---

## 2. Alarm & Intervention Thresholds

| Stage | Parameter | Warning (act) | Critical (escalate to manager) |
| :--- | :--- | :--- | :--- |
| Phase II | Compost temp at pasteurisation | Any probe < 58 °C after 6 h of steaming | Any probe > 63 °C |
| Phase II | Blower status | — | Any stop > 15 min (start backup power) |
| Spawn run | Compost temp | ≥ 26.5 °C or < 22 °C | ≥ 27 °C |
| Spawn run | RH | < 88% | < 85% for > 12 h |
| Case run | Compost temp | > 26 °C | > 27 °C |
| Fruiting | Air temp | < 15 °C or > 19 °C | > 21 °C for > 6 h |
| Fruiting | CO₂ (corrected) | > 1,200 ppm | > 2,000 ppm |
| Fruiting | RH | < 82% or > 93% | Droplets on caps > 4 h |
| Cold room | Air temp | > 5 °C | > 6 °C for > 1 h, or power off > 2 h |

---

## 3. Operating Mode Matrix — Industrial vs Passive

| Stage | Industrial / Track K2 control action | Passive / Track K1 control action |
| :--- | :--- | :--- |
| Spawn run, compost too hot | Lower the air setpoint; raise recirculation; chiller | Night fresh air; open bag tops; space bags; recirculation fan |
| Spawn run, compost too cold | Heating coil | Close vents and doors; thermostatic electric heater |
| Pinning shock | Ramp setpoint 1–2 °C per 12 h; fresh-air damper | Night flush (20:00–07:00); earth tubes; daytime throttling (SOP-401 §4.2) |
| Fruiting, afternoon heat | Chiller/AHU cooling | Throttle vents 11:00–16:00; earth tubes; wet curtains (dry seasons) |
| Fruiting, high RH (rains) | Dehumidifying coil; reheat | Recirculation; ventilate in the warmest, driest hours; no floor wetting |
| Fruiting, low RH (dry season) | Steam/fog humidification | Mist walls and floors; wet floor channels; wet curtains |

---

## 4. Kenyan Seasonal Override Table (Track K1, central highlands)

| Season | Fruiting-room risk | Override |
| :--- | :--- | :--- |
| **Jan – Feb** (hot, dry) | Afternoon air > 19 °C; low RH | Extend the night flush; minimum daytime fresh air; wet curtains; consider not starting a pinning shock in the hottest fortnight |
| **Mar – May** (long rains) | RH > 93%, slow cap drying, blotch | Harvest-day RH target 82–88%; recirculation 24/7; chlorinated watering |
| **Jun – Aug** (cool) | Air < 15 °C at night; spawn run stalls | Throttle night vents; spawn-run heating; insulate doors |
| **Sep – Oct** (warm, dry) | As Jan – Feb | As Jan – Feb |
| **Oct – Dec** (short rains) | As Mar – May | As Mar – May; plan crops to peak mid-Nov to late Dec for holiday demand |

---

## 5. Altitude Correction Factors

| Site | Approx. altitude | Approx. pressure (hPa) | CO₂ meter correction (if not pressure-compensated) | Fan sizing uplift vs sea-level catalogue |
| :--- | :--- | :--- | :--- | :--- |
| Mombasa (reference) | 0–50 m | 1,010 | × 1.00 | 0% |
| Nairobi | 1,700 m | ≈ 830 | × 1.22 | +20% |
| Nyeri / Kiambu | 1,800–1,900 m | ≈ 815 | × 1.24 | +20% |
| Eldoret / Limuru | 2,100–2,250 m | ≈ 790 | × 1.28 | +25% |
| Timau (upper) | 2,500 m | ≈ 760 | × 1.33 | +25–30% |

*Correction: CO₂(true) ≈ reading × 1,013 / P(site). Confirm P(site) with a barometer or a phone barometer app on site.*

---

## 6. Sensor Placement & Calibration Schedule

| Sensor | Placement | Calibration / check | Frequency |
| :--- | :--- | :--- | :--- |
| Compost probes | Centre of compost; top, middle, and bottom tier; same units daily | Ice-water bath (0 °C ± 0.5) and a reference thermometer | **Weekly** |
| Air temperature / RH | Bed height, away from inlets and walls, shaded | Compare against a reference psychrometer; salt test for RH (75%) | Monthly |
| CO₂ | Bed height, centre of room | Fresh outdoor air ≈ 420 ppm (after altitude correction) | **Weekly** |
| NH₃ | Phase II return air / headspace | Detector tubes as reference | Each batch |
| Cold-room thermometer/logger | Middle of the product stack | Ice-water bath | Monthly |
| pH meter | — | Buffers pH 7 and 10 | Each day of use |

---

## 7. Room Configuration Sheet (complete per room)

| Field | Entry |
| :--- | :--- |
| Room ID | |
| Track (K1 passive / K2 semi-industrial / global industrial) | |
| Bed area (m²) / room volume (m³) | |
| Site altitude (m) / pressure (hPa) | |
| Fresh-air fan rating (m³/h at Pa) | |
| Recirculation fan rating (m³/h) | |
| Cooling capacity (kW) / heating capacity (kW) | |
| Earth tubes (number × diameter × length) | |
| Backup power source and capacity | |
| Sensors installed (IDs) | |
| Last calibration date | |
