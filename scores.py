def calculate_rfm_scores(customer_data: pandas.DataFrame) -> pandas.DataFrame:
    """Calculate RFM scores for each customer.

    Args:
        customer_data: DataFrame of customer data, including columns for recency,
            frequency, and monetary value.

    Returns:
        DataFrame of RFM scores for each customer.
    """
    # Calculate recency score
    max_recency = customer_data["recency"].max()
    customer_data["recency_score"] = customer_data["recency"].apply(lambda x: 5 - (x / max_recency) * 5)

    # Calculate frequency score
    max_frequency = customer_data["frequency"].max()
    customer_data["frequency_score"] = customer_data["frequency"].apply(lambda x: 5 - (x / max_frequency) * 5)

    # Calculate monetary value score
    max_monetary_value = customer_data["monetary_value"].max()
    customer_data["monetary_value_score"] = customer_data["monetary_value"].apply(lambda x: 5 - (x / max_monetary_value) * 5)

    return customer_data