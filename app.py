import streamlit as st
import pandas as pd

# Configuration and data structure
COMPARISON_DATA = {
    'Cloud Compute': {
        'AWS Lambda vs EC2': {
            'option_a': {'name': '🟦 AWS Lambda', 'emoji': '⚡'},
            'option_b': {'name': '🟩 EC2', 'emoji': '🖥️'},
            'comparison': {
                'Cost': ['Pay per execution', 'Pay for uptime'],
                'Scalability': ['Auto-scales to zero', 'Manual scaling'],
                'Learning Curve': ['Serverless mindset needed', 'Traditional server knowledge'],
                'Best Use Case': ['Event-driven workloads', 'Long-running applications']
            },
            'verdict': {
                'option_a_scenario': "If you need automatic scaling and pay-per-use pricing for sporadic workloads, choose Lambda.",
                'option_b_scenario': "If you need full control, persistent connections, or long-running processes, choose EC2."
            },
            'scores': {'option_a': 8, 'option_b': 6}
        },
        'Fargate vs EKS': {
            'option_a': {'name': '🟦 AWS Fargate', 'emoji': '🚢'},
            'option_b': {'name': '🟩 EKS', 'emoji': '☸️'},
            'comparison': {
                'Cost': ['Pay for task resources', 'Pay for cluster + nodes'],
                'Scalability': ['Serverless containers', 'Kubernetes orchestration'],
                'Learning Curve': ['Simplified container deployment', 'Kubernetes expertise required'],
                'Best Use Case': ['Simple containerized apps', 'Complex microservices']
            },
            'verdict': {
                'option_a_scenario': "If you want serverless containers without infrastructure management, choose Fargate.",
                'option_b_scenario': "If you need advanced orchestration and full Kubernetes features, choose EKS."
            },
            'scores': {'option_a': 7, 'option_b': 5}
        }
    },
    'Database': {
        'DynamoDB vs RDS': {
            'option_a': {'name': '🟦 DynamoDB', 'emoji': '⚡'},
            'option_b': {'name': '🟩 RDS', 'emoji': '🗄️'},
            'comparison': {
                'Cost': ['Pay per request/storage', 'Pay for instance uptime'],
                'Scalability': ['Automatic horizontal scaling', 'Vertical scaling with downtime'],
                'Learning Curve': ['NoSQL paradigm', 'Familiar SQL interface'],
                'Best Use Case': ['High-traffic web apps', 'Complex relational data']
            },
            'verdict': {
                'option_a_scenario': "If you need massive scale with unpredictable traffic patterns, choose DynamoDB.",
                'option_b_scenario': "If you have complex queries and existing SQL knowledge, choose RDS."
            },
            'scores': {'option_a': 9, 'option_b': 7}
        },
        'MongoDB vs PostgreSQL': {
            'option_a': {'name': '🟦 MongoDB', 'emoji': '🍃'},
            'option_b': {'name': '🟩 PostgreSQL', 'emoji': '🐘'},
            'comparison': {
                'Cost': ['Document-based pricing', 'Open source with hosting costs'],
                'Scalability': ['Built-in sharding', 'Requires manual partitioning'],
                'Learning Curve': ['JSON-like documents', 'SQL and relational concepts'],
                'Best Use Case': ['Rapid prototyping, flexible schemas', 'ACID compliance, complex queries']
            },
            'verdict': {
                'option_a_scenario': "If you need flexible schemas and rapid development cycles, choose MongoDB.",
                'option_b_scenario': "If you need strong consistency and complex relational queries, choose PostgreSQL."
            },
            'scores': {'option_a': 8, 'option_b': 9}
        }
    },
    'Frontend Framework': {
        'React vs Vue': {
            'option_a': {'name': '🟦 React', 'emoji': '⚛️'},
            'option_b': {'name': '🟩 Vue', 'emoji': '💚'},
            'comparison': {
                'Cost': ['Large ecosystem, more devs', 'Smaller but growing community'],
                'Scalability': ['Component-based architecture', 'Progressive framework'],
                'Learning Curve': ['JSX and functional concepts', 'Template-based, gentler slope'],
                'Best Use Case': ['Large enterprise applications', 'Rapid prototyping and small-medium apps']
            },
            'verdict': {
                'option_a_scenario': "If you need maximum ecosystem support and plan to scale a large team, choose React.",
                'option_b_scenario': "If you want faster onboarding and simpler syntax for smaller projects, choose Vue."
            },
            'scores': {'option_a': 7, 'option_b': 8}
        },
        'Angular vs Svelte': {
            'option_a': {'name': '🟦 Angular', 'emoji': '🅰️'},
            'option_b': {'name': '🟩 Svelte', 'emoji': '🔥'},
            'comparison': {
                'Cost': ['Enterprise-grade tooling', 'Minimal bundle size'],
                'Scalability': ['Full framework with everything built-in', 'Compile-time optimizations'],
                'Learning Curve': ['Steep learning curve, TypeScript heavy', 'Simple and intuitive'],
                'Best Use Case': ['Large enterprise applications', 'Performance-critical applications']
            },
            'verdict': {
                'option_a_scenario': "If you need a complete framework with enterprise features and don't mind complexity, choose Angular.",
                'option_b_scenario': "If you prioritize performance and developer experience with minimal overhead, choose Svelte."
            },
            'scores': {'option_a': 6, 'option_b': 9}
        }
    }
}

