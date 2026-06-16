from modules.idea_analyzer import analyze_idea
from modules.benefits_analyzer import analyze_benefits
from modules.innovation_analyzer import analyze_innovation
from modules.feature_generator import generate_features
from modules.mvp_generator import generate_mvp
from modules.techstack_generator import generate_techstack
from modules.architecture_generator import generate_architecture
from modules.database_generator import generate_database
from modules.roadmap_generator import generate_roadmap
from modules.cost_estimator import generate_cost_estimate
from modules.market_analyzer import analyze_market
from modules.competitor_analyzer import analyze_competitors
from modules.revenue_model_generator import generate_revenue_model

import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
if "blueprint_generated" not in st.session_state:
    st.session_state.blueprint_generated = False

# Page Config
st.set_page_config(
    page_title="IdeaForge AI",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("🚀 IdeaForge AI")

st.subheader(
    "Transform Your Idea Into A Complete Project Blueprint"
)

# User Input
idea = st.text_area(
    "Enter your project idea",
    placeholder="Example: AI-powered study planner"
)

# Generate Button
if st.button("Generate Blueprint"):

    if idea.strip() == "":
        st.warning("Please enter a project idea.")

    else:
        with st.spinner("Analyzing your idea..."):

            # AI Modules
            analysis = analyze_idea(client, idea)
            benefits = analyze_benefits(client, idea)
            innovation = analyze_innovation(client, idea)
            features = generate_features(client, idea)
            mvp = generate_mvp(client, idea)
            techstack = generate_techstack(client, idea)
            architecture = generate_architecture(client, idea)
            database = generate_database(client, idea)
            roadmap = generate_roadmap(client, idea)
            cost = generate_cost_estimate(client, idea)
            market = analyze_market(client, idea)
            competitors = analyze_competitors(client, idea)
            revenue = generate_revenue_model(client, idea)

            st.success("Analysis Complete!")

            # Save results
            st.session_state.blueprint_generated = True

            st.session_state.results = {
                "📌 Idea Analysis": analysis,
                "⚡ Benefits & Challenges": benefits,
                "💡 Innovation": innovation,
                "🛠 Features": features,
                "🚀 MVP": mvp,
                "🏗 Tech Stack": techstack,
                "🏛 Architecture": architecture,
                "🗄 Database": database,
                "📅 Roadmap": roadmap,
                "💰 Cost": cost,
                "📊 Market Analysis": market,
                "🏆 Competitor Analysis": competitors,
                "💸 Revenue Model": revenue
            }

# ---------------------------------------
# CARD VIEW
# ---------------------------------------

if st.session_state.blueprint_generated:

    if "selected_feature" not in st.session_state:
        st.session_state.selected_feature = None

    # SHOW DETAIL PAGE
    if st.session_state.selected_feature:

        st.markdown(
            f"# {st.session_state.selected_feature}"
        )

        st.write(
            st.session_state.results[
                st.session_state.selected_feature
            ]
        )

        if st.button("⬅ Back to Features"):
            st.session_state.selected_feature = None
            st.rerun()

    # SHOW ALL CARDS
    else:

        st.markdown("## 🚀 Project Blueprint")

        col1, col2, col3 = st.columns(3)

        features_list = list(
            st.session_state.results.keys()
        )

        for i, feature in enumerate(features_list):

            with [col1, col2, col3][i % 3]:

                st.markdown(
                    f"""
                    <div style="
                    background:#111827;
                    padding:20px;
                    border-radius:15px;
                    margin-bottom:15px;
                    border:1px solid #374151;
                    ">
                    <h4>{feature}</h4>
                    <p>Click to explore</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Open {feature}",
                    key=feature
                ):
                    st.session_state.selected_feature = feature
                    st.rerun()