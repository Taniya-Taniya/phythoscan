# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:37:18 2025

@author: TANIYA
"""

import streamlit as st
from PIL import Image
import base64
import requests

# Set page config
st.set_page_config(page_title="Phythoscan - Leaf Identifier", layout="centered")

# Title
st.title("🌿 Phythoscan - Identify a Leaf and Discover Its Uses")

# Upload Image
uploaded_file = st.file_uploader("📤 Upload a Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Leaf", use_column_width=True)

    # Button to trigger identification
    if st.button("🔍 Identify Leaf"):
        st.info("Identifying... Please wait ⏳")

        # Convert image to base64
        base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")

        # Plant.id API
        api_key = "0XgWeGZovsaC6VQrp8ShyZcJRasPeYi1DwBzkCSRqxC7LDX9hV"  # 🔁 Replace with your free API key from https://web.plant.id
        url = "https://api.plant.id/v2/identify"

        payload = {
            "api_key": api_key,
            "images": [base64_image],
            "plant_details": ["common_names", "wiki_description", "uses"]
        }

        try:
            response = requests.post(url, json=payload).json()
            plant = response['suggestions'][0]
            st.write(response)


            name = plant['plant_name']
            common = ", ".join(plant['plant_details'].get('common_names', []))
            description = plant['plant_details']['wiki_description'].get('value', 'No description available.')
            uses = ", ".join(plant['plant_details'].get('uses', ['No known uses.']))

            # Show results
            st.success(f"✅ Identified: {name} ({common})")
            st.markdown(f"**📖 Description:** {description}")
            st.markdown(f"**🌱 Uses:** {uses}")

            # Save to journal
            if st.button("📝 Save to My Journal"):
                with open("journal.txt", "a") as f:
                    f.write(f"{name} - {common} - {uses}\n")
                st.success("Saved to journal!")

        except Exception as e:
            st.error("❌ Could not identify the plant. Please try a clearer image.")

