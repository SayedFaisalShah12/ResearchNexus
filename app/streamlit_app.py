import sys
from pathlib import Path

import streamlit as st

# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from workflows.graph import build_research_graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchNexus AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* --------------------------------------------------------
       HERO
    -------------------------------------------------------- */

    .hero {
        padding: 2rem 0 1.5rem 0;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(99, 102, 241, 0.25);
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.7;
        max-width: 800px;
        line-height: 1.7;
    }

    /* --------------------------------------------------------
       WORKFLOW
    -------------------------------------------------------- */

    .workflow-card {
        padding: 1.25rem;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background: rgba(128, 128, 128, 0.04);
        margin: 1rem 0 1.5rem 0;
    }

    .workflow-title {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        opacity: 0.6;
        margin-bottom: 1rem;
    }

    .workflow {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.5rem;
    }

    .workflow-step {
        flex: 1;
        text-align: center;
        padding: 0.75rem 0.4rem;
        border-radius: 10px;
        background: rgba(128, 128, 128, 0.08);
        font-size: 0.8rem;
        font-weight: 600;
    }

    .workflow-arrow {
        opacity: 0.4;
        font-size: 1.2rem;
    }

    /* --------------------------------------------------------
       REPORT
    -------------------------------------------------------- */

    .report-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .report-container {
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background: rgba(128, 128, 128, 0.035);
        line-height: 1.8;
    }

    /* --------------------------------------------------------
       SOURCE CARD
    -------------------------------------------------------- */

    .source-card {
        padding: 1rem;
        margin-bottom: 0.75rem;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.035);
    }

    .source-number {
        font-weight: 700;
        opacity: 0.65;
    }

    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.15);
    }

    .sidebar-title {
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .sidebar-subtitle {
        font-size: 0.8rem;
        opacity: 0.6;
        margin-bottom: 1.5rem;
    }

    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer {
        text-align: center;
        padding: 3rem 0 1rem 0;
        opacity: 0.5;
        font-size: 0.8rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">🔬 ResearchNexus</div>
        <div class="sidebar-subtitle">
            Multi-Agent AI Research Assistant
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### ⚙️ Research Settings")

    max_revisions = st.slider(
        "Maximum revisions",
        min_value=0,
        max_value=3,
        value=2,
        help="Maximum number of Writer → Critic revision cycles.",
    )

    st.divider()

    st.markdown("### 🤖 Agent Pipeline")

    st.markdown(
        """
        **01 · Research Agent**  
        Searches the web and collects sources.

        **02 · Analyst Agent**  
        Extracts findings and identifies conflicts.

        **03 · Writer Agent**  
        Produces the research report.

        **04 · Critic Agent**  
        Evaluates accuracy and completeness.

        **05 · Decision Node**  
        Approves or sends the report back for revision.
        """
    )

    st.divider()

    st.caption("ResearchNexus AI")
    st.caption("Powered by LangGraph + Hugging Face + Tavily")


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ MULTI-AGENT RESEARCH SYSTEM
        </div>

        <div class="hero-title">
            ResearchNexus
        </div>

        <div class="hero-subtitle">
            Turn a research question into a structured, evidence-based
            report using autonomous research, analysis, writing,
            and critic agents.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# WORKFLOW VISUALIZATION
# ============================================================

st.markdown(
    """
    <div class="workflow-card">

        <div class="workflow-title">
            Agent Workflow
        </div>

        <div class="workflow">

            <div class="workflow-step">
                🔎<br>
                Research
            </div>

            <div class="workflow-arrow">→</div>

            <div class="workflow-step">
                🧠<br>
                Analysis
            </div>

            <div class="workflow-arrow">→</div>

            <div class="workflow-step">
                ✍️<br>
                Writing
            </div>

            <div class="workflow-arrow">→</div>

            <div class="workflow-step">
                🔍<br>
                Critic
            </div>

            <div class="workflow-arrow">→</div>

            <div class="workflow-step">
                ✅<br>
                Decision
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESEARCH INPUT
# ============================================================

st.subheader("What would you like to research?")

query = st.text_area(
    "Research Question",
    placeholder=(
        "Example: What are the latest developments in generative AI "
        "and how are they affecting software engineering?"
    ),
    height=130,
    label_visibility="collapsed",
)


# ============================================================
# EXAMPLE QUESTIONS
# ============================================================

st.markdown("**Try an example:**")

example_columns = st.columns(3)

examples = [
    "Latest developments in generative AI",
    "Impact of AI agents on software engineering",
    "Future of multimodal AI systems",
]

for column, example in zip(example_columns, examples):
    with column:
        if st.button(
            example,
            use_container_width=True,
        ):
            st.session_state["query"] = example
            st.rerun()


if "query" in st.session_state:
    query = st.session_state["query"]


# ============================================================
# START BUTTON
# ============================================================

st.write("")

start_research = st.button(
    "🚀 Start Research",
    type="primary",
    use_container_width=True,
)


# ============================================================
# WORKFLOW EXECUTION
# ============================================================

if start_research:

    if not query or not query.strip():

        st.warning(
            "Please enter a research question before starting."
        )

    else:

        query = query.strip()

        st.divider()

        st.subheader("🔄 Research in progress")

        progress = st.progress(0)

        status = st.status(
            "ResearchNexus is starting...",
            expanded=True,
        )

        try:

            # ------------------------------------------------
            # STEP 1
            # ------------------------------------------------

            status.update(
                label="🔎 Research Agent is searching the web...",
                state="running",
            )

            progress.progress(10)

            graph = build_research_graph()

            initial_state = {
                "query": query,
                "revision_count": 0,
                "approved": False,
            }

            # ------------------------------------------------
            # RUN GRAPH
            # ------------------------------------------------

            final_state = graph.invoke(initial_state)

            progress.progress(100)

            # ------------------------------------------------
            # COMPLETE
            # ------------------------------------------------

            status.update(
                label="✅ Research completed",
                state="complete",
                expanded=False,
            )

        except Exception as exc:

            status.update(
                label="❌ Research failed",
                state="error",
            )

            st.error(
                "ResearchNexus encountered an error while "
                "processing your request."
            )

            with st.expander("Technical details"):
                st.exception(exc)

            st.stop()

        # ====================================================
        # RESULTS
        # ====================================================

        st.divider()

        st.subheader("📊 Research Results")

        # ----------------------------------------------------
        # METRICS
        # ----------------------------------------------------

        documents = final_state.get("documents", [])
        revision_count = final_state.get(
            "revision_count",
            0,
        )
        approved = final_state.get(
            "approved",
            False,
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Sources",
                len(documents),
            )

        with col2:
            st.metric(
                "Revisions",
                revision_count,
            )

        with col3:
            st.metric(
                "Status",
                "Approved" if approved else "Completed",
            )

        with col4:
            st.metric(
                "Agents",
                "4",
            )

        st.write("")

        # ====================================================
        # FINAL REPORT
        # ====================================================

        st.subheader("📄 Final Research Report")

        final_report = final_state.get(
            "final_report",
            "",
        )

        if final_report:

            st.markdown(
                '<div class="report-container">',
                unsafe_allow_html=True,
            )

            st.markdown(final_report)

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

            st.write("")

            st.download_button(
                label="⬇️ Download Report",
                data=final_report,
                file_name="researchnexus_report.md",
                mime="text/markdown",
            )

        else:

            st.warning(
                "No final report was generated."
            )

        # ====================================================
        # SOURCES
        # ====================================================

        st.divider()

        with st.expander(
            f"🔗 Sources ({len(documents)})",
            expanded=False,
        ):

            if documents:

                for index, document in enumerate(
                    documents,
                    start=1,
                ):

                    url = document.get(
                        "url",
                        "",
                    )

                    st.markdown(
                        f"""
                        <div class="source-card">

                        <span class="source-number">
                        Source {index}
                        </span>

                        <br>

                        <a href="{url}" target="_blank">
                        {url}
                        </a>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            else:

                st.info(
                    "No source documents were collected."
                )

        # ====================================================
        # CRITIC FEEDBACK
        # ====================================================

        with st.expander(
            "🔍 Critic Feedback",
            expanded=False,
        ):

            critique = final_state.get(
                "critique",
                "",
            )

            if critique:
                st.markdown(critique)
            else:
                st.info(
                    "No critic feedback is available."
                )

        # ====================================================
        # ANALYSIS
        # ====================================================

        with st.expander(
            "🧠 Analyst Findings",
            expanded=False,
        ):

            analysis = final_state.get(
                "analysis",
                "",
            )

            if analysis:
                st.markdown(analysis)
            else:
                st.info(
                    "No analysis is available."
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        ResearchNexus · Multi-Agent AI Research Assistant

        <br>

        LangGraph · Hugging Face · Tavily · Streamlit

    </div>
    """,
    unsafe_allow_html=True,
)