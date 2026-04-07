# Summary — Autonomous Systems Resume Strategy

---

## ✅ LOCKED SUMMARY

> MS Computer Engineering (ASU, GPA 3.81, May 2026) with hands-on autonomous systems and production AI experience. Implemented the full self-driving pipeline in C++ from scratch — sensor fusion (EKF), LiDAR localization (ICP/SVD, 4× baseline accuracy), behavior planning (FSM), and PID vehicle control — on the Waymo Open Dataset and CARLA simulator; also built a physical autonomous car as a hardware capstone and shipped Trezzit (trezzit.com), a live production AI SaaS with 600+ users.

**Why this works:**
- "Full self-driving pipeline in C++ from scratch" — directly answers the #1 screening question for AV new-grad roles: can you implement AV algorithms, not just call a library?
- Four named sub-systems (EKF / ICP+SVD / FSM / PID) show stack-wide coverage in one sentence
- "Waymo Open Dataset and CARLA simulator" — both proper nouns signal familiarity with real AV tooling
- "Physical autonomous car as a hardware capstone" — hardware credential; rare for pure software candidates
- Trezzit anchor: production deployment credibility anchors the AV academic work in real-world execution

---

## 🎯 TARGET ROLES

This resume targets:
- **Tesla** — Autopilot Perception, Motion Planning, Sensor Fusion (New Grad SWE / SWE Intern)
- **Waymo** — Software Engineer (Perception / Mapping & Localization / Behavior)
- **Mobileye** — Perception / AV Systems Engineer
- **Cruise, Aurora, Motional, Zoox** — similar AV pipeline roles
- **Robotics companies** (Boston Dynamics, Figure, Apptronik) — leveraging Diffusion Policy + hardware capstone

NOT for:
- Pure AI Engineer/LLM roles → use resume_strategy_ai_eng
- Full-Stack product roles → use resume_strategy_full_stack
- EDA/Chip Design → use resume_strategy_eda

---

## 🔁 BACKUP SUMMARY VERSIONS

### B — Robotics / Robot Learning emphasis
> MS Computer Engineering (ASU, GPA 3.81, May 2026) with hands-on experience across the autonomous systems stack and robot learning. Implemented a full C++ self-driving pipeline (EKF, ICP localization achieving 4× baseline accuracy, FSM behavior planning, PID control on CARLA), adapted Diffusion Policy for visuomotor control in MuJoCo, and built a physical autonomous car as hardware capstone.

*Use when: JD emphasizes robot learning, imitation learning, policy gradients, MuJoCo, or robotic manipulation alongside AV.*

### C — Production Systems angle (for AV + Systems SW hybrid roles)
> MS Computer Engineering (ASU, GPA 3.81, May 2026) with hands-on autonomous systems and production software experience. Built a full C++ self-driving pipeline on Waymo Open Dataset + CARLA and shipped Trezzit, a production AI SaaS (trezzit.com) with 600+ users and 995 automated tests — demonstrating both AV algorithmic depth and production engineering rigor.

*Use when: JD asks for "production-quality code," testing culture, CI/CD, or deployment alongside AV algorithms.*

---

## 🎯 JD-BASED SWAP GUIDE

| JD Signal | Swap / Add |
|---|---|
| "SLAM" / "localization" / "mapping" | Emphasize ICP from scratch, SLAM in skills, NDT benchmarking; mention Waymo dataset |
| "Sensor fusion" / "EKF" / "Kalman filter" | Lead with EKF bullet: predict/update, Mahalanobis, track lifecycle — all from scratch |
| "Perception" / "LiDAR" / "point cloud" | Lead with Perception bullet: BEV projection, YOLOv4 + FPN ResNet18, Waymo dataset pipeline |
| "Motion planning" / "trajectory" | Lead with Planning & Control: FSM, cubic spiral trajectories, collision + lane-deviation cost |
| "C++" / "CMake" / "real-time" | Emphasize all C++ from-scratch implementations; mention CMake and PCL in skills |
| "ROS" / "ROS2" | Add "ROS2 (familiar)" to C++/Systems skills row if you have any ROS exposure; do NOT add if none |
| "Robot learning" / "imitation learning" / "diffusion" | Swap in Summary Version B; move Diffusion Policy earlier in project list |
| "Hardware" / "embedded" / "real car" | Emphasize Raspberry Pi capstone: I2C, Arduino, physical hardware, real-time control |
| "Waymo" specifically | Mention Waymo Open Dataset in summary and first bullet; SLAM in skills |
| "Tesla" specifically | Emphasize C++, real-time systems, BEV perception (Tesla uses BEV heavily), PID |
| "Production" / "reliability" / "testing" | Use Summary Version C; lead with Trezzit: 995 automated tests, CI/CD, live users |
| "Multi-object tracking" / "MOT" | Highlight EKF track lifecycle (initialization, confirmation, deletion) + Multi-Object Tracking in skills |

---

## 📌 KEY DIFFERENTIATORS

1. **ICP from scratch with SVD** — 0.299m pose error over 172m (requirement <1.2m), 4× better than baseline. This is the single strongest quantitative AV result. Always keep it.

2. **EKF from scratch** — full predict/update, Mahalanobis data association, track lifecycle. Depth signal that distinguishes from candidates who used library wrappers.

3. **Full stack coverage** — Perception → Sensor Fusion → Localization → Planning → Control. Few new grads can claim all five layers.

4. **Physical hardware** — Raspberry Pi + Arduino capstone with real driving. Rare credential.

5. **CARLA simulator** — production-grade AV simulator; distinguishes from purely academic work.

---

## ⚠️ KNOWN TRADEOFFS & REVIEWER NOTES

**Udacity attribution deliberately omitted:**
The "Self-Driving Car Engineering Pipeline" entry does not mention Udacity. This is intentional — "nanodegree" carries mixed signals with AV hiring managers who may downweight it vs. actual MS coursework. The implementations (EKF, ICP, FSM, PID) are from scratch and the depth is real. If a JD or hiring manager specifically asks, clarify honestly in interview.

**ROS not listed:**
If you haven't used ROS, do NOT add it to skills. Adding it without experience is a red flag in AV interviews where ROS knowledge is tested technically. If you pick up any ROS exposure before applying, add "ROS2 (familiar)" to the C++/Systems row.

**Recent work is non-AV (Trezzit, SiliconCrew):**
A reviewer may notice the most recent two projects are LLM/SaaS-focused (late 2025). The counter-argument: they demonstrate production deployment maturity, which AV teams value. Address in cover letter: "My AV fundamentals are strong; I've been building production systems to complement algorithmic depth."

**Diffusion Policy is team project:**
Currently marked "team project" with no individual contribution stated. Acceptable for now. If you take on a more significant role in the project before applying, expand the bullet.

**GPA 3.81 always** — never round to 3.8.
