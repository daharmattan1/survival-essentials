---
entry_id:              radio-basics-and-bands
title:                 Radio Basics and Bands
type:                  METHOD
domain:                substrate/08_communication
region_scope:          universal
usda_zone:             n/a
confidence:            high
source_tier:           T1
sources:
  - title: "FCC Part 95: Personal Radio Services"
    publisher: "Federal Communications Commission"
    url: "https://www.fcc.gov/wireless-telecommunications/personal-radio-services"
    tier: T1
  - title: "National Weather Service Radio (NOAA Weather Radio)"
    publisher: "NOAA / National Weather Service"
    url: "https://www.weather.gov/nwr/"
    tier: T1
  - title: "Amateur Radio (Ham) Licensing and Frequencies"
    publisher: "FCC and ARRL"
    url: "https://www.fcc.gov/wireless-telecommunications/amateur-radio"
    tier: T1
  - title: "Citizens Band Radio Regulations"
    publisher: "FCC Part 95, Subpart D"
    url: "https://www.fcc.gov"
    tier: T1
last_reviewed:        draft
review_status:        draft
method_for:           "receive emergency information and transmit in emergencies using radio bands"
materials:
  - battery-powered or hand-crank AM/FM/NOAA receiver
  - FRS/GMRS transceiver (handheld two-way radio)
  - amateur (ham) radio transceiver (if licensed)
  - CB radio (license-free but regulated)
  - spare batteries
  - reference card listing emergency frequencies
difficulty:           easy
---

## Goal & When To Use

Radio is the only communication tool that works when cell and internet are down. The goal is to **receive weather alerts and emergency broadcasts** (receive-only, no license needed) and **transmit in emergency or critical situations** (normally requires a license). Use radio when:

- **Infrastructure is down** (cell towers destroyed, internet out, phone network congested).
- **You need to stay informed** (NOAA weather radio gives alerts; AM/FM broadcast carries emergency information).
- **You need to request help** (FRS/GMRS in range, ham radio over longer distance, CB as fallback).

**Key rule**: receiving information from radio stations requires no license. Transmitting on most bands requires a license. **Emergency exception**: most jurisdictions permit unlicensed emergency transmissions when life safety is at stake, but you must transmit truthfully and cease when the emergency ends.

---

## Steps

### Receive-Only (No License Required)

**1. NOAA Weather Radio**
- Frequency: 162.400–162.550 MHz (seven NOAA channels; varies by region).
- Equipment: battery-powered or hand-crank weather radio (~$20–50, available before emergency).
- Information: continuous weather alerts, tornado/flood warnings, and emergency broadcast messages.
- Activation: most weather radios have an "alert" mode that activates the radio automatically when a watch/warning is issued.
- **Get one before the emergency.** A weather radio with alert mode is the single cheapest insurance against undetected fast-moving threats (tornadoes, flash floods).

**2. AM/FM Broadcast Radio**
- Frequency: AM 540–1700 kHz, FM 88–108 MHz.
- Information: news, emergency broadcasts, shelter information, evacuation routes.
- Reach: commercial stations broadcast from towers; if towers are up, you receive news.
- Equipment: simple hand-crank or battery-powered AM/FM radio.
- Range: 50–200 miles depending on tower height and terrain; long-wave AM penetrates buildings better than FM.

**3. Shortwave Radio (long-range receive)**
- Frequency: 3–30 MHz bands (requires a dedicated shortwave receiver).
- Information: distant broadcasts, international news, amateur repeater nets (if you monitor).
- Equipment: dedicated shortwave receiver or ham radio in receive mode.
- Use: monitoring international broadcasts or amateur emergency nets if you have a receiver.

---

### Transmit (Licensed or Emergency-Only)

**1. FRS (Family Radio Service) — No License, Low Power**
- Frequency: 14 channels on 462–467 MHz (UHF).
- License: **None required** (FCC regulation change 2017).
- Power: 2 watts maximum (very short range).
- Range: 1–2 miles in open terrain; 1/2 mile in forest/urban (line-of-sight only).
- Use: local team coordination, staying in contact with companions during dispersal.
- Equipment: FRS-only or FRS/GMRS combo handheld (important: verify it is FRS-only or GMRS-licensed model).

