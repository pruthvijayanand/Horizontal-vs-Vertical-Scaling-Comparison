# Horizontal Scaling vs Vertical Scaling

## Introduction

Scaling is the process of increasing the capacity of an application to handle more users and requests.

Cloud platforms use two major scaling techniques:

- Horizontal Scaling
- Vertical Scaling

---

# Horizontal Scaling

Horizontal Scaling means adding more servers to distribute workload.

Example:

```
Server1
Server2
Server3
```

connected through a Load Balancer.

## Advantages

- High Availability
- Better Fault Tolerance
- Easy Cloud Expansion
- No Single Point of Failure

## Disadvantages

- More Infrastructure
- Higher Complexity
- Requires Load Balancer

---

# Vertical Scaling

Vertical Scaling means upgrading an existing server.

Example

Upgrade

- CPU
- RAM
- Storage

without adding new servers.

## Advantages

- Easy to Implement
- Lower Complexity
- Good for Small Applications

## Disadvantages

- Hardware Limitations
- Downtime
- Single Point of Failure

---

# Comparison Table

| Feature | Horizontal | Vertical |
|----------|------------|----------|
| Servers | Multiple | Single |
| Cost | Higher | Lower |
| Downtime | Low | Medium |
| Fault Tolerance | High | Low |
| Scalability | Unlimited | Limited |
| Complexity | High | Low |

---

# Real World Examples

Horizontal Scaling

- Netflix
- Amazon
- Google
- Facebook

Vertical Scaling

- Small Business Applications
- Database Servers
- Local Enterprise Applications

---

# Conclusion

Horizontal Scaling is preferred for cloud-native applications because it provides better scalability and fault tolerance.

Vertical Scaling is suitable for smaller applications where simplicity is more important than scalability.