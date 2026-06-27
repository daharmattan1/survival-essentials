---
entry_id:              mesh-and-emergency-comms
title:                 Mesh and Emergency Comms
type:                  METHOD
domain:                substrate/08_communication
region_scope:          universal
usda_zone:             n/a
confidence:            medium
source_tier:           T3
sources:
  - title: "Meshtastic Documentation"
    publisher: "Meshtastic project (open-source community)"
    url: "https://meshtastic.org"
    tier: T3
  - title: "goTenna User Guide"
    publisher: "goTenna Inc."
    url: "https://www.gotenna.com"
    tier: T3
  - title: "LoRa Technology Overview"
    publisher: "LoRa Alliance"
    url: "https://www.loraalliance.org"
    tier: T3
  - title: "Mesh Networking for Emergency Communications"
    publisher: "Practitioner consensus / DIY comms community"
    url: null
    tier: T3
last_reviewed:        draft
review_status:        draft
method_for:           "establish off-grid, local communication when cell networks are unavailable"
materials:
  - Meshtastic radio device (open-source LoRa, ~$50–150)
  - goTenna Mesh (proprietary, ~$100–200 for pair)
  - or amateur LoRa setup (experimental, requires amateur license)
  - smartphone or device running Meshtastic/goTenna app
  - USB charging cable or hand-crank charger
  - mesh network pre-tested with neighbors/team before emergency
difficulty:           moderate
---

## Goal & When To Use

Mesh radios create a local, off-grid communication network **without cell towers or internet**. Unlike a traditional radio that broadcasts to repeaters, a mesh radio relays messages peer-to-peer, with each device re-broadcasting to extend range and redundancy. Use mesh comms when:

- **Cell towers are down or congested** (disaster aftermath, regional power loss).
- **Your team is dispersed** over 1–5 miles (too far for FRS, but local enough for mesh).
- **You need persistent, low-latency messaging** (not just voice; text is often available).
- **You want to stay off traditional licensed frequencies** (mesh operates in license-free ISM bands like 2.4 GHz, LoRa sub-GHz).

**Limitations**: mesh is slower than cell (message latency of minutes in poor topology), has lower range per device than ham radio (1–3 miles typical, up to 10+ miles if conditions align), and depends on a pre-established network of mesh devices in your area. **Pre-arrange before the emergency**: identify 3+ neighbors or team members willing to carry mesh radios; test the network; agree on check-in protocols.

---

## Steps

### Pre-Emergency Setup

**1. Inventory Mesh Devices**
- **Meshtastic**: open-source LoRa radio boards (Heltec, Lilygo, RAK, ~$50–150 each). Runs on AA batteries or USB. Pairs with a smartphone app (iOS/Android, free). Relies on mesh—each device passes messages onward.
- **goTenna Mesh**: proprietary LoRa radio (~$100–200 per unit), app-based, proprietary mesh. No smartphone pairing model; a pair of goTenna Mesh units communicate directly (not dependent on a larger network).
- **DIY amateur LoRa**: requires an amateur (ham) license; uses open LoRa bands; can inter-operate with Meshtastic but adds legal and technical complexity.

**2. Test Network Coverage**
- Distribute mesh devices to 3+ team members or neighborhood contacts.
- Test connectivity over 1–3 miles in typical terrain (through trees, over hills, in urban canyons).
- Note dead zones: areas where the mesh degrades or fails.
- Establish a "mesh check-in" protocol (once daily, same time, simple message) so failures are obvious pre-emergency.

**3. Agree on an Out-of-Area Contact**
- Designate one person outside your local area (different city, different state, different country if possible).
- This person receives status updates via traditional means (phone calls during cell recovery, email if internet returns, or direct message later).
- The rule: your local mesh team updates the out-of-area contact at a set time (daily, if possible) with one sentence: "All safe, supplies holding" or "Need urgent help, person injured."
- The out-of-area contact notifies authorities or family if no update arrives in 48 hours.

