import streamlit as st
from PIL import Image

st.set_page_config(page_title="PhytoScan - Leaf Identifier", layout="centered")
st.title("🌿 PhytoScan - Identify a Leaf and Discover Its Uses")

uploaded_file = st.file_uploader("📤 Upload a Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Leaf", use_column_width=True)

    if st.button("🔍 Identify Leaf"):
        st.info("🔍 Identifying... (Demo Mode)")

        # 🔁 DEMO OUTPUT (No API, hardcoded)
        st.success("✅ Identified: Ocimum tenuiflorum (Tulsi)")
        st.markdown("**🌿 Common Names:** Tulsi, Holy Basil")
        st.markdown("**📖 Description:** Tulsi is a sacred plant in India known for its medicinal properties and role in Ayurveda.")
        st.markdown("**🌱 Uses:** Cough, cold, immunity booster, skincare")

        st.caption("🧪 Demo Mode: Output shown without real API response.")
else:
    st.info("📷 Please upload a leaf image to begin.")
