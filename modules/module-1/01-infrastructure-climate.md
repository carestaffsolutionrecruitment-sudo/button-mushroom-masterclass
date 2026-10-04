# Module 1: Facility Infrastructure & Climate Control Engineering

> **Learning outcomes.** By the end of this module you will be able to (1) choose a production site from climate data, (2) specify a building envelope for either a low-cost passive farm or an industrial climate-controlled farm, (3) size ventilation, cooling, heating, and water systems, and (4) lay out a biosecure facility that complies with Kenyan approvals.
>
> **Linked documents:** SOP-101 · Deliverable-101 · Kenya Regional Reference Annex KE-00 (§1 climate, §3 water, §4 energy, §5 regulation)

---

## 1. Regional Adaptation Frameworks

A commercial button mushroom (*Agaricus bisporus*) facility exists to hold two very different microclimates: a warm, high-CO₂ spawn run, then a cool, fresh-air fruiting regime. How you hold them depends on your climate and capital.

### 1.1 Europe & USA — Industrial benchmark

* **Envelope:** Insulated sandwich panels (80–120 mm PIR/PUR core, aluminium or food-grade coated steel skins) on concrete floors with integral drains. The Netherlands, Ireland, and Poland use multi-tier aluminium **Dutch shelf** rooms; Pennsylvania (USA) still runs many wooden **bed/shelf** farms with room steam pasteurisation.
* **Automation:** Air Handling Units (AHUs) with cooling coils fed by closed-loop chillers, steam or hot-water heating coils, mixing boxes that blend recirculated and fresh air, positive-pressure filtered plenums, and computerised climate controllers (SCADA-type) running every stage.
* **Supply chain model:** Most European growers buy **Phase III (fully spawn-run) compost** from specialised compost companies and only crop it. Room turnover is fast (≈ 5–6 weeks per crop) and yields are 30–35 kg/m².

### 1.2 West Africa — Hot-tropical track