**4. Charge Devices Before Emergency**
- Meshtastic devices: run on 2–4 AA batteries (12–48 hour life depending on message frequency) or USB power bank.
- goTenna Mesh: rechargeable internal battery (12–48 hour life).
- Pre-charge all devices and power banks; keep spares.
- Hand-crank chargers (solar or mechanical) extend battery life in prolonged outages.

### Emergency Use

**1. Activate Mesh Network**
- Power on all team mesh devices; they automatically form a mesh on the same channel.
- Meshtastic nodes appear as participants in the app; goTenna devices appear as contacts.
- Initial mesh formation takes 5–30 minutes (nodes discover each other and establish links).

**2. Send Status Message**
- Compose a brief text message (mesh bandwidth is low; keep to 1–2 sentences).
- Example: "Safe at home. Water supplies good. No injuries. Standing by."
- Send to the "mesh" channel (everyone receives it) or to a specific person.
- Message propagates through relays; delivery may take minutes in a sparse mesh.

**3. Receive Information**
- Team members share updates (supplies, hazard warnings, movement plans).
- Messages stay in the app's chat history; review for coordination.
- Avoid congestion: check for updates every 2–4 hours, not continuously.

**4. Update Out-of-Area Contact**
- If cellular or internet becomes available (even briefly), send a single summary message to your out-of-area contact.
- Example: "Team of 4 at 123 Main St. All safe. No urgent needs. Will update in 12 hours if comms available."
- If networks remain down, the out-of-area contact waits 48 hours, then notifies authorities.

---

## Failure Modes & Fixes

**Mesh won't form (nodes not finding each other).** Likely causes: devices on different channels, out of range, or power off. **Solution**: verify all devices are on the same channel and frequency; bring one device closer as a test; ensure batteries are charged; check manufacturer documentation for default settings.

**Messages delayed 10+ minutes or not arriving.** Sparse mesh topology (not enough relays) or terrain blocking signals. **Solution**: move to higher ground or an elevated location; ask a team member to position themselves halfway between sender and receiver to act as relay; reduce message frequency to avoid congestion.

**Battery depleted rapidly.** High message frequency drains batteries faster. **Solution**: limit messages to 1–2 per hour per device; turn off devices during quiet periods (sleep, shelter); use AA-battery Meshtastic devices for easy swaps.

**Meshtastic app crashes or won't connect to radio.** Bluetooth or USB connection issue. **Solution**: restart phone and radio; forget/re-pair the Bluetooth device in phone settings; check USB cable; try a different USB port.

**Forgot out-of-area contact number/email.** **Solution**: write it down now (before emergency) on paper in your kit. Memorize it or store in an offline contact list.

**Out-of-area contact hasn't heard from you in 48 hours.** They may notify authorities (which is the plan—it triggers help). **Solution**: make best effort to re-establish contact once any internet/phone becomes available. A delayed update is still valuable.

**Mesh device lost or damaged.** It's a backup redundancy tool, not primary. **Solution**: team members with devices continue relaying; fall back to FRS/GMRS radios if available; use the out-of-area contact plan (someone reaches them via traditional means once networks recover).

---

## Sources

- **Meshtastic Documentation.** Open-source LoRa mesh radio project; covers hardware setup, app configuration, and range testing. Maintained by a volunteer community; start at https://meshtastic.org.
- **goTenna Mesh User Guide.** Proprietary LoRa mesh; official setup and troubleshooting.
- **LoRa Alliance Technology Overview.** Background on LoRa (long-range, low-power radio technology) and ecosystem.
- **Practitioner Consensus / DIY Emergency Comms Community.** Mesh radios are relatively new for civilian emergencies; recommendations come from people actively testing them in field conditions (forums, Reddit r/Meshtastic, emergency comms communities). T3 source—useful for field knowledge but not regulatory or medical authority.
