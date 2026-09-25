import sys
from pathlib import Path

import streamlit as st


# Add the ResearchNexus project root to Python's import path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from workflows.graph import build_research_graph


st.set_page_config(
    page_title="ResearchNexus",
    page_icon="🔬",
    layout="wide",
)


def main():
    st.title("🔬 ResearchNexus")
    st.subheader("Multi-Agent AI Research Assistant")

    st.write(
        "ResearchNexus uses multiple AI agents to research, analyze, "
        "write, critique, and refine research reports."
    )

    st.divider()

    query = st.text_area(
        "Research Question",
        placeholder=(
            "Enter the topic you want ResearchNexus to investigate..."
        ),
        height=120,
    )

    if st.button("🚀 Start Research", type="primary"):

        if not query.strip():
            st.warning("Please enter a research question.")
            return

        with st.spinner("ResearchNexus is working..."):

            graph = build_research_graph()

            initial_state = {
                "query": query.strip(),
                "revision_count": 0,
                "approved": False,
            }

            final_state = graph.invoke(initial_state)

        st.success("Research completed successfully.")

        st.divider()

        st.subheader("📄 Final Report")

        final_report = final_state.get("final_report", "")

        if final_report:
            st.markdown(final_report)
        else:
            st.warning("No final report was generated.")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Approved",
                "Yes" if final_state.get("approved") else "No",
            )

        with col2:
            st.metric(
                "Revisions",
                final_state.get("revision_count", 0),
            )

        with st.expander("🔍 View Critic Feedback"):
            st.markdown(
                final_state.get(
                    "critique",
                    "No critique available.",
                )
            )


if __name__ == "__main__":
    main()