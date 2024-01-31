from datetime import timedelta
from feast import Entity, Feature, FeatureView, FileSource, ValueType, Field
from feast.types import String, Int64
from feast.value_type import ValueType
#
zipcode = Entity(name="zipcode", value_type=ValueType.INT64)
#comment    
zipcode_source = FileSource(
    path="data/zipcode_table.parquet",
    timestamp_field="event_timestamp",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)


zipcode_features = FeatureView(
    name="zipcode_features",
    entities=[Entity(name="zipcode", join_keys=["zipcode"])],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="city", dtype=String),
        Field(name="state", dtype=String),
        Field(name="location_type", dtype=String),
        Field(name="tax_returns_filed", dtype=Int64),
        Field(name="population", dtype=Int64),
        Field(name="total_wages", dtype=Int64),
    ],
    source=zipcode_source,
)

dob_ssn = Entity(
    name="dob_ssn",
    value_type=ValueType.STRING,
    description="Date of birth and last four digits of social security number",
)


credit_history_source = FileSource(
    path="data/credit_history.parquet",
    timestamp_field="event_timestamp",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

credit_history = FeatureView(
    name="credit_history",
    entities=[Entity(name="dob_ssn", join_keys=["dob_ssn"])],
    ttl=timedelta(days=90),
    schema=[
        Field(name="credit_card_due", dtype=Int64),
        Field(name="mortgage_due", dtype=Int64),
        Field(name="student_loan_due", dtype=Int64),
        Field(name="vehicle_loan_due", dtype=Int64),
        Field(name="hard_pulls", dtype=Int64),
        Field(name="missed_payments_2y", dtype=Int64),
        Field(name="missed_payments_1y", dtype=Int64),
        Field(name="missed_payments_6m", dtype=Int64),
        Field(name="bankruptcies", dtype=Int64),
    ],
    source=credit_history_source,
)