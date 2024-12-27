CAREERS = {
    'SWE': 'Software Engineer',
    'Data Scientist': 'Data Scientist',
    'Data Analyst': 'Data Analyst',
    'Data Engineer': 'Data Engineer',
    'MLE': 'Machine Learning Engineer'
}

CAREER_DESCRIPTIONS = {
    'SWE': """Software Engineers focus on building and maintaining software applications. They excel in:
    • Writing production-grade code
    • Building user-facing applications
    • System design and architecture
    • Working with clear objectives and concrete solutions""",
    
    'Data Scientist': """Data Scientists combine statistics, mathematics, and programming to extract insights. They excel in:
    • Advanced statistical analysis
    • Research and exploration
    • Working with ambiguous problems
    • Developing novel methodologies""",
    
    'Data Analyst': """Data Analysts transform data into actionable insights. They excel in:
    • Business analysis
    • Data visualization
    • Stakeholder communication
    • Quick, impactful solutions""",
    
    'Data Engineer': """Data Engineers build and maintain data infrastructure. They excel in:
    • Pipeline development
    • System architecture
    • Data quality and reliability
    • Infrastructure optimization""",
    
    'MLE': """Machine Learning Engineers focus on deploying ML systems to production. They excel in:
    • Model deployment
    • System optimization
    • Production ML systems
    • Scalable solutions"""
}