def main():
    st.set_page_config(
        page_title="The Tech Referee",
        page_icon="⚡",
        layout="wide"
    )

    # Sidebar Configuration
    st.sidebar.header("🥊 Configure the Match")

    # Category selection
    category = st.sidebar.selectbox(
        "Category:",
        options=list(COMPARISON_DATA.keys()),
        index=0
    )

    # Matchup selection based on category
    matchups = list(COMPARISON_DATA[category].keys())
    matchup = st.sidebar.selectbox(
        "The Matchup:",
        options=matchups,
        index=0
    )

    # Get the selected comparison data
    data = COMPARISON_DATA[category][matchup]

    # Main UI - The Ring
    st.title("⚡ The Tech Referee")
    st.markdown("---")

    # Display the fighters
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown(f"## {data['option_a']['name']}")
        st.markdown(f"### {data['option_a']['emoji']}")

    with col2:
        st.markdown("## 🥊 VS 🥊")

    with col3:
        st.markdown(f"## {data['option_b']['name']}")
        st.markdown(f"### {data['option_b']['emoji']}")

    st.markdown("---")

    # Comparison Matrix
    st.subheader("📊 Head-to-Head Comparison")

    # Create comparison dataframe
    comparison_df = pd.DataFrame({
        'Criteria': list(data['comparison'].keys()),
        data['option_a']['name']: [data['comparison'][key][0] for key in data['comparison'].keys()],
        data['option_b']['name']: [data['comparison'][key][1] for key in data['comparison'].keys()]
    })

    st.dataframe(comparison_df, use_container_width=True, hide_index=True)

    st.markdown("---")

    # The Referee's Logic - The Final Verdict
    st.subheader("⚖️ The Final Verdict")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"**{data['option_a']['name']} Wins When:**\n\n{data['verdict']['option_a_scenario']}")

    with col2:
        st.info(f"**{data['option_b']['name']} Wins When:**\n\n{data['verdict']['option_b_scenario']}")

    st.markdown("---")

    # Scorecard - Dev Experience Scores
    st.subheader("🏆 Developer Experience Scorecard")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.metric(
            label=f"{data['option_a']['name']} Dev Score",
            value=f"{data['scores']['option_a']}/10",
            delta=None
        )

    with col2:
        st.markdown("### 📈")

    with col3:
        st.metric(
            label=f"{data['option_b']['name']} Dev Score",
            value=f"{data['scores']['option_b']}/10",
            delta=None
        )

    # Footer
    st.markdown("---")
    st.markdown("*The Tech Referee: Settling debates with trade-offs, not opinions* 🥊")

if __name__ == "__main__":
    main()