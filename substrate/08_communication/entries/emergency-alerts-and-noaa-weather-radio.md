---
entry_id: emergency-alerts-and-noaa-weather-radio
title: "Emergency Alerts and NOAA Weather Radio"
type: METHOD
domain: substrate/08_communication
region_scope: universal
usda_zone: n/a
confidence: medium
source_tier: T1
sources:
  - title: "Wireless Emergency Alerts (IPAWS)"
    publisher: "FEMA"
    url: "https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public/wireless-emergency-alerts"
    tier: T1
  - title: "Wireless Emergency Alerts (WEA)"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/wrn/wea"
    tier: T1
  - title: "Emergency Alerts"
    publisher: "Ready.gov / FEMA"
    url: "https://www.ready.gov/alerts"
    tier: T1
  - title: "Emergency Alert System"
    publisher: "FEMA"
    url: "https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public/emergency-alert-system"
    tier: T1
  - title: "Emergency Alert System (EAS) description"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/nwr/eas_description"
    tier: T1
  - title: "NOAA Weather Radio All Hazards"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/nwr/"
    tier: T1
  - title: "NWR Receivers"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/nwr/nwr_receivers"
    tier: T1
  - title: "NWR coverage by county"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/nwr/counties"
    tier: T1
  - title: "Using NWR SAME"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/nwr/usingsame"
    tier: T1
  - title: "NOAA Weather Radio (weekly test), Sterling VA office"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/lwx/nwr"
    tier: T1
  - title: "Routine Weekly Test, Wilmington OH office"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/iln/nwr_rwt"
    tier: T1
  - title: "Frequently Asked Questions (watch, warning, advisory), Sterling VA office"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/lwx/FAQ"
    tier: T1
  - title: "Tornado Safety: Watch and Warning"
    publisher: "National Weather Service"
    url: "https://www.weather.gov/safety/tornado-ww"
    tier: T1
  - title: "Build A Kit"
    publisher: "Ready.gov / FEMA"
    url: "https://www.ready.gov/kit"
    tier: T1
  - title: "People with Disabilities"
    publisher: "Ready.gov / FEMA"
    url: "https://www.ready.gov/disability"
    tier: T1
  - title: "Get Tech Ready"
    publisher: "Ready.gov / FEMA"
    url: "https://www.ready.gov/get-tech-ready"
    tier: T1
  - title: "47 CFR 95.305, Authorization to operate Personal Radio Services stations"
    publisher: "FCC / eCFR"
    url: "https://www.ecfr.gov/current/title-47/part-95/section-95.305"
    tier: T1
  - title: "47 CFR Part 95 Subpart B, Family Radio Service (95.503, 95.531, 95.563, 95.567, 95.587, 95.591)"
    publisher: "FCC / eCFR"
    url: "https://www.ecfr.gov/current/title-47/part-95/subpart-B"
    tier: T1
  - title: "47 CFR 95.905, Authority to operate CBRS stations voided by violation of operating rules"
    publisher: "FCC / eCFR"
    url: "https://www.ecfr.gov/current/title-47/part-95/section-95.905"
    tier: T1
  - title: "47 CFR 95.1705, GMRS individual licenses"
    publisher: "FCC / eCFR"
    url: "https://www.ecfr.gov/current/title-47/part-95/section-95.1705"
    tier: T1
  - title: "47 CFR 95.1763 and 95.1767, GMRS channels and transmitting power limits"
    publisher: "FCC / eCFR"
    url: "https://www.ecfr.gov/current/title-47/part-95/subpart-E"
    tier: T1
  - title: "47 CFR 97.5, Station license required"
    publisher: "FCC / eCFR (text via Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/47/97.5"
    tier: T1
  - title: "Getting Licensed"
    publisher: "American Radio Relay League (ARRL)"
    url: "https://www.arrl.org/getting-licensed"
    tier: T2
  - title: "Thunderstorms and Lightning"
    publisher: "Ready.gov / FEMA"
    url: "https://www.ready.gov/thunderstorms-lightning"
    tier: T1
last_reviewed: draft
review_status: draft
method_for: "receive official emergency warnings by phone and by NOAA Weather Radio, and know what watch and warning mean"
materials: 
  - phone with Wireless Emergency Alerts turned on
  - NOAA Weather Radio receiver with SAME, tone alert and battery backup
  - your six-digit SAME county code(s)
  - spare batteries
difficulty: easy
hazard_severity: low
---

# Emergency Alerts and NOAA Weather Radio

