# Import the functions from the rfm_analysis package
from rfm_analysis import calculate_rfm_scores, segment_customers, create_campaign

# Prepare the input data
customer_data = pd.DataFrame({
    "customer_id": ["A", "B", "C", "D", "E"],
    "recency": [10, 5, 1, 15, 20],
    "frequency": [3, 5, 2, 4, 1],
    "monetary_value": [100, 250, 50, 200, 75]
})

# Calculate RFM scores
rfm_scores = calculate_rfm_scores(customer_data)
print(rfm_scores)

# Segment customers
segmented_customers = segment_customers(rfm_scores)
print(segmented_customers)

# Create campaigns
campaigns = create_campaign(segmented_customers)
print(campaigns)
