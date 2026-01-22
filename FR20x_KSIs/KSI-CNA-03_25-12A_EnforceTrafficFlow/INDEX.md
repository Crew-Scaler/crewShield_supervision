# Service Mesh and Microsegmentation Papers Index
## Downloaded from ArXiv: December 10, 2025

**Total Papers:** 23 papers (service mesh and microsegmentation focus)
**Research Period:** 2024-2025
**Complete Summary:** See `../SERVICE_MESH_MICROSEGMENTATION_RESEARCH_SUMMARY.md`

---

## Directory Structure

### 1. service_mesh/ (7 papers)
Service mesh architectures, performance, observability, and distributed tracing

- `2411.02267_service_mesh_performance_mtls.pdf` - Performance comparison: Istio, Linkerd, Cilium (Nov 2024)
- `2405.13333_service_mesh_architectures.pdf` - Comprehensive survey (May 2024)
- `2403.04378_carisma_car_service_mesh.pdf` - Automotive service mesh (March 2024)
- `2312.01297_flatproxy_dpu_service_mesh.pdf` - DPU hardware acceleration (Dec 2023)
- `2406.06975_tracemesh_distributed_traces.pdf` - Scalable tracing (June 2024)
- `2510.02991_observability_tracing_metrics_patterns.pdf` - Observability patterns (Oct 2024)
- `2512.07638_service_discovery_genai.pdf` - Service discovery for GenAI (Dec 2024)

### 2. microsegmentation/ (4 papers)
Zero-trust microsegmentation, multi-tenancy, network isolation

- `2411.12162_microsegmented_cloud_zero_trust.pdf` - Multi-cloud zero-trust (Nov 2024) ⭐
- `2510.16067_multicloud_zero_trust_auth.pdf` - Multi-cloud workload auth (Oct 2024)
- `2403.01862_mts_multi_tenancy_virtual_networking.pdf` - Virtual network multi-tenancy (March 2024)
- `2309.03628_osmosis_smartnic_multitenancy.pdf` - SmartNIC multi-tenancy (Sept 2023)

### 3. mtls_zero_trust/ (4 papers)
Mutual TLS, identity-based authentication, SPIFFE/SPIRE

- `2401.09575_zero_trust_emerging_tech_survey.pdf` - Zero-trust survey (Jan 2024)
- `2410.18411_federated_sso_zero_trust_ai_hpc.pdf` - AI/HPC zero-trust (Oct 2024)
- `2504.14760_spiffe_workload_identity.pdf` - SPIFFE for CI/CD (April 2025) ⭐
- `2505.23792_zero_trust_foundation_models_iot.pdf` - Zero-trust for AI/IoT (May 2025)

### 4. policy_enforcement/ (7 papers)
Network policies, rate limiting, QoS, chaos engineering, resilience

- `2510.04052_network_policy_enforcement_service_mesh.pdf` - L3-L7 policy enforcement (Oct 2025) ⭐
- `2510.04516_rate_limiting_client_side.pdf` - Client-side rate limiting (Oct 2025)
- `2510.09851_qonnect_qos_kubernetes.pdf` - QoS orchestration (Oct 2025)
- `2411.05323_trade_network_traffic_scheduling.pdf` - Traffic-aware scheduling (Nov 2024)
- `2506.11176_chaos_engineering_model_discovery.pdf` - Model-based chaos engineering (June 2025)
- `2412.01416_chaos_engineering_multi_vocal_review.pdf` - Chaos engineering review (Dec 2024)
- `2507.16109_kubernetes_resilience_failure_injection.pdf` - Kubernetes resilience (July 2025)

### 5. ai_workloads/ (5 papers)
AI inference infrastructure, stateful microservices, LLM workloads

- `2504.03648_aibrix_llm_inference.pdf` - LLM inference infrastructure (April 2025) ⭐
- `2502.17443_ai_agent_enterprise_apis.pdf` - AI agent APIs (Feb 2025)
- `2506.09159_mose_stateful_microservices.pdf` - Stateful migration (June 2025)
- `2509.05794_stateful_migration_kubernetes.pdf` - Kubernetes stateful migration (Sept 2025)
- `2501.03547_metric_criticality_microservices.pdf` - Observability metrics (Jan 2025)

---

## Key Papers by Topic (⭐ = High Priority)

### Production-Ready Service Mesh
1. ⭐ `2411.02267_service_mesh_performance_mtls.pdf` - Definitive performance comparison
2. ⭐ `2405.13333_service_mesh_architectures.pdf` - Comprehensive survey

