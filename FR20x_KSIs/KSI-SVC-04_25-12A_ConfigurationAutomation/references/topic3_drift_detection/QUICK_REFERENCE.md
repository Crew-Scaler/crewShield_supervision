# Quick Reference: Top 10 Papers for ML-Driven Configuration Drift Detection

**Issue #69 Topic 3 | Research Date: December 25, 2025**

---

## Papers by ML Method

### LSTM/RNN-Based (9 papers)
1. **2508.16336v1** - Unsupervised Online Detection (LSTM for concept drift)
2. **2510.27146v1** - SERVIMON (LSTM for time-series)
3. **2506.13828v1** - Hybrid Meta-Learning (CNN-LSTM)
4. **2411.03365v1** - 5G Threat Detection (Self-attention RNN autoencoder)
5. **2511.12351v1** - Dynamic Reward Scaling (LSTM-DQN)
6. **2510.15010v1** - Wind Turbine (LSTM autoencoder ensemble)
7. **2503.12534v1** - Time-EAPCR-T (LSTM-based)
8. **2403.12864v2** - Spacecraft Anomaly (LSTM comparison)
9. **2501.02107v1** - Water Contamination (LSTM)

### Autoencoder-Based (7 papers)
1. **2508.16336v1** - Unsupervised Online Detection
2. **2411.03365v1** - 5G Threat Detection (RNN autoencoder)
3. **2510.15010v1** - Wind Turbine (VAE + LSTM + Transformer autoencoders)
4. **2503.12534v1** - Time-EAPCR-T
5. **2403.12864v2** - Spacecraft Anomaly
6. **2305.08977v2** - Streaming Data (Autoencoder + concept drift)
7. **2502.19307v3** - Complex Dynamical Systems

### Variational Autoencoder (VAE) (5 papers)
1. **2506.13828v1** - Hybrid Meta-Learning (VAE for unsupervised)
2. **2511.12351v1** - Dynamic Reward Scaling (VAE + RL)
3. **2510.15010v1** - Wind Turbine (VAE ensemble)
4. **2502.19307v3** - Complex Dynamical Systems
5. **2503.12534v1** - Time-EAPCR-T

### Transformer-Based (5 papers)
1. **2510.15010v1** - Wind Turbine (Transformer ensemble)
2. **2503.12534v1** - Time-EAPCR-T
3. **2502.19307v3** - Complex Dynamical Systems
4. **2411.03365v1** - 5G Threat Detection (self-attention)
5. **2403.12864v2** - Spacecraft Anomaly

### Isolation Forest (3 papers)
1. **2511.03661v1** - SHIELD Healthcare IoT
2. **2506.13828v1** - Hybrid Meta-Learning
3. **2510.27304v1** - Binary Anomaly Detection

---

## Papers by Application Domain

### Critical Infrastructure Monitoring
- **2508.16336v1** - Water Distribution Networks (pipes, leakages)
- **2510.15010v1** - Wind Turbines (renewable energy)
- **2403.12864v2** - Spacecraft Operations

### Network & 5G
- **2411.03365v1** - 5G Networks (spectral intrusion)
- **2510.27304v1** - IoT Traffic (streaming)

### Cloud & Observability
- **2510.27146v1** - SERVIMON (cloud-native stack: Prometheus, Kafka, Grafana)

### Industrial IoT & Security
- **2511.03661v1** - Healthcare IoT Security
- **2503.12534v1** - Industrial Equipment (Industry 4.0)
- **2110.04049v1** - IIoT Sensors
- **2309.07730v1** - Underwater Acoustic Networks

### Cyber-Physical Systems
- **2506.13828v1** - Nonlinear Dynamical Systems
- **2502.19307v3** - Complex Dynamical Systems (predictive maintenance)

---

## Papers by Research Focus

### Unsupervised Learning
1. **2508.16336v1** - Unsupervised online detection ⭐
2. **2506.13828v1** - VAE unsupervised anomaly
3. **2510.15010v1** - Unsupervised ensemble
4. **2403.03576v3** - Unsupervised incremental learning

