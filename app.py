import streamlit as st
import pandas as pd
import plotly.express as px
from collections import defaultdict
from config import CAREERS, CAREER_DESCRIPTIONS, QUESTIONS


def initialize_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = 0
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    if 'scores' not in st.session_state:
        st.session_state.scores = defaultdict(float)

def calculate_scores(responses):
    scores = defaultdict(float)
    for question, response in responses.items():
        if response in QUESTIONS[question]["options"]:
            weights = QUESTIONS[question]["options"][response]
            for career, weight in weights.items():
                scores[career] += weight
    return scores

def normalize_scores(scores):
    total = sum(scores.values())
    if total == 0:
        return {career: 0 for career in CAREERS}
    return {career: (score/total) * 100 for career, score in scores.items()}

def create_results_visualization(scores):
    df = pd.DataFrame({
        'Career': list(scores.keys()),
        'Match Percentage': list(scores.values())
    })
    
    fig = px.bar(df, 
                 x='Match Percentage', 
                 y='Career',
                 orientation='h',
                 title='Career Match Percentages',
                 color='Match Percentage',
                 color_continuous_scale='Viridis')
    
    fig.update_layout(
        xaxis_title="Match Percentage (%)",
        yaxis_title="Career Path",
        showlegend=False
    )
    
    return fig

def display_question(question_id):
    question_data = QUESTIONS[question_id]
    st.write(f"### {question_data['question']}")
    
    options = list(question_data["options"].keys())
    response = st.radio("Select your answer:", options, key=question_id)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Next"):
            st.session_state.responses[question_id] = response
            st.session_state.page += 1
            st.rerun()

def display_results():
    scores = calculate_scores(st.session_state.responses)
    normalized_scores = normalize_scores(scores)
    
    # Sort careers by score
    sorted_careers = sorted(normalized_scores.items(), key=lambda x: x[1], reverse=True)
    top_career = sorted_careers[0][0]
    
    st.write("# Your Results")
    st.write(f"## Top Career Match: {CAREERS[top_career]}")
    st.write(CAREER_DESCRIPTIONS[top_career])
    
    st.write("## Career Match Breakdown")
    fig = create_results_visualization(normalized_scores)
    st.plotly_chart(fig)
    
    st.write("## Next Steps")
    st.write("""
    1. Research your top matches in detail
    2. Connect with professionals in these roles
    3. Explore required skills and certifications
    4. Consider taking relevant online courses
    """)

def main():
    st.set_page_config(page_title="Data Career Quiz", page_icon="📊", layout="wide")
    
    st.title("Data Career Path Quiz")
    st.write("""
    Discover which data/engineering career path best matches your interests, skills, and working style.
    Answer the following questions to get personalized career recommendations.
    """)
    
    initialize_session_state()
    
    if st.session_state.page >= len(QUESTIONS):
        display_results()
    else:
        progress = st.progress(st.session_state.page / len(QUESTIONS))
        st.write(f"Question {st.session_state.page + 1} of {len(QUESTIONS)}")
        display_question(list(QUESTIONS.keys())[st.session_state.page])

if __name__ == "__main__":
    main()