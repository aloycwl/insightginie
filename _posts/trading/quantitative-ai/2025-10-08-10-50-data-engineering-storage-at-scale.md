---
layout: post
title: "(10/50) Data engineering &amp; storage at scale"
date: 2025-10-08T10:19:09
categories: [11698]
original_url: https://insightginie.com/10-50-data-engineering-storage-at-scale
---

In today's data-driven world, the ability to efficiently store, process, and analyze vast amounts of data is not just an advantage—it's a necessity. This is especially true for time-series data, which streams continuously from sensors, devices, and applications, recording changes over time. Imagine managing minute-level data from hundreds or thousands of assets; the sheer volume and velocity present significant engineering challenges. This article delves into the strategies and technologies essential for handling such scale, culminating in a practical storage schema design for high-frequency asset data.

The Unstoppable Influx: Why Traditional Methods Fall Short
----------------------------------------------------------

The core problem with time-series data at scale is its unique characteristics:

* **High Volume & Velocity:** Data points arrive constantly, often every second or minute, leading to petabytes of data over time.
* **Append-Only Nature:** New data is almost always appended, rarely updated, but queries often involve wide time ranges and aggregations.
* **Temporal Queries:** The most common queries involve time windows (e.g., “what was the average temperature last hour?”) or comparisons across periods.
* **Cardinality:** While the number of assets might be fixed, the number of distinct metric values can be very high, and each asset might have multiple metrics.

Traditional relational databases (RDBMs), while versatile, often struggle with the write amplification, indexing overhead, and query performance for time-series workloads, especially when dealing with the scale required for minute-level data from 200 assets.

The Power of Columnar Storage and Parquet
-----------------------------------------

To overcome these challenges, specialized approaches are required. One fundamental concept is **columnar storage**. Unlike row-oriented databases where an entire row is stored together, columnar storage stores data column by column. This offers several profound advantages for analytical workloads:

* **Superior Compression:** Data within a single column is often of the same type and has similar values (e.g., all timestamps, all temperature readings). This allows for highly effective compression algorithms, significantly reducing storage footprint.
* **Faster Query Performance:** When a query only needs a few columns (e.g., average temperature), only those relevant columns need to be read from disk, not entire rows. This dramatically reduces I/O.
* **Optimized for Aggregations:** Aggregations (SUM, AVG, MIN, MAX) are inherently faster because the data for a specific column is contiguous.

**Apache Parquet** is a leading open-source columnar storage format designed for efficient data storage and retrieval in big data ecosystems. It's language-agnostic and widely used in data lakes and data warehousing solutions. Parquet files are self-describing, containing schema information, and support complex nested data structures. While not a database itself, Parquet is a critical component for storing historical or analytical data efficiently.

Time-Series Databases: The Engine for High-Frequency Data
---------------------------------------------------------

For primary, real-time ingestion and querying of time-series data, a **Time-Series Database (TSDB)** is often the optimal choice. TSDBs are purpose-built to handle the unique demands of time-stamped data. Key characteristics include:

* **Optimized Data Layout:** They organize data by time, often partitioning or sharding data based on time intervals, which makes time-range queries extremely fast.
* **Efficient Indexing:** Specialized indexing for timestamps and tags allows for rapid retrieval of specific data points or ranges.
* **Built-in Functions:** Many TSDBs offer native functions for aggregation, downsampling, interpolation, and other time-series specific operations.
* **High Ingestion Rates:** Designed for high write throughput, essential for continuous data streams.

Popular TSDBs include InfluxDB, Prometheus, OpenTSDB, and TimescaleDB (a PostgreSQL extension). For our assignment, we will consider TimescaleDB due to its SQL compatibility and robust features, combining the power of a TSDB with the familiarity and reliability of PostgreSQL.

Mastering Incremental Updates at Scale
--------------------------------------