### Real-Time Detection
1. **2411.03365v1** - Real-time threat detection (5G)
2. **2510.27146v1** - Real-time monitoring (observatories)
3. **2503.12534v1** - Real-time industrial monitoring

### Concept Drift Handling
1. **2508.16336v1** - Concept drift modeled as leakage ⭐
2. **2501.02107v1** - Water contamination under drift
3. **2305.08977v2** - Streaming data with drift adaptation
4. **2403.03576v3** - Dual concept drift detection
5. **2410.10041v2** - WormKAN for drift tracking
6. **2510.27304v1** - IoT traffic under drift

### Predictive & Forecasting
1. **2506.13828v1** - Anomaly forecasting (physics-inspired)
2. **2510.27146v1** - Predictive maintenance
3. **2511.12351v1** - Time series anomaly prediction

### Ensemble Methods
1. **2510.15010v1** - VAE + LSTM + Transformer ensemble ⭐
2. **2506.13828v1** - Hybrid meta-learning

---

## Implementation Priority (by Score & Relevance)

### Tier 1: Must Read (Score 100)
1. **2508.16336v1** - Best match: LSTM + concept drift + infrastructure
2. **2510.27146v1** - Cloud-native stack reference architecture
3. **2506.13828v1** - CNN-LSTM + VAE hybrid approach

### Tier 2: Strong Candidates (Score 97-99)
4. **2511.12351v1** - VAE + LSTM + RL (advanced)
5. **2502.19307v3** - Systematic framework (theory)
6. **2510.15010v1** - Ensemble methods (practical)

### Tier 3: Comparative Studies (Score 96-97)
7. **2503.12534v1** - Universal approach (Industry 4.0)
8. **2403.12864v2** - Architecture comparison (benchmarking)

### Tier 4: Specialized (Score 100 but specific)
9. **2411.03365v1** - 5G-specific (network layer)
10. **2511.03661v1** - Healthcare IoT (domain-specific)

---

## Key Technical Insights by Paper

### 2508.16336v1: Unsupervised Online Detection ⭐⭐⭐
- **Best for:** Configuration drift as concept drift modeling
- **Architecture:** LSTM-based online learning
- **Key Innovation:** Collective anomalies (blockages) vs. concept drift (leakages)
- **Applicability:** Infrastructure-as-Code validation, config drift over time

### 2510.27146v1: SERVIMON ⭐⭐⭐
- **Best for:** Cloud-native monitoring stack design
- **Stack:** Prometheus + Grafana + Cassandra + Kafka + InfluxDB
- **Key Innovation:** Scalable telemetry collection + ML integration
- **Applicability:** Kubernetes monitoring, distributed system observability

### 2506.13828v1: Hybrid Meta-Learning ⭐⭐⭐
- **Best for:** Physics-inspired anomaly forecasting
- **Architecture:** CNN-LSTM (spatio-temporal) + VAE (unsupervised)
- **Key Innovation:** Deep ensembles for nonlinear dynamics
- **Applicability:** Complex config dependencies, temporal drift patterns

### 2511.12351v1: Dynamic Reward Scaling ⭐⭐
- **Best for:** Adaptive threshold tuning
- **Architecture:** VAE + LSTM-DQN + active learning
- **Key Innovation:** Reinforcement learning for anomaly detection
- **Applicability:** Continuous learning from config changes

### 2502.19307v3: Complex Dynamical Systems ⭐⭐
- **Best for:** Theoretical framework
- **Architecture:** Embedding theory + physics-inspired consistency
- **Key Innovation:** Structured temporal dependencies
- **Applicability:** Cyber-physical infrastructure, predictive maintenance

### 2510.15010v1: Wind Turbine Detection ⭐⭐
- **Best for:** Ensemble methods
- **Architecture:** VAE + LSTM Autoencoder + Transformer ensemble
- **Key Innovation:** Feature engineering across architectures
- **Applicability:** High-dimensional SCADA-like data (Kubernetes metrics)

