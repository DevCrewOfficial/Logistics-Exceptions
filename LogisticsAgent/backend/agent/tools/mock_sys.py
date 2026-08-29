import random
SHIPMENTS = {"SHIP001": {"status": "in_transit", "damaged": False, "value": 2500, "address": "12 MG Road, Hyderabad", "eta": "2026-08-30"}, "SHIP002": {"status": "delivery_failed", "damaged": False, "value": 8500, "address": "Incomplete address", "eta": "2026-08-29"}, "SHIP003": {"status": "in_transit", "damaged": False, "value": 1200, "address": "45 Park St, Kolkata", "eta": "2026-09-02"}}
TICKETS = []
NOTIFICATIONS = []
def get_shipment_status(shipment_id):
    s = SHIPMENTS.get(shipment_id)
    if not s: return {"success": False, "error": "Shipment not found"}
    return {"success": True, **s}
def reschedule_delivery(shipment_id, new_date):
    if random.random() < 0.3: return {"success": False, "error": "Carrier API timeout"}
    if shipment_id not in SHIPMENTS: return {"success": False, "error": "Shipment not found"}
    SHIPMENTS[shipment_id]["eta"] = new_date
    SHIPMENTS[shipment_id]["status"] = "rescheduled"
    return {"success": True, "new_eta": new_date}
def redirect_shipment(shipment_id, new_address):
    if shipment_id not in SHIPMENTS: return {"success": False, "error": "Shipment not found"}
    SHIPMENTS[shipment_id]["address"] = new_address
    SHIPMENTS[shipment_id]["status"] = "redirected"
    return {"success": True, "new_address": new_address}
def initiate_replacement(shipment_id):
    if shipment_id not in SHIPMENTS: return {"success": False, "error": "Shipment not found"}
    SHIPMENTS[shipment_id]["status"] = "replacement_initiated"
    SHIPMENTS[shipment_id]["damaged"] = True
    return {"success": True, "replacement_id": "REPL-" + shipment_id}
def request_missing_document(shipment_id, doc_type):
    return {"success": True, "requested_doc": doc_type, "status": "pending_customer"}
def notify_customer(shipment_id, message):
    NOTIFICATIONS.append({"shipment_id": shipment_id, "message": message})
    return {"success": True, "notified": True}
def create_ops_ticket(shipment_id, reason):
    tid = "TICKET-" + str(len(TICKETS)+1)
    TICKETS.append({"id": tid, "shipment_id": shipment_id, "reason": reason})
    return {"success": True, "ticket_id": tid}
def escalate_to_human(shipment_id, reason):
    return {"success": True, "escalated": True, "reason": reason}
