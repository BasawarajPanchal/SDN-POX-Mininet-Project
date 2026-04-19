from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    dpid = event.connection.dpid
    mac_to_port.setdefault(dpid, {})

    # Learn MAC address
    mac_to_port[dpid][packet.src] = event.port

    # 🚫 Firewall: block h1 → h2
    if str(packet.src) == "00:00:00:00:00:01" and str(packet.dst) == "00:00:00:00:00:02":
        log.info("Blocked traffic from h1 to h2")
        return

    # Forwarding logic
    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

    # Install flow rule
    if out_port != of.OFPP_FLOOD:
        fm = of.ofp_flow_mod()
        fm.match = of.ofp_match.from_packet(packet, event.port)
        fm.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(fm)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