### 2411.03365v1: 5G Threat Detection ⭐
- **Best for:** Self-attention mechanisms
- **Architecture:** Self-attention RNN autoencoder
- **Key Innovation:** Waveform-level anomaly detection
- **Applicability:** Low-latency drift detection

### 2503.12534v1: Time-EAPCR-T ⭐
- **Best for:** Universal industrial approach
- **Architecture:** Deep learning for multi-source heterogeneous data
- **Key Innovation:** Handling noise, coupling, temporal interactions
- **Applicability:** Multi-cloud config drift (heterogeneous sources)

### 2403.12864v2: Spacecraft Comparison
- **Best for:** Benchmarking architectures
- **Architecture:** Compares LSTM, Autoencoder, Transformer, etc.
- **Key Innovation:** Performance metrics for critical systems
- **Applicability:** High-reliability requirements (compliance, audit)

### 2511.03661v1: SHIELD Healthcare IoT
- **Best for:** Model comparison (8 models)
- **Architecture:** XGBoost, KNN, semi-supervised learning
- **Key Innovation:** 200K records benchmark
- **Applicability:** Large-scale config repositories

---

## Reading Order Recommendation

### For Immediate Implementation (Issue #69)
1. **2508.16336v1** - Core LSTM + concept drift approach
2. **2510.27146v1** - Cloud-native monitoring architecture
3. **2510.15010v1** - Ensemble methods (VAE + LSTM + Transformer)

### For Advanced Features
4. **2511.12351v1** - Reinforcement learning for adaptive thresholds
5. **2506.13828v1** - Hybrid meta-learning for forecasting

### For Theoretical Grounding
6. **2502.19307v3** - Systematic framework (embedding theory)

### For Benchmarking
7. **2403.12864v2** - Architecture comparison study
8. **2511.03661v1** - 8-model comparison

### For Specialized Insights
9. **2503.12534v1** - Universal industrial approach
10. **2411.03365v1** - Self-attention mechanisms

---

## Code/Implementation Availability

Check each paper's ArXiv page for:
- GitHub repositories
- Supplementary materials
- Datasets used

**ArXiv Links Template:**
- `https://arxiv.org/abs/[ArXiv_ID]` (abstract)
- `https://arxiv.org/pdf/[ArXiv_ID]` (PDF, already downloaded)

---

## Additional Context Papers (From Initial Search)

### Also Downloaded (Not in Top 10 Expanded)
- **2506.15831v2** - Adaptive Anomaly Detection (concept drift)
- **2501.02107v1** - Water Contamination (concept drift)
- **2510.27304v1** - Binary Anomaly (IoT streaming)
- **2512.12205v1** - Urban Streetlight (spatio-temporal drift)
- **2410.10041v2** - WormKAN (concept drift tracking)
- **2403.03576v3** - Incremental Learning (dual drift)
- **2305.08977v2** - Streaming Data (autoencoder + drift)
- **2110.04049v1** - IIoT Sensors (minimal config)
- **2309.07730v1** - Underwater Networks (adaptive IDS)

---

## Search Strategy Notes

**Successful Queries (70+ results):**
- `drift detection + anomaly`
- `concept drift + detection`
- `anomaly detection + time-series`
- `isolation forest OR autoencoder`
- `LSTM + anomaly`

**Limited Results (<25):**
- `configuration drift detection` (0 results) ❌
- `infrastructure as code` (22 results) ⚠️
- `kubernetes + drift` (9 results) ⚠️

**Research Gap Identified:**
- Configuration-specific drift detection is underexplored
- Opportunity to adapt time-series anomaly methods to config management
- IaC and Kubernetes monitoring need more research

---

*Generated: December 25, 2025*
*Total Papers: 19 PDFs downloaded (10 from expanded search)*
*Directory: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-04_25-12A_ConfigurationAutomation/references/topic3_drift_detection/`*
