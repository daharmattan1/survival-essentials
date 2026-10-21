---
entry_id:              mesh-and-emergency-comms
title:                 Mesh and Emergency Comms
type:                  METHOD
domain:                substrate/08_communication
region_scope:          universal
usda_zone:             n/a
confidence:            medium
source_tier:           T1
sources:
  - title: "Family Communication Plan (Ready Campaign brochure; copy hosted by NJ Office of Emergency Management)"
    publisher: "FEMA / Ready.gov"
    url: "https://www.nj.gov/njoem/plan-prepare/pdf/FEMA_family_communication_plan.pdf"
    tier: T1
  - title: "Make a Plan"
    publisher: "FEMA / Ready.gov"
    url: "https://www.ready.gov/plan"
    tier: T1
  - title: "Emergency Communications Tips (FCC/FEMA)"
    publisher: "Federal Communications Commission (opened via Internet Archive snapshot of 2026-10-15)"
    url: "https://www.fcc.gov/emergency"
    tier: T1
  - title: "Meshtastic overview (community project documentation, not a government source)"
    publisher: "Meshtastic project"
    url: "https://meshtastic.org/docs/overview/"
    tier: T3
last_reviewed: draft
sources_checked: 2026-10-21
review_status: agent-verified
method_for:           "keep a family or small group in touch by text when cell networks are jammed or down, and plan how the family reconnects"
materials:
  - paper family communication plan (out-of-area contact, meeting places, phone numbers)
  - charged phones, spare batteries, solar or car charger
  - optional - a small off-grid mesh radio for each person in the group, tested together beforehand
difficulty:           moderate
---

## Goal & When To Use

The core of emergency communication is a **family plan** that works with ordinary phones. A mesh radio is an optional extra for a group that is close together. Read the plan part first.

A mesh radio is a small device that passes short text messages from node to node by radio, with no cell tower or internet. The Meshtastic documentation calls the mesh "the set of nodes that relay each other's messages" and says it works without internet or cellular service [4].

**A mesh network cannot reach 911.** It has no connection to a 911 call center or the phone network (this guide's judgment, from [4]). If someone is hurt or in danger, use a phone to call 911 (see `08_communication.md`), or leave the area to find coverage.

Use mesh only when:
- Phones are jammed or down, **and**
- everyone you want to reach carries a compatible, charged mesh node, **and**
- you tested the group together before the emergency.

No government source gives a dependable range, battery life or price for mesh devices, so this entry gives none. Treat a mesh as a short-range extra that may or may not work on the day (this guide's judgment).

---

## Steps

### 1. Make the family plan (before anything happens) [1][2][3]

1. **Pick one out-of-town (out-of-state) contact,** and have every family member contact the same person. It might be easier to reach someone who is out of town [1].
2. **Choose two meeting places:** one in your neighborhood and one in your town or region [1]. Ready.gov asks for a meeting place that is familiar and easy to find [2].
3. **Write it down.** Fill in the contact, meeting places, medical and insurance information. Keep a copy in your purse or briefcase, your car, your office and your disaster kit. Look it over every year and keep it up to date [1].
4. **Make sure everyone can text,** including the out-of-town contact [3].
5. **Put an "In Case of Emergency" contact in every phone,** and write down phone numbers for emergency services, utilities, medical providers and insurance [3].

### 2. Use the phone network the right way in an emergency [1][3]

- **Text, do not talk,** unless you are in danger; if you are, call 911 first. Texts may get through when calls do not, and you do not tie up lines emergency workers need [1][3]. Texts to other wireless devices may be delayed during congestion [3].
- Keep calls short and limit non-emergency calls [3].
- Send one short message to your out-of-town contact, for example "I'm OK. At the library." (general practice). They pass word to the rest of the family [1].
- Call 911 only for emergencies [3].

### 3. If you add mesh radios (optional)

**Set up and test beforehand.**
- Give a node to each person in the group, and keep spare batteries or a charger. Keep a solar or car charger on hand for phones and other devices [3].
- All nodes must share the same channel name and key to read each other's messages. Radio settings (frequency, bandwidth, spreading factor) must also match [4]. Write the settings on your plan card.
- Test the group on a normal day: send a message from one end of your usual area to the other, in the places you would really be (this guide's judgment). Note where it fails.
- Agree on a short check-in schedule for the test, so a dead node is noticed early (this guide's judgment).

**In an emergency.**
1. Power the nodes on. A mesh needs other nodes within reach of each other. Other nodes in range may relay your message even if they cannot read it [4].
2. Send short text messages: who you are, where you are, what you need. Keep them brief (general practice).
3. Check for replies at set times instead of constantly, to save the battery (general practice).
4. **When any cell or internet service comes back, even briefly, send one text to your out-of-town contact.** Do not call. Wait about 10 seconds before redialing if you must call [3].

---

## Failure Modes & Fixes

**Nodes do not see each other.** A different channel name, key or radio setting [4]; a node switched off or dead; or the nodes are too far apart or blocked by terrain or buildings (general practice). Check the settings against your plan card, then move closer and try again.

**Messages are slow or never arrive.** Not enough nodes between sender and receiver (general practice). Move to higher or more open ground, or place a group member between you.

**The phone app will not connect to the node.** Restart the phone and the node, and pair them again (general practice).

**Dead batteries.** Carry spare batteries or a charger. Dim the phone screen and turn off apps you do not need [3].

**Out-of-town contact number forgotten.** It is on the paper plan in your kit and wallet [1]. Write it down now.

**Nobody answers, and you are worried.** A mesh failing is common and tells you little. Do not assume the worst, and do not tie up phone lines. Text your out-of-town contact when service returns [3]. This guide does not set a fixed time after which anyone should alert authorities. If you believe someone is in danger, call 911 (this guide's judgment).

**Mesh does not work at all.** You have the phone plan, the paper plan, the meeting places, and any FRS or CB radios (see `radio-basics-and-bands.md`).

---

## Sources

All pages opened 2026-10-21.

1. Family Communication Plan (Ready Campaign brochure). FEMA / Ready.gov; copy hosted by NJ Office of Emergency Management. https://www.nj.gov/njoem/plan-prepare/pdf/FEMA_family_communication_plan.pdf
2. Make a Plan. FEMA / Ready.gov. https://www.ready.gov/plan (meeting place and reconnect wording only; it does not cover the out-of-town contact)
3. Emergency Communications Tips (FCC/FEMA). FCC (Internet Archive snapshot 2026-10-15). https://www.fcc.gov/emergency
4. Meshtastic overview (community project documentation, not a government source). https://meshtastic.org/docs/overview/

Not sourced, so not stated: device prices, battery life, range, mesh formation time, license-free band claims, any brand-specific feature, any "notify authorities after 48 hours" rule.
