def create_campaign(rfm_scores: pd.DataFrame) -> Dict[str, str]:
    """Create a personalized marketing campaign for each customer based on their segment.

    Args:
        rfm_scores: DataFrame of RFM scores with a column for customer segment.

    Returns:
        Dictionary mapping customer IDs to personalized marketing campaigns.
    """
    campaigns = {}
    for _, row in rfm_scores.iterrows():
        if row["segment"] == "bronze":
            campaigns[row["customer_id"]] = f"Get a 10% discount on your next purchase!"
        elif row["segment"] == "silver":
            campaigns[row["customer_id"]] = f"Enjoy free shipping on your next order!"
        elif row["segment"] == "gold":
            campaigns[row["customer_id"]] = f"We've selected a special gift just for you!"

    return campaigns