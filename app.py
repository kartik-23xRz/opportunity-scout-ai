import streamlit as st
from src.agent import run_opportunity_scout

st.set_page_config(page_title="Opportunity Scout AI", page_icon="🎯", layout="wide")

st.title("🎯 Opportunity Scout AI")
st.caption("An AI agent that searches, evaluates and ranks internship opportunities.")

with st.sidebar:
    st.header("About this agent")
    st.write("1. Understands your profile")
    st.write("2. Searches the web using Tavily")
    st.write("3. Checks skill relevance")
    st.write("4. Uses Gemini to explain the best matches")
    st.divider()
    st.caption("Demo project • Verify every opening on its original application page.")

st.subheader("Tell the agent what you're looking for")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your name (optional)")
    degree = st.selectbox("Education", ["B.Tech", "B.E.", "BCA", "MCA", "M.Tech", "Other"])
    branch = st.text_input("Branch / specialization", value="Computer Science - AI/ML")
    graduation_year = st.selectbox("Graduation year", [2027, 2028, 2029, 2030, 2026], index=1)
with col2:
    role = st.text_input("Target role", value="AI/ML Intern")
    skills = st.text_area("Your skills (comma separated)", value="Python, Machine Learning, SQL, Pandas, NumPy")
    location = st.text_input("Preferred location", value="India")
    work_mode = st.selectbox("Work preference", ["Any", "Remote", "On-site", "Hybrid"])

if st.button("🚀 Find matching opportunities", type="primary", use_container_width=True):
    if not role.strip() or not skills.strip():
        st.warning("Please enter your target role and at least one skill.")
    else:
        profile = {
            "name": name.strip() or "Student",
            "degree": degree,
            "branch": branch.strip(),
            "graduation_year": graduation_year,
            "role": role.strip(),
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "location": location.strip() or "India",
            "work_mode": work_mode,
        }
        with st.status("Opportunity Scout is working...", expanded=True) as status:
            st.write("🧠 Understanding your profile...")
            st.write("🔎 Searching the web for opportunities...")
            st.write("⚖️ Comparing skills and requirements...")
            try:
                result = run_opportunity_scout(profile)
                status.update(label="Search and analysis complete", state="complete", expanded=False)
            except Exception as exc:
                status.update(label="The agent could not complete the search", state="error", expanded=True)
                st.error(str(exc))
                st.info("Check that GEMINI_API_KEY and TAVILY_API_KEY are configured in Streamlit Secrets.")
                st.stop()

        st.subheader("Your matching opportunities")
        st.caption(f"Search query: {result.get('search_query', '')} • Results found: {len(result.get('opportunities', []))}")
        if result.get("summary"):
            st.info(result["summary"])

        opportunities = result.get("opportunities", [])
        if not opportunities:
            st.warning("No suitable opportunities were returned. Try a broader role or location.")
        for i, item in enumerate(opportunities, start=1):
            title = item.get("title") or "Untitled opportunity"
            company = item.get("company") or "Company not identified"
            score = item.get("match_score", 0)
            with st.container(border=True):
                top1, top2 = st.columns([4, 1])
                with top1:
                    st.markdown(f"### {i}. {title}")
                    st.write(company)
                with top2:
                    st.metric("Skill match", f"{score}%")
                st.write(item.get("reason", "Review the source for details."))
                if item.get("eligibility"):
                    st.write("**Eligibility:**", item["eligibility"])
                if item.get("location"):
                    st.write("**Location / mode:**", item["location"])
                if item.get("deadline"):
                    st.write("**Deadline:**", item["deadline"])
                url = item.get("url", "")
                if url.startswith("http"):
                    st.link_button("Open original listing", url)
                else:
                    st.caption("No direct application URL was found. Verify using the source.")
        st.divider()
        st.subheader("Personalized application email")
        st.write(result.get("email_draft", "No email draft generated."))
        st.caption("Always review and personalize this draft before sending.")

st.divider()
st.caption("Built with Python • Streamlit • LangGraph • Gemini • Tavily")
