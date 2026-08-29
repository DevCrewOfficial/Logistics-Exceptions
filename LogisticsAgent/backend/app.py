import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from agent.core import run_agent
from agent.tools.mock_sys import SHIPMENTS
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
st.set_page_config(page_title="Shipment Support Agent", layout="wide")
st.title("Shipment Support Agent")
st.caption("Tell us about your shipment issue and our agent will help resolve it.")
st.subheader("Shipment Details")
shipment_id = st.text_input("Shipment ID", placeholder="Example: SHIP001")
issue = st.selectbox("Issue Faced", ["Damaged Package", "Failed Delivery", "Missing Documentation", "Bad Address", "Delayed Shipment"])
problem = st.text_area("Describe the Problem", height=120)
if st.button("Submit Issue", type="primary"):
    if not shipment_id or not problem:
        st.warning("Please fill in Shipment ID and problem description.")
    else:
        user_message = "Shipment ID: " + shipment_id + "\nIssue Type: " + issue + "\nCustomer Problem:\n" + problem
        with st.spinner("Agent working..."):
            trail = []
            answer, history, trail = run_agent(client, user_message, [], trail)
        st.success(answer)
        st.subheader("Agent Execution Trail")
        for i, step in enumerate(trail):
            ok = step["result"].get("success", True) if isinstance(step["result"], dict) else True
            st.markdown(("OK " if ok else "WARN ") + "Step " + str(i+1) + ": " + step["tool"])
            st.json(step["result"])
        st.subheader("Live Shipment States")
        st.json(SHIPMENTS)
