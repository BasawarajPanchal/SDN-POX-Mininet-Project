# SDN Learning Switch with Firewall using POX & Mininet

## Objective

The objective of this project is to design and implement a Software Defined Networking (SDN) solution using Mininet and a POX controller.
The project demonstrates:

* Controller–Switch interaction
* Flow rule (match–action) installation
* Network traffic control using SDN

---

##  Tools & Technologies Used

* **Mininet** – Network emulator
* **POX Controller** – SDN controller
* **OpenFlow (v1.0)** – Communication protocol
* **iperf** – Performance testing tool
* **Ubuntu Linux**

---

##  Network Topology

* Single switch topology
* 3 hosts:

  * h1 → 10.0.0.1
  * h2 → 10.0.0.2
  * h3 → 10.0.0.3
* 1 OpenFlow switch (s1)

---

## Features Implemented

* Learning Switch (MAC address learning)
* Dynamic Flow Rule Installation
* PacketIn handling in controller
* Firewall functionality:

  * Blocks traffic from **h1 → h2**
* Performance analysis using iperf

---

## Steps to Execute

### 1. Start POX Controller

```bash
cd ~/pox
python3.8 pox.py log.level --DEBUG forwarding.my_switch
```

---

### 2. Start Mininet Topology

```bash
sudo mn --topo single,3 --mac --switch ovsk,protocols=OpenFlow10 --controller remote,ip=127.0.0.1,port=6633
```

---

### 3. Run Test Cases

#### ✔ Normal Communication

```bash
h1 ping h3
```

#### Blocked Communication (Firewall)

```bash
h1 ping h2
```

#### Mixed Scenario

```bash
pingall
```

#### 📊 Flow Table Inspection

```bash
sh ovs-ofctl dump-flows s1
```

#### Performance Testing

```bash
h3 iperf -s &
h1 iperf -c 10.0.0.3
```

---

## Results & Observations

* Successful communication between allowed hosts (h1 ↔ h3)
* Traffic from h1 → h2 is blocked by controller logic
* low rules dynamically installed in switch
* Throughput measured using iperf
* Controller logs show PacketIn handling and firewall decisions

---

## Screenshots Included

1. Controller running (POX logs) 
<img width="810" height="229" alt="Screenshot from 2026-04-20 01-02-08" src="https://github.com/user-attachments/assets/58e7ec88-5428-4cc8-a277-73d9c510f839" />

2. Successful ping (h1 → h3)
<img width="971" height="523" alt="Screenshot from 2026-04-20 01-03-30" src="https://github.com/user-attachments/assets/c45914f1-6614-4345-b5cc-f759a6187bf0" />


3. Blocked ping (h1 → h2)
<img width="695" height="163" alt="Screenshot from 2026-04-20 01-05-37" src="https://github.com/user-attachments/assets/0d9dfb58-9c88-4ffc-af2f-c84d4dfa5326" />


4. pingall output (partial drop)
<img width="695" height="163" alt="Screenshot from 2026-04-20 01-06-30" src="https://github.com/user-attachments/assets/5e645778-18dd-49e7-b97a-4deafc0a7ac1" />


5. Flow table entries
<img width="1916" height="846" alt="Screenshot from 2026-04-20 01-07-06" src="https://github.com/user-attachments/assets/37f73fae-fc04-4d4b-a7d5-a42f46b4fe5d" />


6. iperf bandwidth result
<img width="636" height="251" alt="Screenshot from 2026-04-20 01-08-32" src="https://github.com/user-attachments/assets/8480600a-cb3f-4a98-9a02-a07670566815" />


7. Controller logs (PacketIn + blocked traffic)
<img width="890" height="965" alt="Screenshot from 2026-04-20 01-04-55" src="https://github.com/user-attachments/assets/61b5c7e7-db46-49c6-8ba1-079b61e9aeea" />



---

## Key Concepts Demonstrated

* Software Defined Networking (SDN)
* Control Plane vs Data Plane separation
* OpenFlow protocol
* Flow table management
* Match–Action rules
* Centralized network control

---

## Conclusion

The project successfully demonstrates SDN concepts by implementing a learning switch with firewall functionality using a POX controller.
The controller dynamically manages traffic, installs flow rules, and enforces access control, proving the flexibility and power of SDN.

---

## References

* POX Documentation
* Mininet Documentation
* OpenFlow Specification
