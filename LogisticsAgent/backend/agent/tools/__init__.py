from .mock_sys import get_shipment_status, reschedule_delivery, redirect_shipment, initiate_replacement, request_missing_document, notify_customer, create_ops_ticket, escalate_to_human
TOOLS = [
    {"type": "function", "function": {"name": "get_shipment_status", "description": "Get shipment status. ALWAYS call first.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}}, "required": ["shipment_id"]}}},
    {"type": "function", "function": {"name": "reschedule_delivery", "description": "Reschedule delivery.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "new_date": {"type": "string"}}, "required": ["shipment_id", "new_date"]}}},
    {"type": "function", "function": {"name": "redirect_shipment", "description": "Redirect shipment address.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "new_address": {"type": "string"}}, "required": ["shipment_id", "new_address"]}}},
    {"type": "function", "function": {"name": "initiate_replacement", "description": "Start replacement for damaged item.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}}, "required": ["shipment_id"]}}},
    {"type": "function", "function": {"name": "request_missing_document", "description": "Request missing document.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "doc_type": {"type": "string"}}, "required": ["shipment_id", "doc_type"]}}},
    {"type": "function", "function": {"name": "notify_customer", "description": "Notify customer of outcome.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "message": {"type": "string"}}, "required": ["shipment_id", "message"]}}},
    {"type": "function", "function": {"name": "create_ops_ticket", "description": "Create ops ticket.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "reason": {"type": "string"}}, "required": ["shipment_id", "reason"]}}},
    {"type": "function", "function": {"name": "escalate_to_human", "description": "Escalate to human if value over 5000, action fails twice, or unclear.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "reason": {"type": "string"}}, "required": ["shipment_id", "reason"]}}},
]
FUNCTIONS = {"get_shipment_status": get_shipment_status, "reschedule_delivery": reschedule_delivery, "redirect_shipment": redirect_shipment, "initiate_replacement": initiate_replacement, "request_missing_document": request_missing_document, "notify_customer": notify_customer, "create_ops_ticket": create_ops_ticket, "escalate_to_human": escalate_to_human}
def execute_tool(name, args):
    try:
        return FUNCTIONS[name](**args)
    except Exception as e:
        return {"success": False, "error": str(e)}
