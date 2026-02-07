def evaluate_insights(insights):
    if not insights:
        return {
            "total_insights": 0,
            "score": 0.0
        }

    unique_insights = set(insights)
    diversity_score = len(unique_insights) / len(insights)

    return {
        "total_insights": len(insights),
        "unique_insights": len(unique_insights),
        "diversity_score": round(diversity_score, 2)
    }