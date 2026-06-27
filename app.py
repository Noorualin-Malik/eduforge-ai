import streamlit as st

from graph import build_graph

st.set_page_config(
    page_title="EduForge",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 EduForge")
st.caption("AI-Powered Learning Assistant")

with st.sidebar:
    st.header("Configuration")
    st.info(
        "Configure GOOGLE_API_KEY and TAVILY_API_KEY in the .env file."
    )

if "result" not in st.session_state:
    st.session_state.result = None

topic = st.text_input(
    "What do you want to learn?",
    placeholder="Example: LangGraph, Machine Learning, Python..."
)

if st.button("Generate Learning Plan", type="primary"):

    if topic.strip():

        graph = build_graph()

        initial_state = {
            "topic": topic,
            "roadmap": {},
            "research": {},
            "quiz": {},
            "evaluation": {},
            "final_output": {},
            "messages": [],
        }

        with st.spinner("Creating your learning roadmap..."):
            st.session_state.result = graph.invoke(initial_state)

result = st.session_state.result

if result:

    roadmap = result["roadmap"]

    st.header(roadmap["title"])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Difficulty", roadmap["difficulty"])

    with col2:
        st.metric(
            "Estimated Duration",
            roadmap["estimated_duration"],
        )

    st.divider()

    st.subheader("🎯 Learning Objectives")

    for item in roadmap["learning_objectives"]:
        st.markdown(f"- {item}")

    st.divider()

    st.subheader("📅 Weekly Study Plan")

    for week in roadmap["weekly_plan"]:

        with st.expander(f"Week {week['week']}"):

            st.markdown("### Topics")

            for topic in week["topics"]:
                st.markdown(f"- {topic}")

            st.markdown("### Goals")

            for goal in week["goals"]:
                st.markdown(f"- {goal}")

    st.divider()

    st.subheader("🚀 Recommended Projects")

    for project in roadmap["recommended_projects"]:
        st.success(project)

    st.divider()

    st.subheader("📚 Study Notes")

    st.write(result["research"]["summary"]["summary"])

    st.subheader("📝 Quiz")

    for i, question in enumerate(result["quiz"]["mcqs"], start=1):

        st.markdown(f"### Q{i}")

        st.write(question["question"])

        st.radio(
            "Choose an answer",
            question["options"],
            key=f"mcq_{i}",
        )

        with st.expander("Show Answer"):

            st.success(question["answer"])

            st.info(question["explanation"])

    st.divider()

    evaluation = result["evaluation"]

    st.header("Evaluation")

    st.metric("Overall Score", f'{evaluation["overall_score"]}/10')

    st.markdown("### Feedback")

    st.write(evaluation["feedback"])

    st.markdown("### Strengths")

    for s in evaluation["strengths"]:
        st.markdown(f"- {s}")

    st.markdown("### Improvements")

    for s in evaluation["improvements"]:
        st.markdown(f"- {s}")