For time-series data, the concept of “updates” is typically replaced by “appends.” Data points, once recorded, are usually immutable. **Incremental updates** in this context refer to the efficient process of continuously adding new data without re-processing or re-writing existing data. This is crucial for maintaining high ingestion rates and keeping systems performant.

A well-designed data pipeline will typically:

1. Ingest new data streams (e.g., from IoT devices, APIs).
2. Perform light transformation or validation.
3. Append data to the primary TSDB.
4. Optionally, periodically extract, transform, and load (ETL) aggregated or older data into more cost-effective archival storage (e.g., Parquet files in a data lake).

This append-only model simplifies data consistency and improves write performance significantly compared to systems that require frequent updates to existing records.

The Assignment: Designing a Robust Storage Schema for 200 Assets (Minute-Level Data)
------------------------------------------------------------------------------------

Let's tackle the core challenge: designing a storage schema for minute-level data from 200 assets. Each asset generates multiple metrics (e.g., temperature, pressure, humidity, power consumption) every minute. We need a solution that is scalable, performs well for both real-time dashboards and historical analysis, and is cost-effective.

### Defining the Challenge Parameters:

* **Number of Assets:** 200
* **Data Frequency:** Minute-level (1 point per minute per asset)
* **Data Granularity:** High precision (e.g., float or double for metric values)
* **Expected Queries:**
  + Retrieve all metrics for a single asset over a time range.
  + Retrieve a specific metric for all assets over a time range.
  + Aggregate metrics (average, min, max) over various time windows (hour, day, week).
  + Identify outliers or anomalies.
* **Retention:** Full granularity for 3-6 months; downsampled data for several years.

### Proposed Primary Storage Solution: TimescaleDB on PostgreSQL

Given the requirements, a hybrid approach leveraging TimescaleDB as the primary high-ingestion/query store and Parquet for archival/deep analytics offers the best balance.

#### 1. Database Choice & Schema Structure

We'll use TimescaleDB for its robust time-series capabilities built on top of PostgreSQL, providing a familiar SQL interface and ACID compliance.

**Table: `asset_metrics` (Hypertable)**

```
CREATE TABLE asset_metrics ( timestamp TIMESTAMPTZ NOT NULL, -- The time of the reading (minute-level) asset_id INTEGER NOT NULL, -- Foreign key to an assets metadata table metric_type TEXT NOT NULL, -- E.g., 'temperature', 'pressure', 'humidity' value DOUBLE PRECISION NOT NULL, -- The measured value tags JSONB -- Optional: for flexible additional metadata (e.g., sensor_id, location)
); -- Convert to a TimescaleDB hypertable, partitioning by time and asset_id
SELECT create_hypertable('asset_metrics', 'timestamp', chunk_time_interval => INTERVAL '1 day', partition_column => 'asset_id', number_partitions => 8); -- Create a composite index for efficient querying
CREATE INDEX ix_asset_metrics_time_asset_metric ON asset_metrics (timestamp DESC, asset_id, metric_type);
```

**Rationale:**

* **`timestamp`:** Essential for all time-series queries. `TIMESTAMPTZ` handles timezones correctly.
* **`asset_id`:** Allows quick filtering by asset. An `assets` lookup table would store asset names, locations, and other static metadata (`CREATE TABLE assets (id INTEGER PRIMARY KEY, name TEXT, location TEXT, ...);`).
* **`metric_type` & `value`:** This 'narrow' table design is flexible. Instead of adding a new column for every new metric, we add a new row. This scales well for an unknown or evolving number of metrics per asset. For a fixed, small number of metrics, a 'wide' table (e.g., `temp DOUBLE PRECISION, pressure DOUBLE PRECISION`) might be considered, but the narrow approach is generally more robust for evolving IoT data.
* **`tags JSONB`:** Provides schema flexibility for additional, non-core metadata that might vary between metrics or assets.
* **Hypertable Partitioning:** TimescaleDB automatically partitions data by time (e.g., into daily chunks) and further by `asset_id`. This significantly speeds up queries by only scanning relevant chunks and allows for efficient data retention policies. We chose 8 partitions for 200 assets, which means ~25 assets per partition.
* **Indexing:** A composite index on `(timestamp DESC, asset_id, metric_type)` supports the most common queries (latest data for an asset, specific metric for an asset over time).