**2. GMRS (General Mobile Radio Service) — License Required (normally)**
- Frequency: 8 channels + FRS channels; transmit on 462–467 MHz (overlaps FRS).
- License: normally requires an **FCC license** (~$85 for 10 years; application online).
- Power: 5 watts (repeater access allowed; can reach 10+ miles via repeater).
- Range: 5–10 miles line-of-sight (handheld); farther if using a repeater.
- Use: family coordination, emergency relay, longer-distance team comms.
- **Emergency exception**: many jurisdictions recognize GMRS emergency use without a license if life safety is at stake.
- Equipment: GMRS-capable transceiver (must have GMRS license or emergency-authorization before transmitting).

**3. MURS (Multi-Use Radio Service) — No License**
- Frequency: 5 channels at 151–154 MHz (VHF, better range than FRS).
- License: **None required**.
- Power: 2 watts.
- Range: 2–5 miles line-of-sight (better than FRS due to lower frequency).
- Use: local coordination, less congested than FRS in urban areas.
- Equipment: MURS-capable transceiver (less common than FRS/GMRS).

**4. CB Radio (Citizens Band) — License-Free but Regulated**
- Frequency: 40 channels at 27 MHz (AM or SSB).
- License: **None required** for emergency use; normally a violation to transmit without authorization, but emergency exception applies.
- Power: regulated (~4 watts AM, 12 watts SSB).
- Range: 1–10+ miles depending on propagation and antenna (CB can skip long distances at night).
- Use: distress calling on Channel 9 or Channel 19 (trucker network); longer-distance emergency relay.
- Equipment: CB radio (car-mounted or portable handheld).
- Note: CB channels are often congested; Channel 9 is monitored as emergency.

**5. Amateur (Ham) Radio — License Required (normally)**
- Frequency: multiple bands (2-meter, 70-cm, and longer-wave bands; 146–148 MHz for 2-meter).
- License: **FCC license required** (Technician class minimum, covers 2-meter UHF + some HF).
- Power: varies (typically 5–100 watts depending on equipment and band).
- Range: 10–50+ miles line-of-sight with handheld; much farther via repeater or skywave on HF (long-distance).
- Use: emergency coordination nets, long-distance relay, most reliable comms for regional disaster.
- **Emergency exception**: most jurisdictions permit unlicensed emergency transmissions on ham frequencies if life safety is at stake.
- Equipment: ham radio transceiver (more expensive; ~$100–1000+ for capable units).
- Network: amateur repeater nets often activate during regional disasters and maintain a "net" of available operators.

---

## Failure Modes & Fixes

**Radio won't power on.** Batteries dead. **Solution**: keep spare batteries in your kit or use a hand-crank radio (works even dead). Test batteries monthly.

**Can't reach anyone on FRS/GMRS.** Out of range (farther than 1–5 miles, or line-of-sight blocked). **Solution**: move to higher ground, use a repeater (GMRS), or switch to a longer-range band (MURS, CB, or ham if licensed). If close to a town, try CB Channel 9 or local emergency frequency (research before the emergency).

**Receive stations aren't broadcasting.** Towers down or power out. **Solution**: switch to battery/hand-crank radio and monitor multiple stations (AM/FM, shortwave if available). Long-wave AM often survives local power outages. If regional blackout, shortwave international broadcasts are your best bet for information.

**Forgot emergency frequencies.** **Solution**: print or write down emergency frequencies *before* the emergency. Key frequencies:
  - NOAA Weather Radio (seven channels; find your region at weather.gov/nwr).
  - CB Channel 9 (emergency).
  - Local police/fire non-emergency (listed in phone book or county emergency plan).
  - 2-meter ham repeater (if you hold a license; look up via RepeaterBook app).

**Can't transmit legally because unlicensed.** Use FRS only (no license), or trigger emergency exception if life safety is at stake (transmit briefly and truthfully; cease after emergency ends). Don't rely on a legal gray area; get licensed (GMRS, ham) before the emergency if you plan to transmit.

**Battery dead and no charging.** Use hand-crank radio for receive-only. Preserve battery power: receive only when expecting alerts or news, not continuously. Dim the display if possible.

---

## Sources

- **FCC Part 95: Personal Radio Services.** The authoritative regulatory source for FRS, GMRS, MURS, and CB. Defines power limits, channels, licensing requirements, and emergency exceptions.
- **NOAA National Weather Service Radio (NWR).** Official source for weather radio channels, alert protocols, and emergency broadcast procedures; includes regional frequency finder.
- **FCC Part 97: Amateur Radio Service.** Defines ham radio licensing, bands, power limits, repeater coordination, and emergency use. Coordinated through ARRL (American Radio Relay League).
- **RepeaterBook** (app / online). Crowdsourced directory of FRS/GMRS/MURS/ham repeaters by region; invaluable for knowing local relay frequencies before emergency.