QUESTIONS = {
    "work_type": {
        "question": "Which type of work energizes you most?",
        "options": {
            "Building software products and systems from scratch": {"SWE": 2, "MLE": 1},
            "Discovering patterns and insights in data": {"Data Scientist": 1, "Data Analyst": 2},
            "Creating infrastructure that others rely on": {"Data Engineer": 2}
        }
    },
    "problem_approach": {
        "question": "How do you prefer to tackle problems?",
        "options": {
            "Clear objectives with concrete solutions": {"SWE": 1, "Data Engineer": 1},
            "Open-ended questions requiring exploration": {"Data Scientist": 1, "Data Analyst": 1},
            "Complex technical challenges with defined constraints": {"MLE": 2}
        }
    },
    "project_timeline": {
        "question": "What's your ideal project timeline?",
        "options": {
            "Quick wins (days/weeks)": {"Data Analyst": 1, "SWE": 1},
            "Medium-term projects (weeks/months)": {"Data Engineer": 1, "MLE": 1},
            "Long-term research and exploration (months+)": {"Data Scientist": 2}
        }
    },
    "ambiguity": {
        "question": "How do you feel about ambiguity in your work?",
        "options": {
            "Prefer clear, well-defined tasks": {"SWE": 1, "Data Engineer": 1},
            "Comfortable with some ambiguity": {"Data Analyst": 1, "MLE": 1},
            "Thrive in highly ambiguous situations": {"Data Scientist": 2}
        }
    },
    "stakeholder_interaction": {
        "question": "How do you prefer to interact with stakeholders?",
        "options": {
            "Minimal direct interaction": {"Data Engineer": 2},
            "Regular check-ins and presentations": {"Data Analyst": 2, "Data Scientist": 1},
            "Primarily through technical collaboration": {"SWE": 1, "MLE": 1}
        }
    },
    "technical_interest": {
        "question": "Which technical aspect interests you most?",
        "options": {
            "Building user-facing applications": {"SWE": 2},
            "Creating data infrastructure": {"Data Engineer": 2},
            "Analyzing data and building models": {"Data Scientist": 1, "MLE": 1},
            "Interpreting data for business decisions": {"Data Analyst": 2}
        }
    },
    "math_comfort": {
        "question": "How do you feel about mathematics and statistics?",
        "options": {
            "Love complex mathematical problems": {"Data Scientist": 2, "MLE": 2},
            "Comfortable with basic statistics": {"Data Analyst": 2},
            "Prefer logic and algorithms": {"SWE": 1, "Data Engineer": 1}
        }
    },
    "production_comfort": {
        "question": "What's your comfort level with production systems?",
        "options": {
            "Excited to build and maintain them": {"SWE": 2, "Data Engineer": 2},
            "Comfortable deploying models to production": {"MLE": 2},
            "Prefer to focus on analysis and insights": {"Data Analyst": 1, "Data Scientist": 1}
        }
    },
    "oncall": {
        "question": "How do you feel about being on-call or handling emergencies?",
        "options": {
            "Comfortable with production responsibilities": {"SWE": 1, "MLE": 1, "Data Engineer": 1},
            "Prefer not to handle emergency situations": {"Data Analyst": 1, "Data Scientist": 1}
        }
    },
    "career_importance": {
        "question": "What's most important in your first 5 years?",
        "options": {
            "Maximizing earning potential": {"MLE": 2, "SWE": 2},
            "Building broad, versatile skills": {"Data Scientist": 1, "Data Analyst": 1},
            "Developing deep technical expertise": {"Data Engineer": 2}
        }
    },
    "tech_preference": {
        "question": "How do you feel about emerging technologies?",
        "options": {
            "Prefer working with established tools": {"Data Analyst": 1, "SWE": 1},
            "Excited to work with cutting-edge tech": {"MLE": 2, "Data Scientist": 1},
            "Balance of both": {"Data Engineer": 1}
        }
    },
    "impact_type": {
        "question": "What type of impact motivates you most?",
        "options": {
            "Direct product impact": {"SWE": 2, "MLE": 2},
            "Business decision impact": {"Data Analyst": 2, "Data Scientist": 2},
            "Infrastructure and system impact": {"Data Engineer": 2}
        }
    },
    "career_progression": {
        "question": "How important is structured career progression?",
        "options": {
            "Very important": {"SWE": 2, "Data Engineer": 2},
            "Somewhat important": {"MLE": 1, "Data Analyst": 1},
            "Comfortable with flexible paths": {"Data Scientist": 2}
        }
    },
    "learning_style": {
        "question": "How do you prefer to learn new skills?",
        "options": {
            "Creating projects from scratch": {"SWE": 2, "Data Engineer": 2},
            "Studying theory and research papers": {"Data Scientist": 2, "MLE": 2},
            "Analyzing existing solutions": {"Data Analyst": 2}
        }
    },
    "continuous_learning": {
        "question": "How do you feel about continuous learning?",
        "options": {
            "Prefer mastering established technologies": {"Data Analyst": 1, "SWE": 1},
            "Excited to constantly learn new tools": {"MLE": 2, "Data Scientist": 2},
            "Mix of both": {"Data Engineer": 1}
        }
    },
    "education": {
        "question": "Are you interested in pursuing advanced education?",
        "options": {
            "Yes, planning for/have advanced degree": {"Data Scientist": 2, "MLE": 2},
            "Interested in practical certifications": {"Data Engineer": 1, "SWE": 1},
            "Prefer learning through experience": {"Data Analyst": 2}
        }
    },
    "team_structure": {
        "question": "What's your ideal team structure?",
        "options": {
            "Clear hierarchy and roles": {"SWE": 1, "Data Engineer": 1},
            "Cross-functional collaboration": {"Data Scientist": 1, "Data Analyst": 1},
            "Technical autonomy": {"MLE": 2}
        }
    },
    "success_measure": {
        "question": "How do you prefer to measure success?",
        "options": {
            "Concrete metrics": {"SWE": 1, "Data Engineer": 1},
            "Business impact": {"Data Analyst": 2},
            "Research and innovation": {"Data Scientist": 1, "MLE": 1}
        }
    },
    "ml_interest": {
        "question": "Which part of the ML lifecycle interests you most?",
        "options": {
            "Building ML infrastructure and deployment": {"MLE": 2},
            "Research and model development": {"Data Scientist": 2},
            "Using ML tools to solve business problems": {"Data Analyst": 1},
            "Not interested in ML": {"SWE": 1, "Data Engineer": 1}
        }
    },
    "data_cleaning": {
        "question": "How do you feel about data cleaning and preparation?",
        "options": {
            "Enjoy building automated systems for it": {"Data Engineer": 2},
            "See it as necessary part of analysis": {"Data Scientist": 1, "Data Analyst": 1},
            "Prefer working with clean, structured data": {"SWE": 1, "MLE": 1}
        }
    },
    "code_relationship": {
        "question": "What's your ideal relationship with code?",
        "options": {
            "Writing production-grade, maintainable code": {"SWE": 2, "MLE": 2},
            "Building efficient data pipelines": {"Data Engineer": 2},
            "Using code for analysis and modeling": {"Data Scientist": 1},
            "Basic scripting and queries": {"Data Analyst": 1}
        }
    },
    "tools_preference": {
        "question": "Which tools excite you most?",
        "options": {
            "Web frameworks and development tools": {"SWE": 2},
            "Big data processing tools": {"Data Engineer": 2},
            "ML frameworks and algorithms": {"MLE": 2, "Data Scientist": 1},
            "BI and visualization tools": {"Data Analyst": 2, "Data Scientist": 1}
        }
    },
    "problem_solving": {
        "question": "When facing a new problem, what's your first instinct?",
        "options": {
            "Break it down into technical components": {"SWE": 1, "Data Engineer": 1},
            "Look for patterns in available data": {"Data Scientist": 1, "Data Analyst": 1},
            "Consider scalability and implementation": {"MLE": 2}
        }
    },
    "validation": {
        "question": "How do you prefer to validate your work?",
        "options": {
            "Through automated tests and metrics": {"SWE": 2, "Data Engineer": 2},
            "Through statistical validation": {"Data Scientist": 2},
            "Through business impact metrics": {"Data Analyst": 2},
            "Through model performance metrics": {"MLE": 2}
        }
    },
    "debugging": {
        "question": "What type of debugging do you enjoy?",
        "options": {
            "System and code debugging": {"SWE": 2, "Data Engineer": 2},
            "Model performance debugging": {"MLE": 2},
            "Analysis validation": {"Data Scientist": 2},
            "Report/dashboard troubleshooting": {"Data Analyst": 2}
        }
    },
    "documentation": {
        "question": "How do you feel about documentation?",
        "options": {
            "Enjoy writing technical docs": {"SWE": 1, "Data Engineer": 1},
            "Prefer writing analysis reports": {"Data Scientist": 1, "Data Analyst": 1},
            "Focus on model/system specifications": {"MLE": 1}
        }
    },
    "project_ownership": {
        "question": "What's your preferred project ownership style?",
        "options": {
            "End-to-end product ownership": {"SWE": 2},
            "Pipeline and infrastructure ownership": {"Data Engineer": 2},
            "Analysis and insight ownership": {"Data Analyst": 2},
            "Model development and deployment ownership": {"MLE": 2},
            "Research and methodology ownership": {"Data Scientist": 2}
        }
    },
    "deadlines": {
        "question": "How do you handle tight deadlines?",
        "options": {
            "Prioritize core functionality": {"SWE": 2},
            "Focus on data quality and reliability": {"Data Engineer": 2},
            "Simplify analysis scope": {"Data Analyst": 2},
            "Use simpler models/approaches": {"Data Scientist": 1, "MLE": 1}
        }
    },
    "industry_interest": {
        "question": "Which industry aspect interests you most?",
        "options": {
            "Building consumer-facing products": {"SWE": 2},
            "Creating robust data infrastructure": {"Data Engineer": 2},
            "Solving business problems": {"Data Analyst": 2, "Data Scientist": 1},
            "Advancing ML/AI capabilities": {"MLE": 2, "Data Scientist": 1}
        }
    },
    "domain_importance": {
        "question": "How important is domain expertise in your work?",
        "options": {
            "More focused on technical skills": {"SWE": 1, "Data Engineer": 1},
            "Balance of domain and technical": {"MLE": 2},
            "Heavy emphasis on domain knowledge": {"Data Scientist": 1, "Data Analyst": 1}
        }
    },
    "ai_impact": {
        "question": "How do you see AI impacting your role?",
        "options": {
            "As tools to enhance productivity": {"SWE": 1, "Data Engineer": 1},
            "As core technology to work with": {"MLE": 2, "Data Scientist": 2},
            "As analysis tools to leverage": {"Data Analyst": 1}
        }
    },
    "impact_growth": {
        "question": "How do you want to grow your impact?",
        "options": {
            "Through better technical solutions": {"SWE": 2, "Data Engineer": 2},
            "Through more sophisticated models": {"MLE": 2},
            "Through better business decisions": {"Data Analyst": 2},
            "Through novel approaches/research": {"Data Scientist": 2}
        }
    },
    "recognition": {
        "question": "What type of recognition motivates you?",
        "options": {
            "Product success metrics": {"SWE": 2},
            "System reliability metrics": {"Data Engineer": 2},
            "Business impact metrics": {"Data Analyst": 2},
            "Model performance improvements": {"MLE": 2},
            "Research/innovation recognition": {"Data Scientist": 2}
        }
    }
}