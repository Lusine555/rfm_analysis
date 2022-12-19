def segment_customers(rfm_scores: pd.DataFrame) -> pd.DataFrame:
    """Segment customers into different groups based on their RFM scores.

    Args:
        rfm_scores: DataFrame of RFM scores for each customer.

    Returns:
        DataFrame of RFM scores with a new column for customer segment.
    """
    # Assign segments based on RFM scores
    rfm_scores["segment"] = "bronze"
    rfm_scores.loc[rfm_scores["recency_score"] > 3, "segment"] = "silver"
    rfm_scores.loc[rfm_scores["recency_score"] > 4, "segment"] = "gold"

    return rfm_scores