#### 2. Handling Incremental Updates

With TimescaleDB, incremental updates are handled simply by `INSERT` statements. The hypertable structure is optimized for high-volume appends. Data ingestion pipelines (e.g., using Kafka, AWS Kinesis, or custom scripts) would feed new minute-level data points into this table continuously.

#### 3. Data Retention and Downsampling

To manage storage costs and optimize query performance for long-term analysis, a multi-tiered approach is essential:

* **Tier 1 (Hot Data – TimescaleDB):** Full minute-level granularity for 3-6 months. TimescaleDB's data retention policies can automatically drop old chunks.
* **Tier 2 (Warm Data – TimescaleDB Aggregates):** Create continuous aggregates (materialized views in TimescaleDB) for hourly or daily averages, mins, and maxes. This aggregated data can be retained for 1-2 years within TimescaleDB, significantly reducing the data volume for older periods.
* **Tier 3 (Cold Data – Data Lake with Parquet):** For data older than 6 months (or after aggregation), move the raw minute-level data (or even the hourly aggregates) into a data lake (e.g., S3, ADLS) as Parquet files.

**Why Parquet for Cold Storage?**

* **Cost-Effective:** Cloud object storage is significantly cheaper than database storage.
* **Extreme Compression:** Parquet's columnar nature and compression codecs make it highly efficient for static, historical data.
* **Analytical Power:** Tools like Apache Spark, Presto, Athena, or Databricks can directly query Parquet files in the data lake for complex, ad-hoc historical analysis without loading them into a database.
* **Long-Term Archival:** Ideal for compliance and long-term data preservation.

An ETL job would periodically (e.g., daily or weekly) extract old minute-level data from TimescaleDB, transform it if necessary, and write it to Parquet files in the data lake, partitioned by year/month/day/asset for optimal query performance in the lake (e.g., `s3://data-lake/asset_metrics/year=2023/month=01/day=01/asset_id=123/data.parquet`).

### Scalability and Performance Considerations

* **Vertical Scaling:** Start with a powerful PostgreSQL/TimescaleDB instance.
* **Horizontal Scaling:** TimescaleDB supports distributed hypertables for extreme scale, allowing you to shard data across multiple PostgreSQL instances.
* **Connection Pooling:** Use connection pooling (e.g., PgBouncer) to manage database connections efficiently.
* **Monitoring:** Continuously monitor database performance (CPU, memory, I/O, query execution times) to identify and address bottlenecks.

Beyond the Schema: Operationalizing Your Data Platform
------------------------------------------------------

A robust schema is just one piece of the puzzle. For a high-performing data platform, also consider:

* **Data Ingestion Pipeline:** A reliable and fault-tolerant system (e.g., Kafka, Pub/Sub) to collect and stream data from assets to the database.
* **Monitoring & Alerting:** Implement comprehensive monitoring for data quality, pipeline health, and database performance.
* **Backup & Disaster Recovery:** Regular backups and a tested disaster recovery plan are non-negotiable.
* **Security:** Implement robust access controls, encryption at rest and in transit, and regular security audits.
* **Cost Optimization:** Regularly review storage tiers, instance sizes, and query patterns to optimize cloud spending.

Conclusion: Building a Future-Proof Data Foundation
---------------------------------------------------

Designing a storage schema for minute-level data from 200 assets at scale requires a thoughtful combination of specialized technologies and design principles. By leveraging the power of Time-Series Databases like TimescaleDB for high-velocity ingestion and real-time queries, complemented by columnar formats like Parquet for cost-effective archival and deep analytical processing, we can build a highly performant, scalable, and future-proof data foundation. This approach ensures that your organization can not only keep pace with the relentless flow of data but also extract maximum value from it to drive informed decisions.