### Microsegmentation for Multi-Cloud
1. ⭐ `2411.12162_microsegmented_cloud_zero_trust.pdf` - Open-source zero-trust implementation
2. `2403.01862_mts_multi_tenancy_virtual_networking.pdf` - Multi-tenant isolation

### Identity and Zero-Trust
1. ⭐ `2504.14760_spiffe_workload_identity.pdf` - SPIFFE/SPIRE best practices
2. `2505.23792_zero_trust_foundation_models_iot.pdf` - Zero-trust for AI systems

### AI Workload Traffic Control
1. ⭐ `2504.03648_aibrix_llm_inference.pdf` - LLM inference with service mesh
2. ⭐ `2506.09159_mose_stateful_microservices.pdf` - Stateful AI workload migration

### Policy and Resilience
1. ⭐ `2510.04052_network_policy_enforcement_service_mesh.pdf` - L3-L7 policies
2. `2412.01416_chaos_engineering_multi_vocal_review.pdf` - Resilience testing

---

## Research Highlights

### Ambient Mesh (Sidecarless Service Mesh)
- **90%+ overhead reduction** vs traditional sidecars
- Istio Ambient reached GA (Nov 2024, v1.24)
- Cilium eBPF-based sidecarless architecture
- See: `2411.02267_service_mesh_performance_mtls.pdf`

### mTLS Performance Impact
| Service Mesh | Latency Increase |
|--------------|------------------|
| Istio Ambient | 8% (best) |
| Linkerd | 33% |
| Cilium | 99% |
| Istio (sidecar) | 166% (worst) |

Source: `2411.02267_service_mesh_performance_mtls.pdf`

### Stateful AI Workloads
- **77% reduction in migration downtime** (MOSE)
- Message-based state reconstruction (MS2M)
- Context-aware middleware for AI agents
- See: `2506.09159_mose_stateful_microservices.pdf`

### Zero-Trust Implementation
- SPIFFE/SPIRE for workload identity (Gartner 2025 trend)
- Microsegmentation with Istio + Calico (open-source)
- Multi-cloud authentication frameworks
- See: `2411.12162_microsegmented_cloud_zero_trust.pdf`

---

## How to Use This Collection

### For Cloud Architects
1. Start with `SERVICE_MESH_MICROSEGMENTATION_RESEARCH_SUMMARY.md`
2. Read performance comparison: `2411.02267_service_mesh_performance_mtls.pdf`
3. Review zero-trust implementation: `2411.12162_microsegmented_cloud_zero_trust.pdf`

### For AI/ML Engineers
1. Read LLM infrastructure: `2504.03648_aibrix_llm_inference.pdf`
2. Review stateful migration: `2506.09159_mose_stateful_microservices.pdf`
3. Study AI agent APIs: `2502.17443_ai_agent_enterprise_apis.pdf`

### For Security Engineers
1. Study SPIFFE/SPIRE: `2504.14760_spiffe_workload_identity.pdf`
2. Read zero-trust survey: `2401.09575_zero_trust_emerging_tech_survey.pdf`
3. Review policy enforcement: `2510.04052_network_policy_enforcement_service_mesh.pdf`

### For DevOps/SRE
1. Observability patterns: `2510.02991_observability_tracing_metrics_patterns.pdf`
2. Chaos engineering: `2412.01416_chaos_engineering_multi_vocal_review.pdf`
3. QoS orchestration: `2510.09851_qonnect_qos_kubernetes.pdf`

---

## Additional Resources

### Related Paper Collections
- `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-03_25-12A_EnforceTrafficFlow/references/sdn_frameworks/` - SDN papers
- `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-03_25-12A_EnforceTrafficFlow/references/network_virtualization/` - Network virtualization
- `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-03_25-12A_EnforceTrafficFlow/references/intent_based_networking/` - IBN papers

### Industry Resources (from web searches)
- Istio Ambient Mode: https://istio.io/latest/blog/2024/ambient-reaches-ga/
- Cilium Service Mesh: https://cilium.io/
- SPIFFE/SPIRE: https://spiffe.io/
- CNCF Service Mesh Landscape: https://landscape.cncf.io/

---

**Last Updated:** December 10, 2025
**Curator:** ArXiv Research Survey on Service Mesh and Microsegmentation
**Contact:** See `../SERVICE_MESH_MICROSEGMENTATION_RESEARCH_SUMMARY.md` for detailed analysis