> Bracketed numbers point to `## Sources`; "(general practice)" and "(this entry's rule)" mark points no opened source states. The chapter this entry supports is [08_communication.md](../../../08_communication.md#get-warnings-in). Using a radio to talk is in [radio-basics-and-bands](radio-basics-and-bands.md). What to do once a warning arrives is in [08_communication.md](../../../08_communication.md#worked-scenario-a-tornado-warning-phone-networks-jammed) and [04_shelter.md](../../../04_shelter.md).

## Goal & When To Use

A warning only helps if it reaches you. Use at least two sources (this guide's rule, from [08_communication.md](../../../08_communication.md#get-warnings-in)): the alerts on your phone, and a weather radio that works when the power and the cell network do not. This entry covers how each source works, how to set up a weather radio and program your county into it, what "watch" and "warning" mean, and how to test it all.

## Steps

### 1. Set up phone alerts (Wireless Emergency Alerts)

**What they are.** Wireless Emergency Alerts (WEA) are short messages sent to WEA-enabled phones in a targeted area. Senders include state, local, tribal and territorial officials, the National Weather Service (NWS), the National Center for Missing and Exploited Children, and the President [3]. They look like text messages but come with a distinct tone and vibration, repeated twice [1][3]. They are free, and you do not sign up [1][3]. Ready.gov and the NWS both say network congestion does not affect them [2][3]. WEA does not track you. Alerts are broadcast from nearby cell towers to every capable phone in range [1][2]. Someone who enters the threat area after an alert is sent should receive it on arrival [2].

**Alert types.** FEMA lists five: National Alerts (a special class sent only during a national emergency), Imminent Threat Alerts (current or emerging threats such as extreme weather or active shooters), Public Safety Alerts (threats that may not be imminent or have already happened), AMBER Alerts, and opt-in test messages [1].

**What you can turn off.** Phones can opt out of some alerts. The menu is typically in the notification settings [1]. The NWS says you can opt out of WEA messages for imminent threats and AMBER alerts, but not for Presidential messages [2]. This entry's rule: leave imminent-threat alerts on. They carry the warnings that give the least time to act (see the list below). No opened source says to keep them on; this is the safer choice.

**Which NWS warnings trigger a WEA.** Tsunami, tornado, hurricane, typhoon, storm surge, extreme wind, dust storm and snow squall warnings; severe thunderstorm warnings only when the damage threat is "destructive"; flash flood warnings only when the damage threat is "considerable or catastrophic" [2]. A warning not on this list will not reach you as a WEA. That is one reason to own a weather radio (this entry's reading of [2]).

**Check your phone.**
1. Open the notification or alert settings and confirm emergency alerts are on. Some phone models require you to enable WEA, older phones may not support it, and some carriers call the alerts "Government Alerts" or "Emergency Alert Messages" [3]. To find out whether your phone can receive them, ask your wireless provider [1].
2. Know what blocks an alert: weak reception, being on a call (the alert is delayed until the call ends), airplane mode or a powered-off phone, and a VPN [1]. Leave the phone on and out of airplane mode when a warning is possible.
3. If a phone keeps repeating the same alert, powering it off and on may help [1]. Newer phones keep alerts for at least 24 hours or until you delete them [1].
4. The FEMA app can send NWS alerts for up to five locations [3][16]. Also sign up for your community's warning system [24].

### 2. Know the other alert channels

- **Emergency Alert System (EAS).** A national public warning system that interrupts radio and television, and also runs through cable, satellite and wireline operators [3][4]. The President can address the nation through it. Other officials use it for weather, imminent threats and AMBER alerts [3]. The NWS activates it most often, for imminent and dangerous weather, and uses NOAA Weather Radio as its primary means to do so [5]. Whether a station relays a given NWS message is voluntary, except in a national-level activation [5].
- **Local alerts (IPAWS).** FEMA's Integrated Public Alert and Warning System lets local officials send WEA, EAS, weather radio, siren and billboard messages at the same time. FEMA does not review or approve local alerts [3]. If your town has sirens, ask your local emergency management office what the tone means (general practice).

### 3. Get a NOAA Weather Radio

**What it is.** NOAA Weather Radio All Hazards broadcasts NWS warnings, watches, forecasts and other hazard information 24 hours a day. It also carries non-weather hazards such as earthquakes, chemical releases, AMBER alerts and 911 outages [6]. It uses seven frequencies: 162.400, 162.425, 162.450, 162.475, 162.500, 162.525 and 162.550 MHz [6]. A plain AM/FM radio cannot pick it up. You need a receiver or scanner built for it [6][7].

**How far it reaches.** Reliable reception typically extends about a 40-mile radius from the transmitter on level ground. Some counties, especially in mountains, may not have reliable reception because of signal blockages or distance [8]. The NWS county tables show whether your county is covered [8].

**What to look for.** The NWS recommends a receiver with the Public Alert logo or the NWR All Hazards logo, and lists these features [7]:
- **Tone alert.** The NWS sends a 1050 Hz tone before most warnings and many watches. It switches on receivers equipped for it, even if the audio is turned off, which helps at night [7].
- **SAME (Specific Area Message Encoding).** A SAME receiver responds only to alerts for the areas you select, which cuts false alarms from events a few counties away [7].
- **Battery backup.** Power outages often happen during storms [7]. Keep fresh batteries in it. The NWS recommends keeping the receiver on AC power to preserve battery life, with batteries as the backup [7].
- **Optional.** Event blocking (silence alerts for hazards that do not apply to you, such as coastal flooding inland), an external antenna jack, and a jack for external devices such as strobe lights or bed shakers [7].
- **Hearing or vision needs.** Ready.gov suggests a weather radio with a text display and a flashing alert [15].

The NWS does not make or sell receivers and endorses no brand [7]. This entry names none.

**Program your county (SAME).**
1. Find your six-digit SAME code in the NWS county table, by calling 1-888-NWR-SAME (1-888-697-7263) for a voice menu, or by texting the word "Go" to that number. Message rates may apply [9].
2. Understand the code. The first digit is 0 for a whole county and a non-zero number for part of a county. Digits 2 and 3 identify the state and digits 4 to 6 the county [9].
3. Enter the code for each county or area you want alerts for, following the directions in your radio's manual [9]. Add the counties where you spend long hours, such as where you work (general practice).
4. Tune the station that the county table lists for your county. The NWS warns against programming a louder or clearer station that is not designated as a SAME channel for you, because you will not receive alerts [9]. The county table lists the station for your county [8].

Once programmed, a SAME receiver turns on for a SAME-coded message, sounds the 1050 Hz tone, and plays the broadcast [9].

### 4. Battery and hand-crank radios

Ready.gov lists both a battery-powered or hand-crank radio and a NOAA Weather Radio with tone alert for the home kit [14]. They are not the same thing. A hand-crank radio carries local news only if it also receives the weather band, and an ordinary AM/FM radio does not [6][7]. Before you count a crank radio as your weather radio, check its label or manual for the NOAA or weather band, and for SAME if you want county alerts (general practice). If you use a radio to charge a phone, check the manual first (general practice). Include the radio when you check your kit (see [11_essential_gear.md](../../../11_essential_gear.md#keeping-it-working)).

### 5. Watch and warning

The NWS uses the same pattern for most hazards [12]:
- **Watch:** there is potential for a certain type of weather.
- **Warning:** life-threatening weather is expected.
- **Advisory:** like a warning, but not as severe.

For tornadoes, the NWS says a watch means tornadoes are possible in and near the watch area. Watches come from the Storm Prediction Center and often cover many counties. A warning means a tornado has been sighted or indicated by weather radar, and it covers a much smaller area [13]. On a watch, prepare: review your plan, check your supplies and safe room, and be ready to act fast. On a warning, act now: move to an interior room on the lowest floor of a sturdy building, away from windows. In a mobile home, vehicle or outdoors, move to the closest substantial shelter [13].

### 6. Test it

- **Weekly NWR test.** NWS offices normally test the tone-alert and SAME system on Wednesday between 11 a.m. and noon. The test is postponed or canceled when hazardous weather is present or expected [10][11]. Check your local NWS office for its schedule. Use the test to confirm that your radio sounds [10][11].
- **If the radio stays silent.** Missing one test could be the NWS side. Missing several is more likely your radio. Move it to another spot, check the programming [11], look for nearby interference, and try a stronger or outside antenna. Some older analog radios drift off their frequency over time [10].
- **Phone.** National-level tests are run by FEMA and the FCC, and local officials may send opt-in test messages [1][3]. Check settings yourself; no source sets a phone test schedule.

### 7. If you also want a radio that transmits

A weather radio only listens. Transmitting rules differ by service. Under 47 CFR 95.305, the FCC does not require an individual license for a Personal Radio Service station unless the rules for that service say so [17]. The FRS rules contain no license requirement [18], and the CB rules (which call the service CBRS) treat its stations as operating without an individual license under 95.305 [19]. GMRS requires an individual license [20]. **An older radio sold as "FRS/GMRS" needs a GMRS license if you use it on channels or at power levels that only GMRS allows** (new combination radios may not be sold since Sept 30, 2019, 47 CFR 95.591 [18]). The 22 FRS channels are shared with GMRS, and FRS power is capped at 2 W on channels 1 to 7 and 15 to 22 and 0.5 W on 8 to 14 [18]. GMRS has other channels and higher power limits [21]. Anything beyond the FRS channels and limits is a GMRS station (this entry's reading of [18][20][21]). Read the radio's label and manual. Amateur ("ham") radio requires a license, and the entry-level Technician license takes a 35-question exam [22][23]. Details and limits are in [radio-basics-and-bands](radio-basics-and-bands.md) and [08_communication.md](../../../08_communication.md#radios-what-each-service-allows).

## Failure Modes & Fixes

- **Phone in airplane mode or off during a storm.** No WEA arrives [1]. Turn it on.
- **Imminent-threat alerts switched off.** You lose tornado and flash flood warnings. Turn them back on (this entry's rule).
- **A warning not on the WEA list.** No phone alert comes [2]. A weather radio covers it.
- **Radio with no battery backup.** It dies with the power [7]. Add batteries or use a unit with backup.
- **Radio not programmed, or programmed for the wrong county.** It alarms for the wrong area or not at all. Re-enter the code and check the weekly test [9][10].
- **Radio without SAME.** It sounds for everything on the transmitter, so people unplug it [7]. Choose SAME.
- **Out of coverage.** Mountains and distance can block the signal. Check the county table [8].
- **One source only.** Phones fail and power fails. Keep both.
- **Unverified forwards.** Confirm an alert you did not get from an official source before you evacuate or spend money (this guide's rule, from [08_communication.md](../../../08_communication.md#rumors-and-bad-information)).

## Sources

All pages opened 2026-10-21. Where a site blocked automated fetches, the note below says how it was read.

1. Wireless Emergency Alerts (IPAWS). FEMA. https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public/wireless-emergency-alerts
2. Wireless Emergency Alerts (WEA). National Weather Service. https://www.weather.gov/wrn/wea
3. Emergency Alerts. Ready.gov / FEMA. https://www.ready.gov/alerts
4. Emergency Alert System. FEMA. https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public/emergency-alert-system
5. Emergency Alert System (EAS) description. National Weather Service. https://www.weather.gov/nwr/eas_description
6. NOAA Weather Radio All Hazards. National Weather Service. https://www.weather.gov/nwr/
7. NWR Receivers. National Weather Service. https://www.weather.gov/nwr/nwr_receivers
8. NWR coverage by county. National Weather Service. https://www.weather.gov/nwr/counties
9. Using NWR SAME. National Weather Service. https://www.weather.gov/nwr/usingsame
10. NOAA Weather Radio (weekly test), Sterling VA office. National Weather Service. https://www.weather.gov/lwx/nwr
11. Routine Weekly Test, Wilmington OH office. National Weather Service. https://www.weather.gov/iln/nwr_rwt
12. Frequently Asked Questions (watch, warning, advisory), Sterling VA office. National Weather Service. https://www.weather.gov/lwx/FAQ
13. Tornado Safety: Watch and Warning. National Weather Service. https://www.weather.gov/safety/tornado-ww
14. Build A Kit. Ready.gov / FEMA. https://www.ready.gov/kit
15. People with Disabilities. Ready.gov / FEMA. https://www.ready.gov/disability
16. Get Tech Ready. Ready.gov / FEMA. https://www.ready.gov/get-tech-ready
17. 47 CFR 95.305, Authorization to operate Personal Radio Services stations. FCC / eCFR. https://www.ecfr.gov/current/title-47/part-95/section-95.305
18. 47 CFR Part 95 Subpart B, Family Radio Service (95.503, 95.531, 95.563, 95.567, 95.587, 95.591). FCC / eCFR. https://www.ecfr.gov/current/title-47/part-95/subpart-B
19. 47 CFR 95.905, Authority to operate CBRS stations voided by violation of operating rules. FCC / eCFR. https://www.ecfr.gov/current/title-47/part-95/section-95.905
20. 47 CFR 95.1705, GMRS individual licenses. FCC / eCFR. https://www.ecfr.gov/current/title-47/part-95/section-95.1705
21. 47 CFR 95.1763 and 95.1767, GMRS channels and transmitting power limits. FCC / eCFR. https://www.ecfr.gov/current/title-47/part-95/subpart-E
22. 47 CFR 97.5, Station license required. FCC / eCFR (text via Cornell LII). https://www.law.cornell.edu/cfr/text/47/97.5
23. Getting Licensed. American Radio Relay League (ARRL). https://www.arrl.org/getting-licensed
24. Thunderstorms and Lightning. Ready.gov / FEMA. https://www.ready.gov/thunderstorms-lightning

Not sourced, so not stated: receiver prices or brands, a phone test schedule for WEA, what a siren tone means in your town (ask local officials), and FRS, CB or GMRS details beyond the rule text in sources 17 to 21 (the FCC's own FRS, CB and GMRS web pages blocked fetches and are not cited here; see radio-basics-and-bands).