* **Thermal management:** Year-round lowland ambient temperatures of 25–33 °C make passive *A. bisporus* fruiting impossible.
* **Strain selection:** Use warm-weather *Agaricus bitorquis* strains, which spawn-run hotter and fruit at about 24–28 °C, or run fully refrigerated rooms for *A. bisporus*.
* **Infrastructure:** Earth-sheltered root-cellar rooms, double-walled shade houses, roof-thatch drip systems that keep the envelope evaporatively cooled, and night-time ventilation. Highland pockets (e.g., Jos Plateau in Nigeria, Cameroon's western highlands) can use the Kenyan passive model below.

### 1.3 Kenya & East Africa — Highland passive and semi-industrial track

* **The highland advantage:** At 1,900–2,300 m (Limuru, Tigoni, upper Kiambu, Nyeri, Eldoret, Molo) the **mean daily temperature already equals the 16–18 °C fruiting target**. The engineering job is not to create cold; it is to **damp the day–night swing** (often 9 °C → 23 °C) into a stable mean. Thermal mass, roof insulation, and timed ventilation do that for a fraction of chiller cost. See KE-00 §1 for the site table.
* **Two build tracks:**
  * **Track K1 — Passive / low-energy:** Compressed Stabilized Earth Block (CSEB) or machine-cut stone walls, insulated or double-thatched roofs, earth-air tubes, night-flush ventilation, evaporative curtains. CapEx ≈ KES 15,000–22,000 per m² of building.
  * **Track K2 — Semi-industrial:** Locally fabricated PIR/EPS sandwich-panel rooms, ducted inverter split or chiller cooling, controller-managed fresh air, Phase II tunnel. CapEx ≈ KES 45,000–80,000 per m² of building.
* **Altitude corrections:** Air at 2,200 m is about 20% less dense, so fans and coolers must be upsized; NDIR CO₂ meters under-read unless pressure-compensated; water boils at ≈ 93 °C (KE-00 §1.4).
* **Cold-site caveat:** At Timau or upper Molo (> 2,400 m), nights of 3–7 °C in July–August can stall the spawn run. Design those rooms with **heat retention first** (insulation, airtight doors) and a small thermostatic heater.

---

## 2. Site Selection & Layout

### 2.1 Site selection scorecard

| Criterion | Weight | What "good" looks like in Kenya |
| :--- | :--- | :--- |
| Altitude & climate | 25% | 1,900–2,300 m; 12 months of logger data with mean 15–18 °C |
| Water | 20% | Borehole yield ≥ 2 m³/h or piped supply plus ≥ 60 days of storage; water analysis in range (KE-00 §3.4) |
| Market access | 15% | ≤ 90 minutes to buyer DCs (Nairobi, Nakuru, Eldoret, Nyeri); all-weather road (murram that turns impassable in the long rains is a production risk) |
| Raw materials | 15% | ≤ 150 km from straw source; poultry manure supply ≤ 50 km |
| Neighbours & NEMA | 10% | Compost yard ≥ 100–300 m from homes and downwind of them (prevailing winds are mostly easterly in the central highlands — **confirm on site**); no wetland or riparian conflict |
| Power | 10% | 3-phase grid within reach, or a solar-hybrid design |
| Land & security | 5% | Title/lease ≥ 10 years; fenced; flat or gently terraced |

### 2.2 Biosecure "dirty-to-clean" layout

Material moves one way only: **dirty → clean**. People move **clean → dirty** within a day, never back.

```text
 [Raw material store] → [Phase I yard (roofed)] → [Phase II tunnel/chamber] → [Spawning hall]
                                                                                  │
                     [Spent compost exit / SMC pad] ← [Cropping rooms] ← [Spawn-run rooms]
                                                          │
                                                    [Packhouse & cold room] → [Dispatch]
```

* Keep the compost yard **≥ 30 m** from growing rooms and downwind; flies and *Trichoderma* spores travel from compost to crop.
* Separate the spent-compost exit door from the clean filling door.
* Put a changing room, footbath, and handwash station at the clean-zone entry (SOP-402).
* Collect yard leachate and goody water in a lined pit for reuse. **No discharge to watercourses** (a NEMA licence condition).

### 2.3 Building orientation for an equatorial site

Near the equator the sun is close to overhead at noon and rises and sets almost due east and west all year.

* Run the **long axis east–west**. The long walls then face north and south and receive little direct sun; only the short gable walls see low-angle morning and afternoon sun.
* Shade east/west gables with roof overhangs, a veranda, a store room, or a planted windbreak (indigenous trees or *Grevillea*, kept ≥ 5 m from walls).
* **The roof is the dominant heat-gain surface.** Spend insulation money on the roof first (§3.3).

---

## 3. Building Envelope — Kenyan Track K1 (Passive / Low-Energy)

### 3.1 Wall systems

| Wall type | Typical build | Approx. U-value (W/m²K) | Thermal mass & time lag | Kenyan notes |
| :--- | :--- | :--- | :--- | :--- |
| **CSEB, 300 mm** (soil + 5–8% cement, hydraulically pressed, interlocking) | Blocks made on site from subsoil with a manual or motorised press | ≈ 2.0 | High; ≈ 8–10 h lag | Lowest embodied cost; uses on-site murram/subsoil. Needs a damp-proof course, a 600 mm roof overhang, and an external lime-render or water-repellent coat on rainy-side walls. |
| **CSEB, 300 mm + 50 mm external EPS + render** | As above with external insulation | ≈ 0.5 | High mass **inside** the insulation (ideal) | Best passive performance: mass stabilises the interior, insulation blocks the swing. |
| **Machine-cut stone, 200–230 mm** (e.g., quarried volcanic tuff, "6 × 9" or "9 × 9" blocks) | Cement–sand mortar | ≈ 3.0–3.5 | High | Readily available around Nairobi, Kiambu, and Nyeri. Add 40–50 mm internal EPS behind plasterboard **or** a CSEB inner leaf with a cavity. |
| **Timber frame + infill insulation** | Treated cypress/pine studs, 75–100 mm mineral wool, inner PVC/plywood lining, external iron sheet or board | ≈ 0.4–0.5 | Low | Fast and cheap, but no mass, so it needs active control. Use **pressure-treated** timber (termites) and a polythene vapour barrier. |
| **Mud-daub / wattle** | Traditional | ≈ 2.5–3.0 | Medium | Acceptable for antechambers and stores only. It cannot be disinfected or sealed against flies, so **do not use it for grow rooms**. |

**Thermal-mass design rule:** a 300 mm earth wall delays the outdoor peak by ≈ 8–10 h and cuts its amplitude to ≈ 20–30%. A 14 °C outdoor swing (9 °C → 23 °C) becomes a 3–4 °C swing at the inner wall surface, and the stored afternoon heat arrives at night, exactly when you can flush it out with cool night air (SOP-101).

### 3.2 Interior finish — hygiene audit correction

*Audit note: earlier versions recommended bare earth floors and exposed earth walls inside grow rooms. That is withdrawn.* Bare earth harbours nematodes, sciarid larvae, *Trichoderma*, and *Mycogone*, and cannot be disinfected.

* **Floors:** 100 mm concrete slab with a hard trowelled screed sloped **1:100** to a trapped floor drain. Coved floor–wall joints. For floor-wetting humidification, use a shallow screed channel along the wall, not bare earth.
* **Walls:** Cement–lime plaster finished with washable oil-based or epoxy paint, or PVC cladding. It must withstand chlorine and peroxide disinfectants.
* **Earth surfaces** are acceptable on the **outside** of the clean zone (corridors, stores) and for evaporative cooling elements.

### 3.3 Roof systems (highest-impact decision)

| Roof option | Build-up (outside → inside) | Approx. U-value | Notes |
| :--- | :--- | :--- | :--- |
| **Bare iron sheet ("mabati")** | Sheet only | ≈ 6–7 | **Unacceptable** for grow rooms. A dark sheet in equatorial sun reaches a sol-air temperature of 60–70 °C. |
| **Insulated iron sheet + radiant barrier** | Light-coloured/white pre-painted box-profile sheet → **reflective foil sarking with ≥ 25 mm still air gap facing the foil** → ventilated roof void → 100 mm mineral wool or 75 mm EPS on the ceiling → polythene vapour barrier (≈ 250 µm, "1000 gauge") → washable ceiling board/PVC | ≈ 0.3–0.4 | Recommended default. Ventilate the roof void with eaves and ridge vents. |
| **Double-layer grass thatch** | Two independent thatch layers (each ≈ 150–200 mm) with a ventilated gap → **separate sealed inner ceiling** (vapour barrier + washable board) | ≈ 0.25–0.35 | Excellent insulation from local material. Controls: fire break ≥ 10 m from other buildings, fire extinguishers, insect/rodent-proof inner ceiling (thatch harbours insects and debris and must **never** be the grow-room ceiling), re-thatch every 5–8 years. |
| **Sandwich panel roof** (Track K2) | 80–100 mm PIR panel | ≈ 0.2–0.25 | Industrial standard; locally fabricated panels are available. |

**Why the roof matters — worked example.** A 70 m² room ceiling at fruiting temperature (17 °C) under a noon sol-air temperature of 65 °C:

* Bare dark mabati, U ≈ 6.5: Q = 6.5 × 70 × (65–17) ≈ 21.8 kW of heat gain, which no passive system can remove.
* Insulated roof, U ≈ 0.35: Q = 0.35 × 70 × 48 ≈ 1.2 kW, which thermal mass and night ventilation can absorb.

### 3.4 Vapour control, airtightness, and condensation

* Fruiting rooms run at 85–95% RH. Place the **vapour barrier on the warm, humid (inner) side** of insulation, and seal all penetrations.
* Fit doors with rubber gaskets. Airtightness is what lets you hold CO₂ during the spawn run and keep heat in on cold highland nights.
* **Anti-condensation:** Insulated ceilings prevent cold-surface drip. Over shelves, fit sloped polythene or aluminium baffles that shed drips to the aisle. Drips on caps cause bacterial blotch.

### 3.5 Pest-proofing the structure

* **Termites:** pre-construction soil treatment by a licensed applicator, or a physical barrier (graded stone or stainless mesh), plus treated timber.
* **Rodents:** 600 mm concrete apron, sealed service entries, door sweeps.
* **Safari ants (siafu) and other ants:** a water moat or sticky barrier around shelf legs in passive houses, and grease bands on posts.
* **Flies:** every opening screened with **≤ 0.6 mm insect netting** (sciarid and phorid adults are ≈ 2–3 mm). Fine screens cut airflow by 50–70%, so **make the screened area 2–3× the free vent area**.

---

## 4. Passive Climate Systems (Track K1)

### 4.1 Earth–air heat exchanger ("earth tube")

At 1.5–2.0 m depth, soil temperature stays near the **annual mean air temperature** (≈ 15–17 °C at Limuru, ≈ 16–18 °C at Nyeri and Eldoret), which is almost exactly the fruiting target.

* **Design:** 20–30 m of 150–200 mm smooth-bore PVC per tube, buried 1.5–2.0 m deep, laid at a 1–2% fall to a condensate drain at the low end, with an insect-screened and filtered intake hood ≥ 1 m above ground.
* **Output:** ≈ 100–200 m³/h per tube at 16–19 °C outlet temperature (verify on site). Three to five tubes per 100 m² of bed supply the base fresh air for fruiting through an inline fan.
* **Hygiene:** fit a removable inlet filter and clean the tube annually with a pull-through brush or a chlorine flush. Condensate pooling breeds bacteria, so the drain must work.

### 4.2 Night-flush ventilation

Open low intakes and high gable/ridge outlets during the coolest hours (≈ 22:00–07:00, adjusted to your logger data) to purge the heat stored in the walls and the CO₂. Seal up before the morning temperature rise. The **stack effect** (warm air rising out of high vents) drives the flow with no fans when the vertical separation between inlet and outlet is ≥ 2.5 m. Full operating schedule: SOP-101.

### 4.3 Evaporative cooling

* **Hessian/coir curtains or cellulose pads** over intakes, kept wet with a gravity drip line from the elevated tank.
* Effectiveness depends on the **wet-bulb depression**: large in January–February and September–October (dry air, 6–10 °C of cooling possible), small in the rainy seasons (1–3 °C). Plan evaporative cooling for the hot dry seasons and do not rely on it in March–May.
* Hessian grows mould. Rotate two sets weekly, sun-dry, and replace monthly.

### 4.4 Heat retention and supplementary heat (cold highland sites)

* The spawn-run compost generates its own heat. Insulate and close the room, and room air at 20–23 °C keeps the compost at 24–25 °C.
* If night room air drops below ≈ 19 °C and the compost core falls below 22 °C: add a thermostatically controlled oil-filled electric heater (1.5–2 kW per 100 m² of bed is a typical starting point), or hot-water pipes from a solar water heater with a backup element. **Never use open charcoal jikos or paraffin burners.** They produce carbon monoxide (lethal to workers) and ethylene/combustion gases that damage the crop.

---

## 5. Industrial and Semi-Industrial Climate Engineering (Track K2 & Global)

### 5.1 Target operational parameters across cycles

| Stage | Air temp | Compost/bed temp | RH | CO₂ | Fresh air |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Spawn run** | 20–23 °C | 24–25 °C (max 27 °C) | 90–95% | 5,000–10,000 ppm | Minimal, only to stop overheating |
| **Case run** | 22–24 °C | 23–25 °C | 90–95% | 3,000–5,000 ppm | Low |
| **Pinning & fruiting** | 16–18 °C | 17–19 °C | 85–90% | < 1,000 ppm | 4–6 air changes/hour |
| **Cold storage** | 2–4 °C | — | ≈ 90% | — | Closed |

Full matrix with alarm thresholds and Kenyan seasonal overrides: **Deliverable-101**.

### 5.2 Fan and fresh-air sizing (worked example, Limuru altitude)

Room: 10 m × 7 m × 3.5 m = **245 m³**, 100 m² of shelf area.

1. Fruiting fresh-air target at 6 air changes/hour: 245 × 6 = 1,470 m³/h (≈ 14.7 m³/h per m² of bed).
2. Altitude correction (+25% for ≈ 80% air density): 1,470 × 1.25 ≈ 1,840 m³/h.
3. Filter, screen, and duct losses: select a fan rated for **≈ 1,850–2,000 m³/h at 150–250 Pa** static pressure, with a variable-speed controller so the same fan can run at 20–30% during spawn run.
4. Recirculation: add an internal fan moving ≈ 3–5× the room volume per hour through a perforated poly-tube duct along each shelf aisle so the air at the beds is even (no dead pockets of high CO₂).

### 5.3 Cooling load (Track K2, Nairobi peri-urban example)

Sensible load components for a 100 m² bed room during fruiting: envelope gain (≈ 1–2 kW with insulated panels), fresh-air load (1,840 m³/h of 26 °C air cooled to 17 °C at 0.98 kg/m³: ≈ 0.51 kg/s × 1.006 × 9 ≈ 4.6 kW), and crop respiration plus compost heat (≈ 1.5–3 kW in the first flush). **Design ≈ 8–10 kW (≈ 2.5–3 TR) of cooling per 100 m² of bed** for a lowland-edge site, versus ≈ 0–3 kW for a well-built passive room at Limuru. Use inverter split units or a small chiller with a dehumidification-capable coil.

### 5.4 Air distribution, filtration, and pressure

* **Plenums and ducting:** Perforated overhead poly-tube ducts are the low-cost standard (locally made, washable, cheap to replace). They give uniform airflow across all shelf tiers or bag rows.
* **Filtration:** G4 pre-filter plus F7 (or better) fine filter on fresh air during spawning and spawn run, and **positive room pressure** so leaks blow out, not in. HEPA on spawning halls where budget allows.
* **Anti-condensation baffling:** prevents drips onto pins (bacterial blotch).

### 5.5 Instruments (minimum kit per room)

| Instrument | Spec | Indicative cost (KES) |
| :--- | :--- | :--- |
| Compost/bed probe thermometer | Digital, 15–30 cm stainless probe, ±0.5 °C | 2,500–6,000 |
| Min/max air thermometer + hygrometer | Digital, ±3% RH | 1,500–4,000 |
| Data logger (temp/RH) | USB or Bluetooth, 15-min interval | 6,000–15,000 |
| CO₂ meter | NDIR, **pressure-compensated** or with a manual altitude correction | 15,000–45,000 |
| Ammonia detection | Detector tubes or electrochemical NH₃ meter (for Phase II) | 20,000–80,000 |
| pH & EC meter | For casing and water; calibration buffers | 5,000–20,000 |

---

## 6. Water & Power Infrastructure Summary

* **Water:** design for ≈ 3 m³/day average and 10 m³/day peak per 100 m²-bed-per-month throughput; combine rainwater harvesting with a borehole or piped supply; elevated storage for gravity pressure; treat for pH/alkalinity. Full engineering: **KE-00 §3**.
* **Power:** identify critical loads (cold room, Phase II blower, spawn-run recirculation fans, data loggers) and give them backup power (generator with automatic transfer switch, or solar + battery inverter). A Phase II blower failure during the pasteurisation peak can lose a whole batch.

---

## 7. Kenyan Approvals for the Build (summary)

1. County development permission and approved building plans (registered engineer's sign-off for CSEB load-bearing walls).
2. NEMA EIA licence covering the compost yard, Phase II tunnel, borehole, and leachate system, **before** breaking ground.
3. WRA authorisation and abstraction permit for any borehole.
4. DOSHS workplace registration; boiler/pressure-vessel examination for any steam generator.

Detail and timelines: **KE-00 §5**.

---

## 8. Module 1 Checklist

* [ ] 12-month site temperature log reviewed against KE-00 §1 targets
* [ ] Track selected (K1 passive / K2 semi-industrial / global industrial) and justified with a cooling-load estimate
* [ ] Roof U-value ≤ 0.4 W/m²K specified for grow rooms
* [ ] Washable floors and walls with drains in all clean-zone rooms
* [ ] Dirty-to-clean layout drawn and approved
* [ ] Fans sized with the altitude correction; CO₂ meter pressure-compensated
* [ ] Water analysis completed; storage ≥ 60 days if rain-dependent
* [ ] Backup power on critical loads
* [ ] NEMA, WRA, county, and DOSHS approvals filed
